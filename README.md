# TelefoniaMobile
Find herein data related to Openstreetmap import of cell towers in Friuli Venezia Giulia (Italy)
https://wiki.openstreetmap.org/wiki/Import/Catalogue/TorriTelefonia-RAFVG


from dataset, create and export provincia subset, ie: prodenone.json
from OSM query overpass (see profile.py), download provincia data (metadata included), ie: pordenone.osm

generate audit map for http://audit.osmz.ru, ie: preview_pordenone.json and upload it
conflate -i pordenone.json   -v -c preview_pordenone.json --osm pordenone.osm  profile.py

after public audit, download audit file from http://audit.osmz.ru and re-conflate with mappers integrations:
conflate -i pordenone.json -a audit_FVG-PN-towers.json --osm  pordenone.osm -o pn-ready.osm profile.py 
