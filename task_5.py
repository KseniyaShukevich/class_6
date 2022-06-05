class Stationery:
    def __init__(self, title='something'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки: ', self.title)


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой: ', self.title)


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом: ', self.title)


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером: ', self.title)


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
pen.draw()
pencil.draw()
handle.draw()
