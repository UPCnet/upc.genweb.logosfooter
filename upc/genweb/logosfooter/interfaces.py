from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from upc.genweb.logosfooter import logosfooterMessageFactory as _

# -*- extra stuff goes here -*-

class ILogoscontainer(Interface):
    """A Logos Container
    """

class ILogosfooter(Interface):
    """A Logos Container
    """