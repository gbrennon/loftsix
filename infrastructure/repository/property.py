from infrastructure.mapper.property import Property


def get_by(rooms, value, garages, area):
    return Property.query.filter(Property.rooms == rooms).limit(3).all()


def find(id):
    return Property.query.get(id)
