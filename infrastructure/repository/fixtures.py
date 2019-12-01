from infrastructure import db
from domain.property import Property as PropertyDomain
from domain.location import Location as LocationDomain

import csv


def insert(item):
    tower_name = item.tower_name.replace("'", "")
    address = item.location.address.replace("'", "")
    latitude = 0 if item.location.latitude == 'None' else item.location.latitude
    longitude = 0 if item.location.longitude == 'None' else item.location.longitude

    db.engine.execute(
        f"insert into property (tower_name, building_type, rooms, garages, useful_area, maximum_estimate, minimum_estimate) values ('{tower_name}', '{item.building_type}', '{item.rooms}', '{item.garages}', '{item.useful_area}', '{item.maximum_estimate}', '{item.minimum_estimate}'); insert into location(city, state, address, latitude, longitude, property_id) values('{item.location.city}', '{item.location.state}', '{address}', {latitude}, {longitude}, nextval('property_id_seq') - 1);")


def bootstrap():
    with open('infrastructure/fixtures.csv') as file:
        reader = csv.DictReader(file)
        for line in reader:
            line.pop('point_estimate')
            location_data = {
                'city': line.pop('city'),
                'state': line.pop('state'),
                'address': line.pop('address'),
                'latitude': line.pop('latitude'),
                'longitude': line.pop('longitude'),
            }
            p = PropertyDomain(**line)
            location = LocationDomain(**location_data)
            p.location = location
            insert(p)
