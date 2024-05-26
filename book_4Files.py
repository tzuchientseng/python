import os

print("----------------------------------------", 'demo-os.getcwd()(get current directory), os.walk()(Field: dirname, sub_dirnames, filenames), os.listdir()', "-"*40)
print("Current Working Directory:", os.getcwd())
print("The content: ", os.listdir(os.getcwd()))

# Ensure the 'D' directory exists at the root level
if os.path.exists('D:/coding/python'):
    for dirname, sub_dirnames, filenames in os.walk('D:/coding/python'):
        print("Current Directory:", dirname)
        print("Subdirectories:", sub_dirnames)
        print("Files:", filenames)
        print()
else:
    print("The directory does not exist at the root level.")

print("----------------------------------------", 'demo-mkdir', "-"*40)
mydir = "test"
if os.path.exists(mydir):
    print(f"{mydir}, is exist!")
else:
    # os.mkdir(mydir)
    # print(f"Build the {mydir} sucessfully.")
    pass

print("----------------------------------------", 'demo-os.path.join()', "-"*40)
import os

_path = os.path.join('D:\\','coding','python')
print(os.path.getsize(_path), 'bytes')

print("----------------------------------------", 'demo-glob(列出特定工作目錄內容)', "-"*40)
import os 
import glob
print("Method1: list out \\coding\\python files and sizes. ")
for file in glob.glob('D:\\coding\python\*'):
    print(f"{file} : {os.path.getsize(file)} bytes")

print("----------------------------------------", 'demo-Read() the file and close()', "-"*40)
fn = 'D:\\Coding\\python\\test.py'
fObj = open(fn, 'r', encoding='cp950') #ANSI
data = fObj.read()
fObj.close()
print(data)
print("----------------------------------------", 'demo-with open()', "-"*40)
fn = 'D:\\Coding\\python\\test.py'
with open(fn, 'r', encoding='cp950') as fObj:
    data = fObj.read()
print(data)

print("----------------------------------------", 'demo-readline()(Read lines by line)', "-"*40)
fn = 'D:\\Coding\\python\\test.py'
with open(fn, 'r', encoding='cp950') as fObj:
    for line in fObj:
        print(line.rstrip())
print("====or====")
with open(fn, 'r', encoding='cp950') as fObj:
    txt1 = fObj.readline()
    print(txt1)
    print(fObj.readline())

print("----------------------------------------", 'demo-readlines()', "-"*40)
fn = 'D:\\Coding\\python\\test.py'
with open(fn, 'r', encoding='cp950') as fObj:
    mylist = fObj.readlines()
    # print(mylist)
    for line in mylist:
        print(line.rstrip())

print("----------------------------------------", 'demo-tell(), read(n)', "-"*40)
fn = 'D:\\Coding\\python\\test.py'
with open(fn, 'r', encoding='cp950') as fObj:
    print(f"Point location: {fObj.tell()}")
    txt1 = fObj.read(3)
    print(f"{txt1}, point locattion: {fObj.tell()}")
    txt2 = fObj.read(3)
    print(f"{txt2}, point locattion: {fObj.tell()}")
    txt3 = fObj.read(3)
    print(f"{txt3}, point locattion: {fObj.tell()}")
