from asyncore import loop
from urllib import request


DATABASE = {
    "ANIMALS": [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "status": "Admitted",
        "customerId": 1
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "Status": "Admitted",
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "Status": "Admitted",
        "customerId": 1
    }
    ],
    "CUSTOMERS": [
    {
        "id": 1,
        "name": "Ryan Tanay"
    },
    {
        "id": 2,
        "name": "Eric Carle"
    }
    ],
    "EMPLOYEES": [
    {
        "id": 1,
        "name": "Jenna Solis",
        "locationId": 1
    }
    ],
    "LOCATIONS": [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]


}


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource.upper()]


def retrieve(resource, id):
    """For GET requests to a single resource"""
        # Variable to hold the found animal, if it exists
    requested_resource = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for item in DATABASE[resource.upper()]:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if item["id"] == id:
            requested_resource = item
    
    if requested_resource == None:
        return None


    if resource.upper() == "ANIMALS":

        location = retrieve("locations", requested_resource["locationId"])
        customer = retrieve("customers", requested_resource["customerId"])
        requested_resource["customer"] = customer
        requested_resource["location"] = location
        requested_resource.pop("customerId")
        requested_resource.pop("locationId")
        return requested_resource

    else:
        return requested_resource


required_elements = {
    "ANIMALS": ["name", "species", "locationId", "Status", "customerId"],
    "CUSTOMERS": ["name"],
    "EMPLOYEES": ["name"],
    "LOCATIONS": ["name", "address"]
}

def create(resource, item):
    """For POST requests to a collection"""

    for required_element in required_elements[resource.upper()]:
        if required_element not in item:
            return f"{required_element} is required"

    # Get the id value of the last animal in the list
    max_id = DATABASE["ANIMALS"][-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    item["id"] = new_id

    # Add the animal dictionary to the list
    DATABASE["ANIMALS"].append(item)

    # Return the dictionary with `id` property added
    return item



def update(resource, id, body):
    """For PUT requests to a single resource"""

    for required_element in required_elements[resource.upper()]:
        if required_element not in body:
            return f"{required_element} is required"

    for index, item in enumerate(DATABASE[resource.upper()]):
        if item["id"] == id:
            # Found the item. Update the value.
            DATABASE[resource.upper()][index] = body
            break


def delete(resource, id):
    """For DELETE requests to a single resource"""
    # Initial -1 value for animal index, in case one isn't found
    item_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, item in enumerate(DATABASE[resource.upper()]):
        if item["id"] == id:
            # Found the animal. Store the current index.
            item_index = index

    # If the animal was found, use pop(int) to remove it from list
    if item_index >= 0:
        DATABASE[resource.upper()].pop(item_index)