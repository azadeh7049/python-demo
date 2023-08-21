class Customer:
    def __init__(self, name, address, balance):
        self.name = name
        self.address = address
        self.balance = balance
        self.has_pet = False

    def update_name(self, new_name):
        self.name = new_name

    def update_address(self, new_address):
        self.address = new_address

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def get_balance(self):
        return self.balance

    def set_pet_status(self, has_pet=False):
        self.has_pet = has_pet

    def get_description(self):
        print("Hello my name is", self.name)
        print("My address is", self.address)


if __name__ == "__main__":
    rutuja = Customer(name="Rutuja", address="123 Toronto", balance=0)
    rutuja.deposit(100)
    print(rutuja.get_balance())
    rutuja.withdraw(50)
    print(rutuja.get_balance())
    rutuja.get_description()
    rutuja.update_name("Azadeh")
    rutuja.update_address("123 Vancouver")
    rutuja.get_description()
    print(rutuja.has_pet)
    rutuja.set_pet_status(True)
    print(rutuja.has_pet)
