print("----------------------------------------", 'demo-os.getcwd()(get current directory), os.walk()(field: dirname, sub_dirnames, filenames), os.listdir()', "-"*40)
import os
print("current working directory:", os.getcwd())
print("the content: ", os.listdir(os.getcwd()))

# ensure the 'd' directory exists at the root level
if os.path.exists('d:/coding/python'):
    for dirname, sub_dirnames, filenames in os.walk('d:/coding/python'):
        print("current directory:", dirname)
        print("subdirectories:", sub_dirnames)
        print("files:", filenames)
        print()
else:
    print("the directory does not exist at the root level.")

print("----------------------------------------", 'demo-mkdir', "-"*40)
mydir = "test"
if os.path.exists(mydir):
    print(f"{mydir}, is exist!")
else:
    # os.mkdir(mydir)
    # print(f"build the {mydir} sucessfully.")
    pass

print("----------------------------------------", 'demo-os.path.join()', "-"*40)
import os

_path = os.path.join('d:\\','coding','python')
print(os.path.getsize(_path), 'bytes')

print("----------------------------------------", 'demo-!!!!!!!動態路徑(可在不同的目錄下執行)!!!!!!!', "-"*40)
import os
fn = os.path.join(os.path.dirname(__file__), '_fileName_')

print("----------------------------------------", 'demo-glob(列出特定工作目錄內容) + os.path.getsize()', "-"*40)
import os 
import glob
print("method1: list out \\coding\\python files and sizes. ")
for file in glob.glob('d:\\coding\python\*'):
    print(f"{file} : {os.path.getsize(file)} bytes")

print("----------------------------------------", 'demo-read() the file and close()', "-"*40)
fn = 'd:\\coding\\python\\temp\\test.py'
fobj = open(fn, 'r', encoding='cp950') #ansi
data = fobj.read()
fobj.close()
print(data)
print("----------------------------------------", 'demo-with open() as', "-"*40)
fn = 'd:\\coding\\python\\temp\\test.py'
with open(fn, 'r', encoding='cp950') as fobj:
    data = fobj.read()
print(data)

print("----------------------------------------", 'demo-readline()(read lines by line)', "-"*40)
fn = 'd:\\coding\\python\\temp\\test.py'
with open(fn, 'r', encoding='cp950') as fobj:
    for line in fobj:
        print(line.rstrip())
print("====or====")
with open(fn, 'r', encoding='cp950') as fobj:
    txt1 = fobj.readline()
    print(txt1)
    print(fobj.readline())

print("----------------------------------------", 'demo-readlines()', "-"*40)
fn = 'd:\\coding\\python\\temp\\test.py'
with open(fn, 'r', encoding='cp950') as fobj:
    mylist = fobj.readlines()
    # print(mylist)
    for line in mylist:
        print(line.rstrip())

print("----------------------------------------", 'demo-tell()+read(n)', "-"*40)
fn = 'd:\\coding\\python\\temp\\test.py'
with open(fn, 'r', encoding='cp950') as fobj:
    print(f"point location: {fobj.tell()}")
    txt1 = fobj.read(3)
    print(f"{txt1}, point locattion: {fobj.tell()}")
    txt2 = fobj.read(3)
    print(f"{txt2}, point locattion: {fobj.tell()}")
    txt3 = fobj.read(3)
    print(f"{txt3}, point locattion: {fobj.tell()}")

print("----------------------------------------", 'demo-read by chunk', "-"*40)
fn = 'd:\\coding\\python\\temp\\test.py'
chunk = 100
msg = ''
with open(fn, 'r', encoding='cp950') as fobj:
    while True:
        txt = fobj.read(chunk)
        if not txt:
            break
        msg += txt
print(msg)

print("----------------------------------------", 'demo-write()', "-"*40)
fn = 'd:\\coding\\python\\temp\\test.py'
string = 'print(\'i love python.\')'

# with open(fn, 'w+', encoding='cp950') as fobj: #檔案不再則新增
with open(fn, 'w', encoding='cp950') as fobj:
    print(fobj.write(string)) #only str()

print("----------------------------------------", 'demo-append', "-"*40)
fn = 'd:\\coding\\python\\temp\\test.py'
str = 'print(\'append\')'
str2 = 'print(\'------\')'

with open(fn, 'a') as fobj:
    fobj.write('\n' + str + '\n')
    fobj.write(str2 + '\n')

mystr = ['print(\'my name is sunny.\')']
with open(fn, 'a', encoding='cp950') as fobj:
    fobj.writelines(mystr)

print("----------------------------------------", 'demo-duplicate the binary file', "-"*40)
src = 'temp\\sunny.jpg'
dst = 'temp\\sunny1.jpg'
tmp = ''

with open(src, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(dst, 'wb') as file_wr:
        file_wr.write(tmp)

print("----------------------------------------", 'demo-tell()+seek(offet, origin)', "-"*40)
dst = 'temp\\bdata'
bytedata =  bytes(range(0, 256))
with open(dst, 'wb') as file_dst:
    file_dst.write(bytedata)
with open(dst, 'rb') as file_src:
    print("curent pointer: ", file_src.tell())
    file_src.seek(10)
    print("curent pointer: ", file_src.tell())
    data = file_src.read()
    print("current content: ", data[0])
    file_src.seek(255)
    print("current pointer: ", file_src.tell())
    data = file_src.read()
    print("current content: ", data[0])

print("----------------------------------------", 'demo-shutil', "-"*40)
import  os
import shutil
mydir = "test"
if os.path.exists(mydir):
    print(f"{mydir}, is exist!")
else:
    os.mkdir(mydir)
    print(f"build the {mydir} sucessfully.")
    pass

shutil.rmtree('test')
print(f"->rmtree({mydir}).")

print("----------------------------------------", 'demo-send2trash', "-"*40)
import os
import send2trash
os.mkdir('HI')
fn = 'd:\\coding\\python\\Hi\\test.py'
string = 'print(\'i love python.\')'
with open(fn, 'w', encoding='cp950') as fobj:
    print("The bytes: ", fobj.write(string)) #only str()
send2trash.send2trash('HI')

print("----------------------------------------", 'demo-with zipfile.ZipFile(\'out.zip\',\'w\') as ...', "-"*40)
import zipfile
import glob, os

# 創建一個新的 ZIP 檔案
with zipfile.ZipFile('temp/sunny.zip', 'w', zipfile.ZIP_DEFLATED) as fileZip:
    for name in glob.glob('temp/*'):
        if os.path.isfile(name) and not name.endswith('.zip'):
            fileZip.write(name, os.path.basename(name))
            print(f"Added {name} to the ZIP file.")
print("ZIP file created successfully.")

"""
import zipfile
import glob
import os
# 創建一個新的 ZIP 檔案
try:
    with zipfile.ZipFile('temp/sunny.zip', 'w', zipfile.ZIP_DEFLATED) as fileZip:
        for name in glob.glob('temp/*'):
            # 檢查是否是文件
            if os.path.isfile(name):
                try:
                    file_size = os.path.getsize(name)
                    print(f"Adding {name} to the ZIP file. Size: {file_size} bytes")
                    fileZip.write(name, os.path.basename(name))
                    print(f"Successfully added {name}")
                except Exception as e:
                    print(f"Failed to add {name} to the ZIP file. Error: {e}")
            else:
                print(f"Skipped {name}, because it's not a file.")
    print("ZIP file created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
"""
import zipfile

# 列出 ZIP 文件內容
with zipfile.ZipFile('temp/sunny.zip', 'r') as listZipInfo:
    print(listZipInfo.namelist())
    print()
    for info in listZipInfo.infolist():
        print(info.filename, info.file_size, info.compress_size)

#extractall()
import zipfile
import os
# 確保目錄存在
output_dir = 'temp/temp2'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# 解壓縮文件
with zipfile.ZipFile('temp/sunny.zip', 'r') as fileUnZip:
    fileUnZip.extractall(output_dir)
    print(f"Files extracted to {output_dir}")
