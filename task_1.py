import time

class TrafficLight:
    __color = 'red'

    def running(self):
        while True:
            print('Red')
            time.sleep(7)
            print('Yellow')
            time.sleep(2)
            print('Green')
            time.sleep(5)
            print('Yellow')
            time.sleep(2)

obj = TrafficLight()
obj.running()
