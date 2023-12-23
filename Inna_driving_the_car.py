import random
class Car:
    def __init__(self, model, color, economy, mileage: int = 0, fuel: int = 100):
        self._mileage = mileage
        self._fuel = fuel
        self._model = model
        self._color = color
        self._economy = economy
    def drive(self, distance):
        if distance > self.distance_left():
            raise Exception("Not enough fuel")
        else:
            self._fuel -= distance / 100 * self._economy
            self._mileage += distance
    def distance_left(self):
        return self._fuel * 100 / self._economy
    def fuel_up(self):
        self._fuel += 20

empty_cars_list = []
models_list = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
colors_list = ["blue", "yellow", "white"]
random_color = random.choice(colors_list)
random_economy = random.randint(5,20)

for i in models_list:
    car = Car(i, random_color, random_economy)
    empty_cars_list.append(car)
for car in empty_cars_list:
    car.drive(200)
    car.fuel_up()
    car.drive(100)
max_fuel_reserve_car = max(empty_cars_list, key=lambda x: x._fuel)

print(f"A car with the biggest fuel reserve is {max_fuel_reserve_car._model}, {max_fuel_reserve_car._color}, uses {max_fuel_reserve_car._economy} l/100km, {max_fuel_reserve_car._mileage} km passed, remains {max_fuel_reserve_car._fuel} l")