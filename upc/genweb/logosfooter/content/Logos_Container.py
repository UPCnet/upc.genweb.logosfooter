# -*- coding: utf-8 -*-
"""Definition of the logos Container content type.
"""
__author__ = """José Luis Vivanco C <jose.luis.vivanco@upcnet.es>"""
__docformat__ = 'plaintext'

from zope.interface import implements

from Products.Archetypes.atapi import *
from AccessControl import ClassSecurityInfo

from Products.ATContentTypes.content.folder import ATFolder

from upc.genweb.logosfooter.interfaces import ILogos_Container
from upc.genweb.logosfooter.config import PROJECTNAME

schema = Schema((

),
)

LogosContainer_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()


class Logos_Container(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(ILogos_Container)

    meta_type = 'Logos_Container'
    _at_rename_after_creation = True

    schema = LogosContainer_schema

registerType(Logos_Container, PROJECTNAME)
