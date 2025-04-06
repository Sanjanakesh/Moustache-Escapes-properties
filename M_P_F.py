
from fastapi import FastAPI
from pydantic import BaseModel
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# List of all our cool Moustache properties with their exact locations!
places_we_have = [
    {"name": "Moustache Goa Luxuria", "lat": 15.6135195, "lon": 73.75705228},
    {"name": "Moustache Koksar Luxuria", "lat": 32.4357785, "lon": 77.18518717},
    {"name": "Moustache Daman", "lat": 20.41486263, "lon": 72.83282455},
    {"name": "Panarpani Retreat", "lat": 22.52805539, "lon": 78.43116291},
    {"name": "Moustache Pushkar", "lat": 26.48080513, "lon": 74.5613783},
    {"name": "Moustache Khajuraho", "lat": 24.84602104, "lon": 79.93139381},
    {"name": "Moustache Manali", "lat": 32.28818695, "lon": 77.17702523},
    {"name": "Moustache Bhimtal Luxuria", "lat": 29.36552248, "lon": 79.53481747},
    {"name": "Moustache Srinagar", "lat": 34.11547314, "lon": 74.88701741},
    {"name": "Moustache Ranthambore Luxuria", "lat": 26.05471373, "lon": 76.42953726},
    {"name": "Moustache Coimbatore", "lat": 11.02064612, "lon": 76.96293531},
    {"name": "Moustache Shoja", "lat": 31.56341267, "lon": 77.3673331},
    {"name": "Moustache Udaipur Luxuria", "lat": 24.57799888, "lon": 73.68263271},
    {"name": "Moustache Udaipur", "lat": 24.58145726, "lon": 73.68223671},
    {"name": "Moustache Udaipur Verandah", "lat": 24.58350565, "lon": 73.68120777},
    {"name": "Moustache Jaipur", "lat": 27.29124839, "lon": 75.89630143},
    {"name": "Moustache Jaisalmer", "lat": 27.20578572, "lon": 70.85906998},
    {"name": "Moustache Jodhpur", "lat": 26.30365556, "lon": 73.03570908},
    {"name": "Moustache Agra", "lat": 27.26156953, "lon": 78.07524716},
    {"name": "Moustache Delhi", "lat": 28.61257139, "lon": 77.28423582},
    {"name": "Moustache Rishikesh Luxuria", "lat": 30.13769036, "lon": 78.32465767},
    {"name": "Moustache Rishikesh Riverside Resort", "lat": 30.10216117, "lon": 78.38458848},
    {"name": "Moustache Hostel Varanasi", "lat": 25.2992622, "lon": 82.99691388},
]

# Turn whatever the user typed (even with small typos) into coordinates
def convert_place_to_coords(place_name):
    finder = Nominatim(user_agent="property_finder_app")
    found_place = finder.geocode(place_name)
    if found_place:
        return found_place.latitude, found_place.longitude
    return None, None

# Math check – are two places close enough (within 50km)?
def close_enough(user_coords, moustache_coords, max_distance_km=50):
    return geodesic(user_coords, moustache_coords).km <= max_distance_km

#Figure out which Moustache properties are near the user
def find_moustache_near_you(place_you_mentioned):
    your_lat, your_lon = convert_place_to_coords(place_you_mentioned)
    if not your_lat or not your_lon:
        return []

    where_you_are = (your_lat, your_lon)
    nearby_spots = []

    for each_property in places_we_have:
        where_property_is = (each_property['lat'], each_property['lon'])
        if close_enough(where_you_are, where_property_is):
            nearby_spots.append(each_property['name'])

    return nearby_spots

# Build the actual API now!
app = FastAPI()

# Just a tiny model to accept input properly
class LocationQuery(BaseModel):
    location: str

# This is the main route you'd hit with a location name
@app.post("/find-properties")
def get_places_based_on_user_location(input_data: LocationQuery):
    found_places = find_moustache_near_you(input_data.location)
    if not found_places:
        return {"message": "No Moustache stays found nearby. Try a different location?"}
    return {"places_near_you": found_places}
