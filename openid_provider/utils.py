# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 fdm=indent : */
# some code from http://www.djangosnippets.org/snippets/310/ by simon
# and from examples/djopenid from python-openid-2.2.4
from openid_provider import conf
from openid.extensions import ax, sreg

from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from django.core.urlresolvers import reverse

def openid_is_authorized(request, identity_url, trust_root):
    """
    Check that they own the given identity URL, and that the trust_root is
    in their whitelist of trusted sites.
    """
    if not request.user.is_authenticated():
        return None

    openid = openid_get_identity(request, identity_url)
    if openid is None:
        return None

    if openid.trustedroot_set.filter(trust_root=trust_root).count() < 1:
        return None

    return openid

def openid_get_identity(request, identity_url):
    """
    Select openid based on claim (identity_url).
    If none was claimed identity_url will be 'http://specs.openid.net/auth/2.0/identifier_select'
    - in that case return default one
    - if user has no default one, return any
    - in other case return None!
    """
    for openid in request.user.openid_set.iterator():
        if identity_url == request.build_absolute_uri(
                reverse('openid-provider-identity', args=[openid.openid])):
            return openid
    if identity_url == 'http://specs.openid.net/auth/2.0/identifier_select':
        # no claim was made, choose user default openid:
        openids = request.user.openid_set.filter(default=True)
        if openids.count() == 1:
            return openids[0]
        if request.user.openid_set.count() > 0:
            return request.user.openid_set.all()[0]
    return None

def import_module_attr(path):
    package, module = path.rsplit('.', 1)
    return getattr(import_module(package), module)

def get_default_sreg_data(request, orequest):
    return {
        'email': request.user.email,
        'nickname': request.user.username,
        'fullname': request.user.get_full_name(),
    }

def get_default_ax_data(request, orequest):
    res = {
        'http://axschema.org/contact/email': request.user.email,
        'http://axschema.org/namePerson': request.user.get_full_name(),
        'http://axschema.org/namePerson/friendly': request.user.username,
        'http://axschema.org/namePerson/first': request.user.first_name,
        'http://axschema.org/namePerson/last': request.user.last_name,
    }

    openid = openid_is_authorized(request, orequest.identity,
                                  orequest.trust_root)
    for axdata in openid.axdatas.all():
        res[axdata.key] = axdata.value

    return res

def add_sreg_data(request, orequest, oresponse):
    callback = get_sreg_callback()
    if callback is None or not callable(callback):
        return
    sreg_data = callback(request, orequest)
    sreg_req = sreg.SRegRequest.fromOpenIDRequest(orequest)
    sreg_resp = sreg.SRegResponse.extractResponse(sreg_req, sreg_data)
    oresponse.addExtension(sreg_resp)

def add_ax_data(request, orequest, oresponse):
    callback = get_ax_callback()
    if callback is None or not callable(callback):
        return
    ax_data = callback(request, orequest)
    ax_req = ax.FetchRequest.fromOpenIDRequest(orequest)
    ax_resp = ax.FetchResponse(ax_req)
    if ax_req is not None:
        for attr in ax_req.getRequiredAttrs():
            value = ax_data.get(attr, None)
            if value is not None:
                ax_resp.addValue(attr, value)
    oresponse.addExtension(ax_resp)

def get_sreg_callback():
    try:
        return import_module_attr(conf.SREG_DATA_CALLBACK)
    except (ImportError, AttributeError):
        return None

def get_ax_callback():
    try:
        return import_module_attr(conf.AX_DATA_CALLBACK)
    except (ImportError, AttributeError):
        return None

def get_store(request):
    try:
        store_class = import_module_attr(conf.STORE)
    except ImportError:
        raise ImproperlyConfigured("OpenID store %r could not be imported" % conf.STORE)
    # The FileOpenIDStore requires a path to save the user files.
    if conf.STORE == 'openid.store.filestore.FileOpenIDStore':
        return store_class(conf.FILESTORE_PATH)
    return store_class()
