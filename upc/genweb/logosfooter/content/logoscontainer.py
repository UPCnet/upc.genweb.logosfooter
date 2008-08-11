"""Definition of the logos Container content type.
"""
__author__ = """José Luis Vivanco C <jose.luis.vivanco@upcnet.es>"""
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.component import adapts

from Products.CMFCore.utils import getToolByName, _checkPermission
from Products.Archetypes.interfaces import IObjectPostValidation

from Products.Archetypes.atapi import *
from AccessControl import ClassSecurityInfo

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATContentTypes.content.folder import ATFolder

from upc.genweb.logosfooter.interfaces import ILogoscontainer
from upc.genweb.logosfooter.config import PROJECTNAME

schema = Schema((

),
)

LogosContainer_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()


class Logoscontainer(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(ILogoscontainer)

    meta_type = 'Logos Container'
    _at_rename_after_creation = True

    schema = LogosContainer_schema

registerType(Logoscontainer, PROJECTNAME)