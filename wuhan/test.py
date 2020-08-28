#pandas for csv reading


import requests
import io
import pandas as pd

'''
response = requests.get('http://www.chp.gov.hk/files/misc/building_list_eng.csv')

file_object = io.StringIO(response.content.decode('utf-8'))
download_temp = pd.read_csv(file_object)
download_temp.to_csv('building_list_eng.csv')
'''
# Read data from file
data=pd.read_csv("building_list_eng.csv")
'''
# Preview the first 5 lines of the loaded data 
print(data.head())
'''

# Changing columns name for easier operation
data.columns = ['ID','District','Building','Date','case_no']
#print(data.head())

# As source data doesn't have indication for building' corrisponding region/country,
# adding suffix for easier geo location search
data['Building'] = data['Building'].astype(str) + ', Hong Kong'
#print(data.head())
# Set column ID as Index
data = data.set_index('ID')

#import time
#time.sleep(5)
#printing whole csv data
print(data)

import geopandas as gpd
import geopy
from geopy import geocoders
from geopy.geocoders import GoogleV3
from geopy.extra.rate_limiter import RateLimiter

# Using address in Building column to search for geotag

# 1 - Function to delay between geocoding calls
g = geocoders.GoogleV3(api_key="AIzaSyD_lKWZVzvA7u9jJ7epVSnni13rr8FNisM")
geocode = RateLimiter(g.geocode, min_delay_seconds=5)
# 2- - Using address in Building column to search for geotag and append in column
data['Building'] = data['Building'].apply(geocode)
# 3 - Create GeoTag column which contain longitude, laatitude and altitude from Building column geotag result search 
data['GeoTag'] = data['Building'].apply(lambda loc: tuple(loc.point) if loc else None)
# 4 - Split GeoTag column into latitude, longitude and altitude columns
data[['latitude', 'longitude', 'altitude']] = pd.DataFrame(data['GeoTag'].tolist(), index=data.index)

#print(data)

# Plotting map by folium
import folium

map1 = folium.Map(
    location=[22.28552, 114.15769],
    tiles='CartoDB dark_matter',
    zoom_start=11,
)
data.apply(lambda row:folium.CircleMarker(location=[row["latitude"], row["longitude"]],color='red').add_to(map1), axis=1)
map1


# Save a map in html as well
map1.save("map1.html")


# Plotting map by folium plugin FastMarkerCluster to make data clustering visualization
from folium.plugins import FastMarkerCluster

map2 = folium.Map(location=[22.28552, 114.15769],
                        zoom_start=12,
                        tiles='CartoDB dark_matter')


FastMarkerCluster(data=list(zip(data['latitude'].values, data['longitude'].values))).add_to(map2)
folium.LayerControl().add_to(map2)
map2

# Save a map in html as well
map2.save("map2.html")

# Using Geocoder "Nominatim OpenStreetMap"
locator = Nominatim(user_agent="GeoTag")
location = locator.geocode("Tower 1A, Oceanaire, Hong Kong")
#or do the geocode
#location = g.geocode(inputAddress=above address, timeout=10)


print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

from geopy import geocoders


