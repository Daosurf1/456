# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.


class Car:

    def __init__(self, speed=1, color="red", name="Porsche", is_police: bool = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def on_start(self):
        print('start')
        print(f"Go-go  {self.name} with speed {self.speed}!")
        self.show_speed()

    def show_speed(self):
        if type(self)== Town_car and self.speed >50 or type(self) == WorkCar and self.speed >= 60:
            print('Превышение скорости')
        self.on_stop()


    def on_stop(self):
        print("Stop")

    def turn_rigt(self):
        print(f'{self.name} повернула на право')
        pass

    def turn_left(self):
        print(f'{self.name} повернула на лево')
        pass



class Town_car(Car):
    pass


class ClassSportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    # self.is_police=True
    pass


car1 = Car(19, 'green', 'Lexus', False)
print(car1.name)
car1.on_stop()
print('-'*35)

car2 = Town_car(70, 'black', 'Smart', False)
car2.on_start()
car2.turn_rigt()
print('-'*35)

car3 = WorkCar(70, 'red', 'Kamaz', False)
car3.on_start()
car3.turn_left()