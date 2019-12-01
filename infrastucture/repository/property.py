from infrastucture.mapper.property import Property


def get_all():
    return Property.query.all()
