#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name' : 'Google Translate',
    'name_de_DE' : 'Google Übersetzung',
    'version' : '1.1.0',
    'author' : 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': 'Translate untranslated items with google translate',
    'description_de_DE': 'Unübersetzte Elemente per Google Übersetzung ausfüllen',
    'depends' : [
        'ir',
    ],
    'xml' : [
        'ir.xml',
    ],
    'translation': [
        'de_DE.csv',
    ],
}
