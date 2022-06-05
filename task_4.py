class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Go!')

    def stop(self):
        print('Stop!')

    def turn(self, direction):
        print('Turn to', direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость выше 60!!! Скорость: ', self.speed)
        else:
            print('Скорость: ', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость выше 40!!! Скорость: ', self.speed)
        else:
            print('Скорость: ', self.speed)


class PoliceCar(Car):
    is_police = True


town_car = TownCar(50, 'black', 'Black Town Car')
print(town_car.name)
print(town_car.is_police)
town_car.go()
town_car.show_speed()
town_car.turn('left')
town_car.speed = 61
town_car.show_speed()
town_car.stop()

sport_car = SportCar(100, 'red', 'Red Sport Car')
print(sport_car.name)
print(sport_car.is_police)
sport_car.go()
sport_car.show_speed()
sport_car.turn('right')
sport_car.speed = 120
sport_car.show_speed()
sport_car.stop()

work_car = WorkCar(50, 'white', 'White Work Car')
print(work_car.name)
print(work_car.is_police)
work_car.go()
work_car.show_speed()
work_car.turn('left')
work_car.speed = 30
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(100, 'blue', 'Blue Police Car')
print(police_car.name)
print(police_car.is_police)
police_car.go()
police_car.show_speed()
police_car.turn('right')
police_car.speed = 120
police_car.show_speed()
police_car.stop()
