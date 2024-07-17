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

print("----------------------------------------", 'demo-Entry()', "-"*40)
from tkinter import *
window = Tk()
window.title('Entry Test')
lab1 = Label(window, text="Account: ").grid(row=0)
lab2 = Label(window, text="Password: ").grid(row=1)

e1 = Entry(window)
e2 = Entry(window, show='*')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
window.mainloop()

print("----------------------------------------", 'demo-get()', "-"*40)
from tkinter import *

def printInfo():
    print("Account: %s\nPassword: %s" % (e1.get(), e2.get()))
    e1.delete(0, END)
    e2.delete(0, END)

# 建立主視窗
window = Tk()
window.title("ch18_19")  # 視窗標題

# 建立標籤
Label(window, text="Account").grid(row=0)
Label(window, text="Password").grid(row=1)

# 建立文字方塊
e1 = Entry(window)
e2 = Entry(window, show='*')
e1.insert(0, "Kevin")  # 預設文字方塊1内容
e2.insert(0, "pwd")    # 預設文字方塊2内容
e1.grid(row=0, column=1)  # 定位文字方塊1
e2.grid(row=1, column=1)  # 定位文字方塊2

# 建立按鈕
btn1 = Button(window, text="Print", command=printInfo)
btn1.grid(row=2, column=0, sticky=W, pady=10)  # 設定物件與上面的Label切齊，並設定上下間距是10

btn2 = Button(window, text="Quit", command=window.quit)
btn2.grid(row=2, column=1, sticky=W, pady=10)  # 設定物件與上面的Entry切齊，並設定上下間距是10

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo-Entry combine all', "-"*40)
from tkinter import *

def add():
    n3.set(n1.get() + n2.get())

window = Tk()
window.title("ch18_20")  # 視窗標題

n1 = IntVar()
n2 = IntVar()
n3 = IntVar()

e1 = Entry(window, width=8, textvariable=n1)
e2 = Entry(window, width=8, textvariable=n2)
e3 = Entry(window, width=8, textvariable=n3)

e1.grid(row=0, column=0)  # 定位文字方塊1
e2.grid(row=1, column=0)  # 定位文字方塊2
e3.grid(row=2, column=1, padx=5)  # 定位儲存結果文字方塊

label = Label(window, width=8, text="+")
label.grid(row=1, column=1)  # 定位加號

btn = Button(window, width=5, text="等於", command=add)
btn.grid(row=2, column=0, pady=5)  # 定位等號按鈕

window.mainloop()  # 進入主迴圈

print("----------------------------------------", 'demo-Text()', "-"*40)
from tkinter import *

# 建立主視窗
window = Tk()
window.title("ch18_22")  # 視窗標題

# 建立文字方塊
text = Text(window, height=2, width=30)
text.insert(END, "我懷念\n一個人的極境旅行")
str_content = "2016年12月，我一個人訂了機票和船票，開始我的南極旅行，飛機經杜拜再往阿根廷的烏斯懷雅，在此我登上郵輪開始我的南極之旅"
text.insert(END, str_content)
text.pack()

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo-scrollbar(window)', "-"*40)
from tkinter import *

# 建立主視窗
window = Tk()
window.title("ch18_23")  # 視窗標題

# 建立卷軸物件
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)  # 靠右安置與父物件高度相同

# 建立文字區域物件
text = Text(window, height=10, width=30)
text.pack(side=LEFT, fill=Y)  # 靠左安置與父物件高度相同

# 設定卷軸與文字區域的互動
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

# 插入文字內容
text.insert(END, "我懷念\n一個人的極境旅行")
str_content = "2016年12月，我一個人訂了機票和船票，開始我的南極旅行，飛機經杜拜再往阿根廷的烏斯懷雅，在此我登上郵輪開始我的南極之旅"
text.insert(END, str_content)

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo-Radiobutton()', "-"*40)
from tkinter import *

def printSelection():
    label.config(text="你選擇了 " + var.get())

# 建立主視窗
window = Tk()
window.title("ch18_24")  # 視窗標題

# 變數設定
var = StringVar()
var.set("男生")  # 預設選項

# 標籤
label = Label(window, text="尚未選擇", bg="Lightyellow", width=30)
label.pack()

# 單選按鈕
rb1 = Radiobutton(window, text="男生", variable=var, value='男生', command=printSelection)
rb2 = Radiobutton(window, text="女生", variable=var, value='女生', command=printSelection)
rb1.pack()
rb2.pack()

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo', "-"*40)
from tkinter import *

def printSelection():
    print(cities[var.get()])
    # 列出所選城市

# 建立主視窗
window = Tk()
window.title("ch18_25")  # 視窗標題

# 城市選項
cities = {0: "東京", 1: "紐約", 2: "巴黎", 3: "倫敦", 4: "香港"}

# 變數設定
var = IntVar()
var.set(0)  # 預設選項

# 標籤
label = Label(window, text="選擇最喜歡的城市", fg="blue", bg="Lightyellow", width=30)
label.pack()

# 建立選項按鈕
for val, city in cities.items():
    Radiobutton(window, text=city, variable=var, value=val, command=printSelection).pack()

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo', "-"*40)
from tkinter import *

def printSelection():
    print(cities[var.get()])
    # 列出所選城市

# 建立主視窗
window = Tk()
window.title("ch18_25")  # 視窗標題

# 城市選項
cities = {0: "東京", 1: "紐約", 2: "巴黎", 3: "倫敦", 4: "香港"}

# 變數設定
var = IntVar()
var.set(0)  # 預設選項

# 標籤
label = Label(window, text="選擇最喜歡的城市", fg="blue", bg="Lightyellow", width=30)
label.pack()

# 建立選項按鈕
for val, city in cities.items():
    Radiobutton(window, text=city, indicatoron=0, width=30, variable=var, value=val, command=printSelection).pack()

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo-Checkbutton()', "-"*40)
from tkinter import *

# 建立主視窗
window = Tk()
window.title("ch18_27")  # 視窗標題

# 標籤
Label(window, text="請選擇喜歡的運動", fg="blue", bg="Lightyellow", width=30).grid(row=0)

# 變數設定
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

# 勾選框
Checkbutton(window, text="美式足球", variable=var1).grid(row=1, sticky=W)
Checkbutton(window, text="棒球", variable=var2).grid(row=2, sticky=W)
Checkbutton(window, text="籃球", variable=var3).grid(row=3, sticky=W)

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo', "-"*40)
from tkinter import *

def printInfo():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection += sports[i] + "\t"
    print(selection)

# 建立主視窗
window = Tk()
window.title("ch18_28")  # 視窗標題

# 標籤
Label(window, text="請選擇喜歡的運動", fg="blue", bg="Lightyellow", width=30).grid(row=0)

# 運動字典
sports = {0: "美式足球", 1: "棒球", 2: "籃球", 3: "網球"}
checkboxes = {}

# 建立勾選框
for i in range(len(sports)):
    checkboxes[i] = BooleanVar()
    Checkbutton(window, text=sports[i], variable=checkboxes[i]).grid(row=i+1, sticky=W)

# 確定按鈕
Button(window, text="確定", width=10, command=printInfo).grid(row=len(sports)+1, sticky=W)

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo', "-"*40)
from tkinter import *
from tkinter import messagebox

def myMsg():
    # 按Good Morning按鈕時執行
    messagebox.showinfo("My Message Box", "Python tkinter")

# 建立主視窗
window = Tk()
window.title("ch18_29")  # 視窗標題
window.geometry("300x160")  # 視窗寬300高160

# 按鈕
Button(window, text="Good Morning", command=myMsg).pack()

# 進入主迴圈
window.mainloop()

# print("----------------------------------------", 'demo-PhotoImage()', "-"*40)
# from tkinter import *

# # 建立主視窗
# window = Tk()
# window.title("ch18_30")  # 視窗標題

# # 載入圖片
# html_gif = PhotoImage(file="ma.gif")

# # 顯示圖片
# Label(window, image=html_gif).pack()

# # 進入主迴圈
# window.mainloop()

# print("----------------------------------------", 'demo', "-"*40)
# from tkinter import *

# # 建立主視窗
# window = Tk()
# window.title("ch18_31")  # 視窗標題

# # 載入圖片
# sselogo = PhotoImage(file="sse.gif")
# Label(window, image=sselogo).pack(side="right")

# # 設定文字內容
# sseText = "SSE全名是Silicon Stone Education，這家公司在美國，這是國際專業證照公司，產品多元與豐富。"
# Label(window, text=sseText, bg="lightyellow", padx=10).pack(side="left")

# # 進入主迴圈
# window.mainloop()

# print("----------------------------------------", 'demo', "-"*40)
# from tkinter import *

# def msgShow():
#     label.config(text="I love Python", bg="Lightyellow", fg="blue")

# # 建立主視窗
# window = Tk()
# window.title("ch18_33")  # 視窗標題

# # 標籤
# label = Label(window)
# label.pack()

# # 載入圖片並建立按鈕
# sun_gif = PhotoImage(file="sun.gif")
# btn = Button(window, image=sun_gif, command=msgShow)
# btn.pack()

# # 進入主迴圈
# window.mainloop()

print("----------------------------------------", 'demo-Scale', "-"*40)
from tkinter import *

def printInfo():
    print(slider1.get(), slider2.get())

# 建立主視窗
window = Tk()
window.title("ch18_35")  # 視窗標題

# 建立垂直尺度
slider1 = Scale(window, from_=0, to=10)
slider1.pack()

# 建立水平尺度
slider2 = Scale(window, from_=0, to=10, length=300, orient=HORIZONTAL)
slider2.set(3)  # 設定水平尺度初始值
slider2.pack()

# 建立按鈕
Button(window, text="Print", command=printInfo).pack()

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo', "-"*40)
from tkinter import *
from tkinter import messagebox

def newfile():
    messagebox.showinfo("開新檔案", "可在此撰寫開新檔案程式碼")

def savefile():
    messagebox.showinfo("儲存檔案", "可在此撰寫儲存檔案程式碼")

def about():
    messagebox.showinfo("程式說明", "作者：洪錦魁")

# 建立主視窗
window = Tk()
window.title("ch18_36")
window.geometry("300x160")  # 視窗寬300高160

# 建立功能表物件
menu = Menu(window)
window.config(menu=menu)

# 建立檔案功能表
filemenu = Menu(menu)
menu.add_cascade(label="檔案", menu=filemenu)
filemenu.add_command(label="開新檔案", command=newfile)
filemenu.add_separator()  # 增加分隔線
filemenu.add_command(label="儲存檔案", command=savefile)
filemenu.add_separator()  # 增加分隔線
filemenu.add_command(label="結束", command=window.destroy)

# 建立說明功能表
helpmenu = Menu(menu)
menu.add_cascade(label="說明", menu=helpmenu)
helpmenu.add_command(label="程式說明", command=about)

# 進入主迴圈
window.mainloop()

print("----------------------------------------", 'demo', "-"*40)
from tkinter import *

def calculate():
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))

def show(buttonString):
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)

def backspace():
    equ.set(equ.get()[:-1])

def clear():
    equ.set("0")

root = Tk()
root.title("計算器")

equ = StringVar()
equ.set("0")

label = Label(root, width=25, height=2, relief="raised", anchor=SE, textvariable=equ)
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

clearButton = Button(root, text="C", fg="blue", width=5, command=clear)
clearButton.grid(row=1, column=0)

Button(root, text="DEL", width=5, command=backspace).grid(row=1, column=1)
Button(root, text="%", width=5, command=lambda: show("%")).grid(row=1, column=2)
Button(root, text="/", width=5, command=lambda: show("/")).grid(row=1, column=3)

Button(root, text="7", width=5, command=lambda: show("7")).grid(row=2, column=0)
Button(root, text="8", width=5, command=lambda: show("8")).grid(row=2, column=1)
Button(root, text="9", width=5, command=lambda: show("9")).grid(row=2, column=2)
Button(root, text="*", width=5, command=lambda: show("*")).grid(row=2, column=3)

Button(root, text="4", width=5, command=lambda: show("4")).grid(row=3, column=0)
Button(root, text="5", width=5, command=lambda: show("5")).grid(row=3, column=1)
Button(root, text="6", width=5, command=lambda: show("6")).grid(row=3, column=2)
Button(root, text="-", width=5, command=lambda: show("-")).grid(row=3, column=3)

Button(root, text="1", width=5, command=lambda: show("1")).grid(row=4, column=0)
Button(root, text="2", width=5, command=lambda: show("2")).grid(row=4, column=1)
Button(root, text="3", width=5, command=lambda: show("3")).grid(row=4, column=2)
Button(root, text="+", width=5, command=lambda: show("+")).grid(row=4, column=3)

Button(root, text="0", width=12, command=lambda: show("0")).grid(row=5, column=0, columnspan=2)
Button(root, text=".", width=5, command=lambda: show(".")).grid(row=5, column=2)
Button(root, text="=", width=5, bg="yellow", command=calculate).grid(row=5, column=3)

root.mainloop()

print("----------------------------------------", 'demo', "-"*40)
