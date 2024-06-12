print("----------------------------------------", 'GUI(Graphical User Interface) with tkinter(ToolKit interface)', "-"*40)
print("----------------------------------------", 'demo-root window', "-"*40)
from tkinter import *

window = Tk()
window.title("My window")
window.geometry("1000x700")
window.mainloop() #按右上角叉叉在會結束程式

print("----------------------------------------", 'demo-Label', "-"*40)
from tkinter import *

window = Tk()
window.title("My window")
window.geometry("1000x700")

label = Label(window, text='I like tkinter'
                    , bg='lightyellow'
                    , width=15
                    , font="Helvetica 16 bold italic")
label.pack() #包裝與定位文件

window.mainloop() #按右上角叉叉在會結束程式

print("----------------------------------------", 'demo-Layout Management:pack()', "-"*40)
from tkinter import *

window = Tk()
window.title("My window")
window.geometry("1000x700")

label1 = Label(window, text='I like tkinter'
                    , bg='lightyellow'
                    , width=15
                    , font="Helvetica 16 bold italic")
label2 = Label(window, text='My Name is Sunny~'
                    , bg='lightblue'
                    , width=15)
label3 = Label(window, text='I am from Taiwan' 
                    , bg='lightgreen'
                    , width=15)

label1.pack() #包裝與定位文件
label2.pack(side=LEFT, padx=7) #包裝與定位文件
label3.pack(side=LEFT) #包裝與定位文件

window.mainloop() #按右上角叉叉在會結束程式

print("----------------------------------------", 'demo-Layout Management:grid()', "-"*40)
from tkinter import *

window = Tk()
window.title("My window")
window.geometry("1000x700")

label1 = Label(window, text='I like tkinter'
                    , bg='lightyellow'
                    , width=15
                    , font="Helvetica 16 bold italic")
label2 = Label(window, text='My Name is Sunny~'
                    , bg='lightblue'
                    , width=15)
label3 = Label(window, text='I am from Taiwan' 
                    , bg='lightgreen'
                    , width=15)

label1.grid(row=0, column=1)
label2.grid(row=1, column=0) 
label3.grid(row=1, column=1) 

window.mainloop() #按右上角叉叉在會結束程式

print("----------------------------------------", 'demo-columnspan', "-"*40)
from tkinter import *

# 創建主視窗
window = Tk()
window.title("Label Demo")
window.geometry("1000x700")

# 創建標籤
lab1 = Label(window, text="標籤1", relief="raised")
lab2 = Label(window, text="標籤2", relief="raised")
lab3 = Label(window, text="標籤3", relief="raised")
lab4 = Label(window, text="標籤4", relief="raised")
lab5 = Label(window, text="標籤5", relief="raised")
lab6 = Label(window, text="標籤6", relief="raised")
lab7 = Label(window, text="標籤7", relief="raised")
lab8 = Label(window, text="標籤8", relief="raised")

# 使用 grid 方法佈局標籤
lab1.grid(row=0, column=0)
lab2.grid(row=0, column=1, columnspan=2)
lab4.grid(row=0, column=3, rowspan=2)
lab5.grid(row=1, column=0)
lab6.grid(row=1, column=1)
lab7.grid(row=1, column=2)

# 進入主循環
window.mainloop()

print("----------------------------------------", 'demo-place()', "-"*40)
from tkinter import *

window = Tk()
window.title("place()")

Lab1 = Label(window, text="I like tkinter", bg="lightyellow", width=15)
Lab2 = Label(window, text="My Name is Sunny~", bg="lightgreen", width=15)
Lab3 = Label(window, text="I am from Taiwan", bg="lightblue", width=15)

# 使用 place() 方法直接設定標籤的位置
Lab1.place(x=0, y=0)  # 直接定位
Lab2.place(x=30, y=50)  # 直接定位
Lab3.place(x=60, y=100)  # 直接定位

# 運行主視窗的主循環
window.mainloop()

print("----------------------------------------", 'demo-Botton', "-"*40)
from tkinter import *
def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "Lightyellow"
    label["fg"] = "blue"
window =Tk()
label = Label(window)
btn = Button(window, text="Message", command=msgShow)

label.pack()
btn.pack()
window.mainloop()

print("----------------------------------------", 'demo-Exit Button', "-"*40)
from tkinter import *
def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "Lightyellow"
    label["fg"] = "blue"
window = Tk()
window.title("Exit Demo")
label = Label(window)
btn1 = Button(window, text="Message",width=15, command=msgShow)
btn2 = Button(window, text="Exit" ,width=15, command=window.destroy) #Exit window
label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
window.mainloop()

print("----------------------------------------", 'demo-config()', "-"*40)
from tkinter import *

def yellow():
    window.config(bg="yellow")

def blue():
    window.config(bg="blue")

window = Tk()
window.geometry("300x200")  

exitbtn = Button(window, text="Exit", command=window.destroy)
bluebtn = Button(window, text="Blue", command=blue)
yellowbtn = Button(window, text="Yellow", command=yellow)

exitbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
bluebtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
yellowbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)

window.mainloop()

print("----------------------------------------", 'demo-lambda', "-"*40)
from tkinter import *

def change_bg_color(bg_color):
    window.config(bg=bg_color)

window = Tk()
window.title("Lambda Demo")
window.geometry("300x200")

exit_btn = Button(window, text="Exit", command=window.destroy)
blue_btn = Button(window, text="Blue", command=lambda: change_bg_color("blue"))
yellow_btn = Button(window, text="Yellow", command=lambda: change_bg_color("yellow"))

exit_btn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
blue_btn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
yellow_btn.pack(anchor=S, side=RIGHT, padx=5, pady=5)

window.mainloop()

print("----------------------------------------", 'demo-Variable classes', "-"*40)
from tkinter import *

def btn_hit():
    global msg_on
    if not msg_on:
        msg_on = True
        Varx.set("I like python")
    else:
        msg_on = False
        Varx.set("")

window = Tk()
window.title("Variance Test")

msg_on = False
Varx = StringVar()

label = Label(window, textvariable=Varx,
              fg="blue", bg="lightyellow",
              font="Verdana 16 bold", 
              width=25, height=2)
label.pack()

btn = Button(window, text="Hit", command=btn_hit)
btn.pack()

window.mainloop()

print("----------------------------------------", 'demo', "-"*40)
