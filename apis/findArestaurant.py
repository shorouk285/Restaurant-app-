#!/usr/bin/python3
from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "TSJYJL4NYJPNKRRXTPF40DBOP34D5WJLBTXSUYEQOIDZCHDJ"
foursquare_client_secret = "BYES1GT04AIEYRTDHXK1KLFBZ5KGTLI4WKB2Z4IN5KVAXZCK"


def findARestaurant(mealType, location):
    # 1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    latitude, longitude = getGeocodeLocation(location)
    # 2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    # HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    url = ("https://api.foursquare.com/v2/venues/search?client_id=%s \
          &client_secret=%s&v=20130815&ll=%s,%s&query=%s"
           % (foursquare_client_id, foursquare_client_secret,
              latitude, longitude, mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # 3. Grab the first restaurant
    if result['response']['venues']:
        restaurant = result['response']['venues'][0]
        venue_id = restaurant['id']
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['formattedAddress']
        address = ""
        for i in restaurant_address:
            address += i + " "
        restaurant_address = address
        # 4.  Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
        url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s \
                &v=20150603&client_secret=%s'
               % ((venue_id, foursquare_client_id, foursquare_client_secret)))
        result = json.loads(h.request(url, 'GET')[1])
        # 5.  Grab the first image
        if result['response']['photos']['items']:
            firstpic = result['response']['photos']['items'][0]
            prefix = firstpic['prefix']
            suffix = firstpic['suffix']
            imageURL = prefix + "300x300" + suffix
        # 6. If no image is available, insert default a image url
        else:
            imageURL = ("https://drive.google.com/file/d/1vcdiUfGioiJHYFzspCO4f5NmXZl0pj30/view?usp=sharing")
        # 7. Return a dictionary containing the restaurant name, address, and image url
            restaurantInfo = {'name': restaurant_name, 'address': restaurant_address, 'image': imageURL}
        print ("Restaurant Name: " + restaurantInfo['name'])
        print ("Restaurant Address: " + restaurantInfo['address'])
        print ("Image: %s \n" % restaurantInfo['image'])
        return restaurantInfo
    else:
        print "No Restaurants Found for %s" % location
        return "No Restaurants Found"


if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney, Australia")
