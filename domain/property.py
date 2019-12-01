class Property:
    def __init__(self, tower_name, building_type, rooms, garages, useful_area, minimum_estimate, maximum_estimate):
        self.tower_name = tower_name
        self.building_type = building_type
        self.rooms = rooms
        self.garages = garages
        self.useful_area = useful_area
        self.minimum_estimate = minimum_estimate
        self.maximum_estimate = maximum_estimate
        self.location = None

    @property
    def point_estimate(self):
        return (self.maximum_estimate + self.minimum_estimate) / 2
