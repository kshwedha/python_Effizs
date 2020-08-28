# import folium package 
import folium 

# Map method of folium return Map object 

# Here we pass coordinates of Gfg 
# and starting Zoom level = 12 
my_map1 = folium.Map(location = [28.5011226, 77.4099794], 

folium.CircleMarker(location = [28.5011226, 77.4099794], radius = 50, popup = ' FRI ').add_to(my_map1)

# Pass a string in popup parameter 
folium.Marker([28.5011226, 77.4099794], popup = ' Geeksforgeeks.org ').add_to(my_map1)  										zoom_start = 12 ) 

# save method of Map object will create a map 
my_map1.create_map(" my_map1.html " ) 
#for py2
#my_map1.save("filename.html")
