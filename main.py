# Simple Python Script to extract coordinates from a KML file. This can be used to use for OpenStreetMap or other JS mapping libraries.

import xml.etree.ElementTree as ET

filename = "file.kml"

tree = ET.parse(filename)
root = tree.getroot()

ns = {'kml': 'http://www.opengis.net/kml/2.2'}

placemarks = root.findall('.//kml:Placemark', ns)
coords = []

for pm in placemarks:
    name = pm.find('.//kml:name', ns).text.strip()
    coord = pm.find('.//kml:coordinates', ns).text.strip()
    coord_values = coord.split(',')
    if len(coord_values) >= 2:
        lat, lon = float(coord_values[1]), float(coord_values[0])
        coords.append([name, lat, lon])

# replace single quotes with double quotes
coords_str = str(coords).replace("'", '"')

# print on new lines
print(coords_str.replace('], [', '],\n['))
