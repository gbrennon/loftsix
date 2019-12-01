from domain.property import Property as PropertyDomain
from infrastructure import db


class Property(db.Model, PropertyDomain):
    id = db.Column(db.Integer, primary_key=True)
    tower_name = db.Column(db.String(255), nullable=True)
    building_type = db.Column(db.String(255), nullable=True)
    rooms = db.Column(db.Integer, nullable=True)
    garages = db.Column(db.Integer, nullable=True)
    useful_area = db.Column(db.Integer, nullable=True)
    minimum_estimate = db.Column(db.Float, nullable=True)
    maximum_estimate = db.Column(db.Float, nullable=True)
    location = db.relationship('Location')
