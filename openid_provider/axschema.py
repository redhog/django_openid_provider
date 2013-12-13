# This data is from http://openid.net/specs/openid-attribute-properties-list-1_0-01.html

axschema = {
    'http://axschema.org/namePerson': {
        'title': 'Full name',
        'description': 'Full name of subject',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/namePerson/prefix': {
        'title': 'Name prefix',
        'description': 'Honorific prefix for the subject\'s name; i.e. "Mr.", "Mrs.", "Dr."',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/namePerson/first': {
        'title': 'First name',
        'description': 'First or given name of subject',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/namePerson/last': {
        'title': 'Last name',
        'description': 'Last name or surname of subject',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/namePerson/middle': {
        'title': 'Middle name',
        'description': 'Middle name(s) of subject',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/namePerson/suffix': {
        'title': 'Name suffix',
        'description': 'Suffix of subject\'s name',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/namePerson/friendly': {
        'title': 'Alias',
        'description': 'Subject\'s alias or "screen" name',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/person/guid': {
        'title': 'GUID',
        'description': 'Subject\'s globally unique identifier',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/birthDate/birthYear': {
        'title': 'Birth year',
        'description': 'Year of birth (four digits)',
        'type': 'http://www.w3.org/2001/XMLSchema#gYear'},
    'http://openid.net/schema/birthDate/birthMonth': {
        'title': 'Birth month',
        'description': 'Month of birth (1-12)',
        'type': 'http://www.w3.org/2001/XMLSchema#gMonth'},
    'http://openid.net/schema/birthDate/birthday': {
        'title': 'Birth day',
        'description': 'Day of birth',
        'type': 'http://www.w3.org/2001/XMLSchema#gDay'},
    'http://openid.net/schema/gender': {
        'title': 'Gender',
        'description': 'Gender, either "M" or "F"',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/language/pref': {
        'title': 'Language',
        'description': 'Preferred language, as per [RFC4646]',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/phone/default': {
        'title': 'Phone (preferred)',
        'description': 'Main phone number (preferred)',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/phone/home': {
        'title': 'Phone (home)',
        'description': 'Home phone number',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/phone/business': {
        'title': 'Phone (work)',
        'description': 'Business phone number',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/phone/cell': {
        'title': 'Phone (mobile)',
        'description': 'Cellular (or mobile) phone number',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/phone/fax': {
        'title': 'Phone (fax)',
        'description': 'Fax number',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/postaladdress/home': {
        'title': 'Address',
        'description': 'Home postal address: street number, name and apartment number',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/postaladdressadditional/home': {
        'title': 'Address 2',
        'description': 'Home postal address: supplementary information',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/city/home': {
        'title': 'City',
        'description': 'Home city name',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/state/home': {
        'title': 'State/Province',
        'description': 'Home state or province name',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/country/home': {
        'title': 'Country',
        'description': 'Home country code in [ISO.3166.1988] (alpha 2) format',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/postalcode/home': {
        'title': 'Postal code',
        'description': 'Home postal code; region specific format',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/postaladdress/business': {
        'title': 'Address',
        'description': 'Business postal address: street number, name and apartment number',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/postaladdressadditional/business': {
        'title': 'Address 2',
        'description': 'Business postal address: supplementary information',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/city/business': {
        'title': 'City',
        'description': 'Business city name',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/state/business': {
        'title': 'State/Province',
        'description': 'Business state or province name',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/country/business': {
        'title': 'Country',
        'description': 'Business country code in [ISO.3166.1988] (alpha 2) format',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/postalcode/business': {
        'title': 'Business postal or zip code; region specific format',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/IM/default': {
        'title': 'IM',
        'description': 'Preferred instant messaging service (one of ',
        'type': 'http://openid.net/schema/contact/IM/*)',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/contact/IM/AIM': {
        'title': 'AOL IM',
        'description': 'AOL instant messaging service handle',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/IM/ICQ': {
        'title': 'ICQ IM',
        'description': 'ICQ instant messaging service handle',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/IM/MSN': {
        'title': 'MSN IM',
        'description': 'MSN instant messaging service handle',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/IM/Yahoo': {
        'title': 'Yahoo! IM',
        'description': 'Yahoo! instant messaging service handle',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/IM/Jabber': {
        'title': 'Jabber IM',
        'description': 'Jabber instant messaging service handle',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/IM/Skype': {
        'title': 'Skype IM',
        'description': 'Skype instant messaging service handle',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://axschema.org/contact/email': {
        'title': 'Email',
        'description': 'Internet SMTP email address',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/internet/email': {
        'title': 'Email',
        'description': 'Internet SMTP email address',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/contact/web/default': {
        'title': 'Web page',
        'description': 'Web site URL',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/contact/web/blog': {
        'title': 'Blog',
        'description': 'Blog URL',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/contact/web/Linkedin': {
        'title': 'LinkedIn URL',
        'description': 'LinkedIn URL',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/contact/web/Amazon': {
        'title': 'Amazon URL',
        'description': 'Amazon URL',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/contact/web/Flickr': {
        'title': 'Flickr URL',
        'description': 'Flickr URL',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/contact/web/Delicious': {
        'title': 'del.icio.us URL',
        'description': 'del.icio.us URL',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/company/name': {
        'title': 'Company',
        'description': 'Company name (employer)',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/company/title': {
        'title': 'Title',
        'description': 'Employee title',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'},
    'http://openid.net/schema/media/spokenname': {
        'title': 'Spoken name',
        'description': 'Spoken name (web URL)',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/greeting/audio': {
        'title': 'Audio greeting',
        'description': 'Audio greeting (web URL)',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/greeting/video': {
        'title': 'Video greeting',
        'description': 'Video greeting (web URL)',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/biography': {
        'title': 'Biography',
        'description': 'Biography (text)',
        'type': 'http://www.w3.org/2001/XMLSchema#string'},
    'http://openid.net/schema/media/image': {
        'title': 'Image',
        'description': 'Image (web URL); unspecified dimension',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/16x16': {
        'title': '16x16 image',
        'description': 'Image (web URL); 16x16 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/32x32': {
        'title': '32x32 image',
        'description': 'Image (web URL); 32x32 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/48x48': {
        'title': '48x48 image',
        'description': 'Image (web URL); 48x48 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/64x64': {
        'title': '64x64 image',
        'description': 'Image (web URL); 64x64 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/80x80': {
        'title': '80x80 image',
        'description': 'Image (web URL); 80x80 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/128x128': {
        'title': '128x128 image',
        'description': 'Image (web URL); 128x128 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/160x120': {
        'title': '160x120 image',
        'description': 'Image (web URL) 4:3 ratio - landscape; 160x120 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/320x240': {
        'title': '320x240 image',
        'description': 'Image (web URL) 4:3 ratio - landscape; 320x240 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/640x480': {
        'title': '640x480 image',
        'description': 'Image (web URL) 4:3 ratio - landscape; 640x480 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/120x160': {
        'title': '120x160 image',
        'description': 'Image (web URL) 4:3 ratio - portrait; 120x160 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/240x320': {
        'title': '240x320 image',
        'description': 'Image (web URL) 4:3 ratio - portrait; 240x320 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/480x640': {
        'title': '480x640 image',
        'description': 'Image (web URL) 4:3 ratio - portrait; 480x640 pixels',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/media/image/favicon': {
        'title': 'Favicon image',
        'description': 'Image (web URL); favicon format',
        'type': 'http://www.w3.org/2001/XMLSchema#anyURI'},
    'http://openid.net/schema/timezone': {
        'title': 'Time zone',
        'description': 'Home time zone information (as specified in [zoneinfo])',
        'type': 'http://www.w3.org/2001/XMLSchema#normalizedString'}}

for key in axschema.keys():
    axschema[key.replace('http://openid.net/schema/', 'http://axschema.org/')] = axschema[key]
