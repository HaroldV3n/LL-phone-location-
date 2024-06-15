import phonenumbers 
import opencage
from LLphone import number

from phonenumbers 
import geocoder

pepnumbers=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en')
print(location)                                

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opemcage.geocoder import OpenCageGeocode

key="e0facf38a5b24c2cb1ea264b0612aed1"

geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat_lng)

myMap=folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")

