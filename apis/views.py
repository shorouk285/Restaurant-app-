#!/usr/bin/python3
from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)




foursquare_client_id = "TSJYJL4NYJPNKRRXTPF40DBOP34D5WJLBTXSUYEQOIDZCHDJ"
foursquare_client_secret = "BYES1GT04AIEYRTDHXK1KLFBZ5KGTLI4WKB2Z4IN5KVAXZCK"
google_api_key = "AIzaSyCluVT5yELlVqmZEdOrBRub3CkKzFfVobw"

engine = create_engine('sqlite:///restaurants.db', connect_args = ({'check_same_thread': False}))

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
    if request.method == 'GET':
        restaurants = session.query(Restaurant).all()
        return jsonify(restaurants = [r.serialize for r in restaurants])
    elif request.method == 'POST':
        location = request.args.get('location', '')
        mealType = request.args.get('mealType', '')
        restaurant_info= findARestaurant(mealType, location)
        if restaurant_info != "No Restaurants Found":
            restaurant = Restaurant(restaurant_name=unicode(restaurant_info['name']),
                         restaurant_address=unicode(restaurant_info['address']),
                         restaurant_image=unicode(restaurant_info['image']))
            session.add(restaurant)
            session.commit()
            return jsonify(restaurant=restaurant.serialize)
        else:
            return jsonify({"error": "No restaurant in %s for %s" % (location, mealType)})

@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
    restaurant = session.query(Restaurant).filter_by(id = id).one()
    if request.method == 'GET':
        return jsonify(restaurant = restaurant.serialize)
    elif request.method == 'PUT':
        name = request.args.get('name', '')
        address = request.args.get('address', '')
        image = request.args.get('image', '')
        if address:
  		    restaurant.restaurant_address = address
  	    if image:
  		    restaurant.restaurant_image = image
  	    if name:
  		    restaurant.restaurant_name = name
        session.commit()
        return jsonify(restaurant = restaurant.serialize)
    elif request.method == 'DELETE':
        session.delete(restaurant)
        session.commit()
        return "Restaurant deleted"    


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
