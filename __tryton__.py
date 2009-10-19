#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name' : 'Google Translate',
    'name_de_DE' : 'Google Übersetzung',
    'name_es_CO': 'Traducción de Google',
    'name_es_ES': 'Google Traductor',
    'name_fr_FR': 'Google Translate',
    'version' : '1.5.0',
    'author' : 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': 'Translate items with Google Translate',
    'description_de_DE': 'Unübersetzte Elemente per Google Übersetzung ausfüllen',
    'description_es_CO': 'Traducir términos vía Traducción de Google',
    'description_es_ES': 'Traduce términos con Google Traductor',
    'description_fr_FR': 'Traduit les termes avec Google Translate',
    'depends' : [
        'ir',
    ],
    'xml' : [
        'ir.xml',
    ],
    'translation': [
        'de_DE.csv',
        'es_CO.csv',
        'es_ES.csv',
        'fr_FR.csv',
    ],
}
