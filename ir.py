#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView
from trytond.wizard import Wizard
from trytond.version import PACKAGE, VERSION
from urllib import urlopen, urlencode, unquote
from urllib2 import build_opener
from BeautifulSoup import BeautifulSoup
GOOGLE_URL = 'http://translate.google.com/translate_t?'


class GoogleTranslateInit(ModelView):
    'Translate with Google Init'
    _name = 'ir.translation.google_translate.init'
    _description = __doc__

GoogleTranslateInit()


class GoogleTranslateStart(ModelView):
    'Translate with Google Start'
    _name = 'ir.translation.google_translate.start'
    _description = __doc__

GoogleTranslateStart()


class GoogleTranslate(Wizard):
    'Translate with Google'
    _name = 'ir.translation.google_translate'

    states = {
        'init': {
            'result': {
                'type': 'form',
                'object': 'ir.translation.google_translate.init',
                'state': [
                    ('end', 'Cancel', 'tryton-cancel'),
                    ('start', 'Start translate', 'tryton-ok', True),
                ],
            },
        },
        'start': {
            'actions': ['_translate'],
            'result': {
                'type': 'form',
                'object': 'ir.translation.google_translate.start',
                'state': [
                    ('end', 'Ok', 'tryton-ok', True),
                ],
            },
        },
    }

    def _translate(self, cursor, user, data, context=None):
        translation_obj = self.pool.get('ir.translation')
        opener = build_opener()
        opener.addheaders = [('User-agent', '%s/%s' % (PACKAGE, VERSION))]

        for translation in translation_obj.browse(cursor, user, data['ids'],
                context=context):
            lang = translation.lang[:2].lower().encode('utf-8')
            src = translation.src.encode('utf-8')
            value = BeautifulSoup(opener.open(GOOGLE_URL + urlencode({
                'sl': 'en',
                'tl': lang,
                }), data=urlencode({
                    'hl': 'en',
                    'ie': 'UTF-8',
                    'text': src,
                    'sl': 'en',
                    'tl': lang,
                    })),
                convertEntities=BeautifulSoup.HTML_ENTITIES).find('div',
                        attrs={'id': 'result_box'})
            if not value:
                continue
            if not value.string:
                continue
            value = str(value.string)
            translation_obj.write(cursor, user, translation.id, {
                'value': value,
                'fuzzy': True,
                }, context=context)
        return {}

GoogleTranslate()
