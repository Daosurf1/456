# 2. реализовать класс road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:

    def __init__(self):
        self.length = None
        self.width = None
        self.thickness = None

    def start(self, length, width, thickness,):
        print("вес асвальта")
        self.length = length
        self.width = width
        self.thickness = thickness

        def volume():
            vol= length * width * thickness * 25 / 1000
            return vol


        return volume()


road1 = Road()


print(road1.start(20, 5000, 5), "тон")
