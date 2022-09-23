import time
import sys



def blink_once():
    sys.stdout.write('\r\033[1m\033[37m\033[43m{}\033[0m'.format(" Желтый "))
    time.sleep(0.5)
    sys.stdout.write('\r     ')
    time.sleep(0.5)
    sys.stdout.write('\r\033[1m\033[37m\033[43m{}\033[0m'.format(" Желтый "))
    time.sleep(0.5)

def blink(number):
     for x in range(0,number):
         blink_once()



class Traffic:

    def ligh(self, red=2, yellow=3, green=4):
        print("\033[31m\033[47m{}\033[0m".format(" Красный "))
        time.sleep(red)
        blink(4)
        time.sleep(yellow)
        sys.stdout.write('\n\r     ')
        print("\r\033[32m\033[40m{}\033[0m".format(" Зеленый "))
        time.sleep(green)
        self.on_stop()

    def on_stop(self):
        print("Go")


Traffic_lights_1 = Traffic()
Traffic_lights_1.ligh(3, 1, 0)
