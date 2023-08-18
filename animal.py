class Animal:
    def __init__(self, name, age, price, animal_type):
        self.name = name
        self.age = age
        self.price = price
        self.animal_type = ""

    def get_animal(self):
        description = (
            self.name
            + " "
            + str(self.age)
            + " "
            + str(self.price)
            + " "
            + self.animal_type
        )
        print(description)

    def check_price(self):
        return self.price

    def compare_price(self, price_value):
        if self.price > price_value:
            print("This is expensive")
        else:
            print("This is in budget")


if __name__ == "__main__":
    dog = Animal(name="puppy", age=5, price=1000, animal_type="dog")
    dog.get_animal()
    print(dog.check_price())
    dog.compare_price(500)
