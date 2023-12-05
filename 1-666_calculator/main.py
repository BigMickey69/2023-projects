#「大學國文：科技人文選讀-科學與文化」中一次國文報告使用，報告的書中提到"布萊文"，一個極端的基督徒，指控當時美國前總統"雷根"是敵基督、惡魔
#他的說他的證據是以他定義的字母規則(A = 1 x 6, B = 2 x 6... Z = 26 x 6)
#雷根的名字"Ronald Reagan"會等於660
#前面再加"A"的話是666，野獸的數字 ¯\_(ツ)_/¯
#這個計算機讓你方便運算並找出666的字串
#n 為倍率，d為差
#右上角pin使視窗永遠在上 (Tkinter 不支持gif，所以我讓他顯示的方式很慢需要載入幾秒)

import tkinter as tk
from PIL import Image,ImageTk
from gif import ImageLabel
Devil = False
bullshit = "這世間存在著不少超自然現象與靈異事件，\n而其主因大都是惡魔的存在。\n即使存在惡魔獵人，還是有不少惡魔活在你我之中，\n日常生活中的縫隙。\n此計算機能揭開世間的奧秘，請問你也是惡魔嗎?"
dog = tk.Tk()
def pinfunc ():
    global state
    if (state):
        state = False 
    else: 
        state = True
    dog.attributes('-topmost',state)
state = False

#initials
dog.resizable(width=False, height=False)
dog.title("666 計算機，你也是惡魔嗎?")
dog.geometry("500x650")
dog.iconbitmap(r"1-666_calculator\icon.ico")



#top text
title = tk.Label(dog, text=bullshit, font=('Arial', 13), bg="#D5DADE")
title.pack(pady=20)

#pin
pin = tk.Button(dog, text=" Pin ", font=('Comic Sans MS', 9), command=pinfunc, borderwidth=3)
pin.place(x=460,y=2)

#input
e = tk.Entry(dog, width=28, font=('Arial', 14))
e.pack()


#declare n,d


#check button (w/fire)
fire = ImageLabel(dog)
fire.place(relx=0.5,rely=0.83, anchor=tk.CENTER)
def exe ():
    global Devil
    if (Devil):
        fire.place_forget()
        Devil = False
    word = e.get()
    n = float(nbox.get())
    d = float(dbox.get())
    f=filter(str.isalpha,word)
    word="".join(f)
    word = word.lower()
    total = 0
    for i in range(len(word)):
        total += float((ord(word[i])-96))*n-d
    total = round(total)
    if (total == 666):  #fire
        Devil = True
        fire.place(relx=0.5,rely=0.83, anchor=tk.CENTER)
        fire.load(r'1-666_calculator\fire.gif')

    #output
    temp = tk.Label(dog, text="                          ", bg="black")
    temp.place(x=245,y=206,anchor="center")
    outp = tk.Label(dog, text=total, font=('Arial', 18, "bold"), bg="black", fg="white")
    outp.place(x=245,y=206,anchor="center")

butt = tk.Button(dog, text=" Check! ", font=('Chiller', 11, 'bold'), command=exe, borderwidth=2, background="#cdd0db")
butt.place(x=360,y=135)


#ink 
imagey = Image.open(r"1-666_calculator\ink.png")
imagey = imagey.resize((270,70))
imagey2 = ImageTk.PhotoImage(imagey)


imagey3 = Image.open(r"1-666_calculator\arrow.png")
imagey3 = imagey3.resize((40,40))
imagey4 = ImageTk.PhotoImage(imagey3)

canvas = tk.Canvas(dog, width=500, height=70)
canvas.place(relx=0.5,rely=0.318, anchor=tk.CENTER)
canvas.create_image(240,40,image=imagey2)
canvas.create_image(150,25,image=imagey4)


#n
nl = tk.Label(dog, text="n= ", font=('Arial', 13, "italic"))
nl.place(x=410,y=182)
nbox = tk.Entry(dog, width=3, font=('Arial', 10))
nbox.place(x=440,y=185)


#d
nl = tk.Label(dog, text="d= ", font=('Arial', 13,"italic"))
nl.place(x=410,y=212)
dbox = tk.Entry(dog, width=3, font=('Arial', 10))
dbox.place(x=440,y=215)



#description of shit
desc = tk.Text(dog, font=('Arial', 13),width=50, height=9)
desc.pack(pady=100)
text = """     規則:  
             a=1*n - d           
             b=2*n - d           找出字句與名子間的規律，
             c=3*n - d           找出你我間的惡魔。 ༽◺_◿༼
             .
             .
             .
             z=26*n - d
        
"""
desc.insert("0.0", text)
desc.configure(state="disabled")


dog.mainloop()