#from infrastructure.repository.property import bulk_insert
from domain.property import Property
from domain.location import Location

import csv


def bulk_insert(db, properties):
    return db.engine.execute(Property.__table__.insert(), properties)


def bootstrap(db):
    with open('infrastructure/fixtures.csv') as file:
        properties = []
        reader = csv.DictReader(file)
        for line in reader:
            #property.location = location
            # property.save()
            line.pop('point_estimate')
            location_data = {
                'city': line.pop('city'),
                'state': line.pop('state'),
                'address': line.pop('address'),
                'latitude': line.pop('latitude'),
                'longitude': line.pop('longitude'),
            }
            property = Property(**line)
            location = Location(**location_data)
            property.location = location

            properties.append(property)
        bulk_insert(db, properties)
