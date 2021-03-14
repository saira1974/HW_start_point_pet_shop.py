# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, pound_sterling):
    pet_shop["admin"]["total_cash"] += pound_sterling

def add_or_remove_cash(pet_shop, pound_sterling):
    pet_shop["admin"]["total_cash"] += pound_sterling

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num_pets_sold):
    pet_shop["admin"]["pets_sold"] += num_pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed (pet_shop,breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)
    return found_pets

def get_pets_by_breed (pet_shop,breed):
    not_found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            not_found_pets.append(pet)
    return not_found_pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

# Not sure on the one below...
# From what I understand the return is None because there isn't a customer called Fred nor a pet called Fred.
# If I put Fred where "name" is and return "none" then I get a NameError Fred is not defined.
# I know this is similar to the one above which is why I have kept it the same so that I don't get an error...

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    delete_pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(delete_pet)

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(custome):
    return custome["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)


