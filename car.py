class car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 45

    def get_descriptive(self):
        long_name = str(self.name) + " " + (self.model) + " " + str(self.year)
        return long_name.title()

    def read_odometer(self):
        """prints the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """sets the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """increments the odometer reading by the given amount"""
        self.odometer_reading += miles


if __name__ == "__main__":
    car = car(name="BMW", model="320", year=2019)
    print(car.get_descriptive())
    car.read_odometer()
    car.update_odometer(mileage=23)
