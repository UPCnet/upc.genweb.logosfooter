from five import grok
from zope.interface import Interface
from zope.component.hooks import getSite

from Products.CMFCore.utils import getToolByName

from plone.app.layout.viewlets.interfaces import IPortalFooter

from upc.genweb.logosfooter.interfaces import IGWFooterLogosInstalled

from upc.genweb.logosfooter import logosfooterMessageFactory as _

grok.context(Interface)


class logosFooterViewlet(grok.Viewlet):
    grok.name('genweb.logosfooter')
    grok.template('logosfooter')
    grok.viewletmanager(IPortalFooter)
    grok.layer(IGWFooterLogosInstalled)

    def portal_url(self):
        return self.portal().absolute_url()

    def portal(self):
        return getSite()

    def getLogosFooter(self):
        catalog = getToolByName(self.portal(), 'portal_catalog')

        return catalog.searchResults(portal_type='Logos_Footer',
                                     review_state=['published', 'intranet'],
                                     sort_on='getObjPositionInParent',
                                     sort_limit=5)[:5]

    def getAltAndTitle(self, altortitle):
        """ Funcio que extreu idioma actiu i afegeix al alt i al title de les imatges del banner
            el literal Obriu l'enllac en una finestra nova.
        """
        return '%s, %s' % (altortitle.decode('utf-8'),
            self.portal().translate(_('obrir_link_finestra_nova', default=u"(obriu en una finestra nova)")))
