"""Definition of the logos footer content type.
"""
__author__ = """José Luis Vivanco C <jose.luis.vivanco@upcnet.es>"""
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.component import adapts

from Products.CMFCore.utils import getToolByName, _checkPermission
from Products.Archetypes.interfaces import IObjectPostValidation

from Products.Archetypes.atapi import *
from AccessControl import ClassSecurityInfo

from upc.genweb.logosfooter.interfaces import ILogos_Footer
from upc.genweb.logosfooter.config import PROJECTNAME

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

schema = Schema((

    ImageField(
        name='Imatge',
        widget=ImageField._properties['widget'](
            label='Imatge',
            label_msgid='siteBanners_label_Imatge',
            i18n_domain='siteBanners',
        ),
        storage=AttributeStorage(),
    ),
    StringField(
        name='URLdesti',
        widget=StringField._properties['widget'](
            label='Urldesti',
            label_msgid='siteBanners_label_URLdesti',
            i18n_domain='siteBanners',
        ),
    ),
    BooleanField(
        name='Obrirennovafinestra',
        widget=BooleanField._properties['widget'](
            label='Obrirennovafinestra',
            label_msgid='siteBanners_label_Obrirennovafinestra',
            i18n_domain='siteBanners',
        ),
    ),
),
)

logos_schema = BaseSchema.copy() + \
    schema.copy()


class Logos_Footer(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(ILogos_Footer)

    meta_type = 'Logos_Footer'
    _at_rename_after_creation = True

    schema = logos_schema

registerType(Logos_Footer, PROJECTNAME)
