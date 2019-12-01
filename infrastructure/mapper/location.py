from domain.location import Location as LocationDomain
from infrastructure import db


class Location(db.Model, LocationDomain):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255), nullable=True)
    state = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
