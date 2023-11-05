# from geopy.distance import great_circle
# from geopy.geocoders import Nominatim
# import geocoder
# import webbrowser






# def GMAP(place):
#     url_place = "https://www.google.com/maps/place/" + str(place)

#     geolocator = Nominatim(user_agent="mygeocoder")
#     location = geolocator.geocode(place, addressdetails= True)
#     target_lat_lon = location.latitude, location.longitude
#     location = location.raw['address']

#     target = {'city' : location.get('city', ''),
#               'state' : location.get('state', ''),
#               'country' : location.get('country', '')}
    
#     current_loc = geocoder.ip('me')

#     current_lat_lon = current_loc.latlng
#     dist = str(great_circle(current_lat_lon, target_lat_lon))
#     dist = str(dist.split(' ', 1)[0])
#     dist = round(float(dist), 2)
#     print(target)

#     webbrowser.open(url=url_place)

#     GMAP()
    

   

 




    


  

import geocoder
g = geocoder.ip("me")
print(g.latlng)