from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from upc.genweb.logosfooter import logosfooterMessageFactory as _

# -*- extra stuff goes here -*-

class ILogos_Container(Interface):
    """A Logos Container
    """

class ILogos_Footer(Interface):
    """A Logos Container
    """
