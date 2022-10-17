from models import location


class Animal():

    def __init__(self, id, name, breed, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.status = breed
        self.breed = status
        self.location_id = location_id
        self.customer_id = customer_id
        self.location = None
        self.customer = None