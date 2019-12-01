from domain.property import Property as PropertyDomain
from infrastructure import db

class Property(db.Model, PropertyDomain):
    id = db.Column(db.Integer, primary_key=True)
    tower_name = db.Column(db.String(255), nullable=False)
    building_type = db.Column(db.String(255), nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    garages = db.Column(db.Integer, nullable=False)
    useful_area = db.Column(db.Integer, nullable=False)
    minimum_estimate = db.Column(db.Float, nullable=False)
    maximum_estimate = db.Column(db.Float, nullable=False)
    location = db.relationship('Location')
