# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:18:26 2015

@author: thomas.douenne
"""

import os
import pkg_resources
import urllib

from ipp_macro_series_parser.config import Config


parser = Config(
    config_files_directory = os.path.join(pkg_resources.get_distribution('ipp-macro-series-parser').location)
    )
transports_directory = parser.get('data', 'transports_directory')


def getunzipped(theurl, thedir, file_name):
    name = os.path.join(thedir, file_name)
    if not os.path.exists(thedir):
        os.makedirs(thedir)
    try:
        name, hdrs = urllib.urlretrieve(theurl, name)
    except IOError, e:
        print "Can't retrieve %r to %r: %s" % (theurl, thedir, e)
        return

to_be_downloaded = ['a-transport-activite-economique', 'b-entreprises',
                    'c-transport-emploi-remuneration', 'd-transport-developpement-durable',
                    'e-transport-marchandises', 'f-transports-voyageurs-b', 'g-bilan-circulation']


def transports_downloader():
    for element in to_be_downloaded:
        theurl = 'http://www.statistiques.developpement-durable.gouv.fr/fileadmin/documents/Produits_editoriaux/Publications/References/2015/comptes-transports-2014/2014-comptes-transports-{}.xls'.format(element)
        #theurl = 'http://www.statistiques.developpement-durable.gouv.fr/fileadmin/documents/Produits_editoriaux/Publications/References/2014/comptes-transports/annexes-{}-2013.xls'.format(element)
        thedir = os.path.join(transports_directory)
        getunzipped(theurl, thedir, element + '.xls')

transports_downloader()
