from domain.location import Location as LocationDomain
from infrastructure import db


class Location(db.Model, LocationDomain):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
