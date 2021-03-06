# -*- coding: utf-8 -*-


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('upc.genweb.footer_various.txt') is None:
        return

#    la creació de continguts s'ha centralitzat al paquet upc.genwebupc, per fer-la language-aware
#
#    from Products.CMFPlone.utils import _createObjectByType, getToolByName
#    portal = context.getSite()
#
#    workflowTool = getToolByName(portal, "portal_workflow")
#
#    if not getattr(portal,'logospeu',False):
#        _createObjectByType('Logos_Container', portal, 'logospeu')
#        portal['logospeu'].setExcludeFromNav(True)
#        portal['logospeu'].setTitle('Logos peu')
#        portal['logospeu'].reindexObject()
#        workflowTool.doActionFor(portal.logospeu, "publish")
