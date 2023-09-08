# -*- coding: utf-8 -*-

'''
Translation examples:
https://github.com/roelderickx/ogr2osm-translations

A translation function for IGMI 020102: Edificio (edifc) data. 
https://www.igmi.org/dbsn_supporto/dbsn/#F020102

01	generica	
02	palazzo a torre, grattacielo	
03	edificio tipico	
0301	nuraghe	
0302	damuso	
0303	tabià	
0304	masseria	
0305	trullo	
04	villa	
05	villetta a schiera	
06	battistero	
07	campanile	
08	capannone	
09	edificio rurale	
10	castello	
11	chiesa	
12	anfiteatro	
13	faro	
14	hangar	
15	minareto, moschea	
16	tempio	
17	mulino	
18	osservatorio	
19	palazzetto dello sport	
20	sinagoga	
21	stadio	
22	cattedrale	
23	tettoia	
24	bastione	
25	mura di cinta	
93	non definito	
95	altro
'''

import ogr2osm
import re

class DbsnEdifcTranslation(ogr2osm.TranslationBase):    
    def filter_tags(self, attrs):
        if not attrs:
            return
        tags = {}

# TIPO EDIFICIO
        if 'edifc_ty' in attrs:
           if re.match('^0[1-3]', attrs['edifc_ty']):
                tags['building'] = 'yes'
           if re.match('^0[45]', attrs['edifc_ty']):
                tags['building'] = 'yes'
           if attrs['edifc_ty'] == "07":
                tags['building'] = 'bell_tower'
                tags['man_made'] = 'tower'
                tags['tower:type'] = 'bell_tower'
           if attrs['edifc_ty'] == "08":
                tags['building'] = 'industrial'
           if attrs['edifc_ty'] == "09":
                tags['building'] = 'farm'
           if attrs['edifc_ty'] == "10":
                tags['building'] = 'castle'
           if attrs['edifc_ty'] == "11":
                tags['building'] = 'church'
                tags['religion'] = 'christian'
           if attrs['edifc_ty'] == "15":
                tags['building'] = 'church'
                tags['religion'] = 'muslim'


           if re.match('^9[35]', attrs['edifc_ty']):
                tags['building'] = 'yes'

        else:
             tags['building'] = 'yes'

# STATO EDIFICIO
        if 'edifc_stat' in attrs:
           if attrs['edifc_stat'] == "01":
                tags['construction'] = 'yes'
           if attrs['edifc_stat'] == "02":
                tags['ruins'] = 'yes'

        if attrs["edifc_nome"] != "UNK":
             tags["name"] = attrs["edifc_nome"].title()

#       tags['source'] = 'IGMI DBSN -020102: Edificio (edifc)'
        tags['edifc_ty'] = attrs['edifc_ty']

        return tags
