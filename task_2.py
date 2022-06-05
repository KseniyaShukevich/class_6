class Road:
    __weight_asphalt = 25
    __thickness = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_weight(self):
        print((self.__length * self.__width * self.__weight_asphalt * self.__thickness) / 1000, 'т')


obj = Road(10, 5)
obj.calc_weight()
