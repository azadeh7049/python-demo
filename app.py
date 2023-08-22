from car import Car
from animal import Animal
from customer import Customer


def pet_owner(customer):
    if customer.has_pet:
        print(f"{customer.name} has a pet")
    else:
        print(f"{customer.name} does not have a pet")


def approve_loan(customer: Customer) -> bool:
    if customer.balance > 5000 and customer.has_pet:
        print(f"{customer.name} is approved for a loan")
        return True
    else:
        print(f"{customer.name} is not approved for a loan")
        return False


if __name__ == "__main__":
    car = Car(name="Audi", model="G4", year=2023)
    print(car.get_descriptive())

    animal = Animal(name="Kitty", age=2, price=2500, animal_type="Cat")
    animal.get_animal()

    mike = Customer(name="Mike", address="321 Toronto", balance=1000)
    mike.get_description()
    mike.set_pet_status(True)

    pet_owner(customer=mike)
    approve_loan(customer=mike)

    azadeh = Customer(name="Azadeh", address="123 York blvd", balance=1000000000)
    azadeh.set_pet_status(True)
    approve_loan(customer=azadeh)
