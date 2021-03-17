# mobile phone towers 

# aggiunge tag source=RAFVG
add_source = True
source = 'RAFVG'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del RAFVG>
# True -> relying only on geometric matching every time
no_dataset_id = True
# sito opendata della regione fvg                           
dataset_id = 'rafvg'

# Overpass query to use when searching OSM for data
#overpass_timeout = 120 default
overpass_timeout = 300
query = [('man_made', 'mast')],[('man_made', 'tower')]

# parameter --osm will use indipendently generated queries, ie:
# http://overpass-turbo.eu/s/156t
# use wget -O manual-query.osm <http_addr obtained exporting compact query>

bbox = True


# tags to replace on matched OSM objects
master_tags = ('operator')

delete_unmatched = False
#tag_unmatched = { 'note':'this mobile phone tower is not in RAFVG dataset' }


# max distance to search for a match in meters
max_distance = 50

duplicate_distance = 5
