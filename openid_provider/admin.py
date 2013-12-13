# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 : */

from django.contrib import admin

from openid_provider.models import TrustedRoot, OpenID, AxData

class TrustedRootInline(admin.TabularInline):
    model = TrustedRoot

class AxDataInline(admin.TabularInline):
    model = AxData

class OpenIDAdmin(admin.ModelAdmin):
    list_display = ['openid', 'user', 'default']
    inlines = [AxDataInline, TrustedRootInline]

admin.site.register(OpenID, OpenIDAdmin)
