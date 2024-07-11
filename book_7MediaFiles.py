"""
pip install pillow
from PIL import ImageColor
"""
print("----------------------------------------", 'demo-(r,g,b) = getrgb(color) retrun tuple; Red,Green,Blue,Alpha', "-"*40)
from PIL import ImageColor
print(ImageColor.getrgb('#0000ff'))
print(ImageColor.getrgb('rgb(0, 0, 225)'))
print(ImageColor.getrgb('rgb(0%, 0%, 100%)'))
print(ImageColor.getrgb('Blue'))
print(ImageColor.getrgb('Red'))
print(ImageColor.getrgb('red')) #可小寫

print("----------------------------------------", 'demo-(r,g,b[,a]) = getcolor(color, "MODE")', "-"*40)
from PIL import ImageColor
#MODE: capital letter
print(ImageColor.getcolor('#0000ff', "RGB"))
print(ImageColor.getcolor('rgb(0, 0, 225)', "RGB"))
print(ImageColor.getcolor('rgb(0%, 0%, 100%)', "RGB"))
print(ImageColor.getcolor('Blue', "RGBA"))
print(ImageColor.getcolor('Red', "RGBA"))
print(ImageColor.getcolor('red', "RGBA"))

print("----------------------------------------", 'demo-size, filename', "-"*40)
from PIL import Image
import re
rushMore = Image.open("temp\\basketball.jpg")
print("Object Type: ", type(rushMore))

pattern = r'[^\\]+$' # CharacterClass[不存在\] 在結尾至少一個
name = re.search(pattern, rushMore.filename).group()
# nameList = re.findall(pattern, rushMore.filename)
width, height = rushMore.size
print(f"The fileName: {name}\nThe width: {width} \nThe height: {height}")
print("File extension: ", rushMore.format, "; File description: ", rushMore.format_description)
"""
ISO 10918 是一個國際標準，與 JPEG 圖像壓縮有關。其全稱是 "ISO/IEC 10918" 或 
"Information technology - Digital compression and coding of continuous-tone still images: Requirements and guidelines"，
這是一個由國際標準化組織 (ISO) 和國際電工委員會 (IEC) 聯合制定的標準。它主要涉及到 JPEG 壓縮技術的規範和指導，定義了如何對連續調靜態圖像進行數字壓縮和編碼。

JPEG 是 "Joint Photographic Experts Group" 的縮寫，這個標準由該小組制定並命名。ISO 10918 標準詳細說明了圖像壓縮算法，
文件格式以及壓縮圖像的解碼方式，廣泛應用於數碼相機、網頁圖像和其他需要壓縮靜態圖像的領域。
"""

print("----------------------------------------", 'demo-save(), show()', "-"*40)
from PIL import Image
rushMore = Image.open("temp\\basketball.jpg")
rushMore = rushMore.save('temp\\rushmore.png')
rushMore = Image.open("temp\\rushmore.png")
rushMore.show()

print("----------------------------------------", 'demo-Image.new(MODE, size, color=0)', "-"*40)
"""
PNG (Portable Network Graphics):
特點：支援透明背景和無損壓縮。
用途：適合需要高品質圖像且需透明背景的場合，如網頁圖標、圖表和插圖等。
JPG/JPEG (Joint Photographic Experts Group):
特點：使用有損壓縮，檔案大小較小，適合存儲照片和複雜圖像。
用途：適合照片、網頁圖像以及任何需要平衡圖像品質和檔案大小的場合。

rgba 和 rgb 各要用哪個？
rgba:假設這是需要高品質且可能需要透明背景的圖像，建議使用 PNG 格式，因為 PNG 支援無損壓縮和透明背景。
rgb:假設這是照片或需要較小檔案大小的圖像，建議使用 JPG 或 JPEG 格式，因為這種格式可以有效壓縮圖像並保持較好的圖像品質。
"""
from PIL import Image
pictObj = Image.new("RGB", (300, 180), "aqua")
pictObj.save("temp\\aura.jpg")
pictObj2 = Image.new("RGBA", (300, 180))
pictObj2.save("temp\\invisible.png")

print("----------------------------------------", 'demo-resize((width,heigh), Image.BILINEAR)', "-"*40)
from PIL import Image

pict = Image.open("temp/basketball.jpg")
width, height = pict.size
# Resize the image to double its width while maintaining the height
new_width = width * 2
new_height = height
# Resize with different resampling methods
newpict_nearest = pict.resize((new_width, new_height), Image.NEAREST)
newpict_lanczos = pict.resize((new_width, new_height), Image.LANCZOS)
newpict_bicubic = pict.resize((new_width, new_height), Image.BICUBIC)
# Save the images
newpict_nearest.save("temp/output_nearest_basketball.jpg")
newpict_lanczos.save("temp/output_lanczos_basketball.jpg")
newpict_bicubic.save("temp/output_bicubic_basketball.jpg")

print("----------------------------------------", 'demo-rotate()', "-"*40)
from PIL import Image
pict = Image.open("temp/basketball.jpg")
pict.rotate(70).save("temp\\Rotate.jpg")
pict.rotate(70, expand=True).save("temp\\RotateExpand.jpg")

print("----------------------------------------", 'demo-transpose()', "-"*40)
from PIL import Image
pict = Image.open("temp/basketball.jpg")
pict.transpose(Image.FLIP_LEFT_RIGHT).save("temp\\transposeLR.jpg")
pict.transpose(Image.FLIP_TOP_BOTTOM).save("temp\\transposeTB.jpg")

# Corrected mode 'RBGA' to 'RGBA' and fixed the getpixel method
print("----------------------------------------", 'demo-getpixel()', "-"*40)
from PIL import Image, ImageColor
newImage = Image.new('RGBA', (300, 100), "Yellow")
print(newImage.getpixel((150, 50)))  # Corrected to use a tuple for the coordinates
newImage.save("temp/outputYellow.png")

# Corrected mode 'RBGA' to 'RGBA' and fixed the pixel manipulation
print("----------------------------------------", 'demo-putpixel((x,y),(r,g,b,a))', "-"*40)
newImage = Image.new('RGBA', (300, 300), "Yellow")
for x in range(50, 251):
    for y in range(50, 151):
        newImage.putpixel((x, y), (0, 255, 255, 255))
newImage.save("temp/putpixel.png")

for x in range(50, 251):
    for y in range(151, 251):
        newImage.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA"))
newImage.save("temp/putpixel.png")

# Corrected file path and added required mode to the 'open' method
print("----------------------------------------", 'demo-crop()', "-"*40)
pict = Image.open("temp/basketball.jpg")
cropPict = pict.crop((80, 30, 150, 100))
cropPict.save("temp/crop.jpg")

# Corrected file path
print("----------------------------------------", 'demo-copy()', "-"*40)
pict = Image.open("temp/basketball.jpg")
copyPict = pict.copy()
copyPict.save("temp/copy.jpg")

# Demonstrating crop and paste operations
print("----------------------------------------", 'demo-copy(), paste()', "-"*40)
pict = Image.open("temp/basketball.jpg")
copyPict = pict.copy()
cropPict = copyPict.crop((80, 30, 150, 100))
copyPict.paste(cropPict, (20, 20))
copyPict.paste(cropPict, (20, 100))
copyPict.save("temp/crop_paste.jpg")

# Final demo with loop and creating a new image
print("----------------------------------------", 'demo-fill in', "-"*40)
pict = Image.open("temp/basketball.jpg")
copyPict = pict.copy()
cropPict = copyPict.crop((80, 30, 150, 100))
cropWidth, cropHeight = cropPict.size

width, height = 600, 320
newImage = Image.new('RGB', (width, height), "Yellow")
for x in range(20, width-20, cropWidth):
    for y in range(20, height-20, cropHeight):
        newImage.paste(cropPict, (x, y))

newImage.save("temp/fill.jpg")

print("----------------------------------------", 'demo-filter()', "-"*40)
from PIL import Image
from PIL import ImageFilter

rushMore = Image.open("temp/basketball.jpg")
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("temp\\_BLUR.jpg")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("temp\\_CONTOUR.jpg")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("temp\\_EMBOSS.jpg")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("temp\\_FIND_EDGES.jpg")

print("----------------------------------------", 'demo-Draw()', "-"*40)
from PIL import Image, ImageDraw

newImage = Image.new('RGBA', (300, 300), "Yellow")
drawObj = ImageDraw.Draw(newImage)

# Draw points
for x in range(100, 200, 3):
    for y in range(100, 200, 3):
        drawObj.point([x,y], fill='Green')

# Draw lines, draw outer frame
drawObj.line([(0,0), (299,0), (299,299), (0,299), (0,0)], fill="Black")

# Draw fine lines in top right corner
for x in range(150, 300, 10):
    drawObj.line([(x,0), (300,x-150)], fill="Blue")

# Draw fine lines in bottom left corner
for y in range(150, 300, 10):
    drawObj.line([(0,y), (y-150,300)], fill="Blue")

newImage.save("temp\\Draw.png")

print("----------------------------------------", 'demo-rectangle(), ellipse(), polygon()', "-"*40)
from PIL import Image, ImageDraw

newImage = Image.new('RGBA', (300, 300), 'Yellow')
drawObj = ImageDraw.Draw(newImage)

drawObj.rectangle((0,0,299,299), outline='Black')  # Draw outer frame
drawObj.ellipse((30,60,130,100), outline='Black')  # Draw left eye frame
drawObj.ellipse((65,65,95,95), fill='Blue')  # Draw left eye
drawObj.ellipse((170,60,270,100), outline='Black')  # Draw right eye frame
drawObj.ellipse((205,65,235,95), fill='Blue')  # Draw right eye
drawObj.polygon([(150,120),(180,180),(120,180)], fill='Aqua')  # Draw nose
drawObj.rectangle((100,200,240,240), fill='Red')  # Draw mouth

newImage.save("temp\\ellipse.png")
"""
print("----------------------------------------", 'demo-Words in picture', "-"*40)
from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Sunny Tseng Institute of Technology'  # 設定欲列印英文字串
drawObj.text((50, 50), strText, fill='Blue')  # 使用預設字型與字型大小

# 使用古老英文字型，字型大小是36
fontInfo = ImageFont.truetype('C:\\Windows\\Fonts\\OLDENGL.TTF', 36)
drawObj.text((50, 100), strText, fill='Blue', font=fontInfo)

# 處理中文字體
strCtext = '台中教育大學'  # 設定欲列印中文字串
fontInfo = ImageFont.truetype('C:\\Windows\\Fonts\\DFZongYiStd-W9.otf', 48)
drawObj.text((50, 180), strCtext, fill='Blue', font=fontInfo)

newImage.save("temp\\wordsInPict.png")
"""

print("----------------------------------------", 'demo-pip in qrcode', "-"*40)
import qrcode
import qrcode.constants 
codeText = 'https://tzuchientseng.github.io/sunny.github.io/'
img = qrcode.make(codeText)
print("Type: ", type(img))
img.save("temp\\QRcode.jpg")
"""
def make(data=None, **kwargs):
    qr = qrcode.QRCode(**kwargs) #設定格式
    qr.add_data(data)   #設定條碼內容
    return qr.make_image()  #建立條碼檔案
"""

print("----------------------------------------", 'demo-pict in qrcode', "-"*40)
import qrcode
from PIL import Image

# 創建 QR 碼
qr = qrcode.QRCode(
    version=5,  # 1~40
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # 預設為 'M'
    box_size=10,
    border=4  # 預設為 4
)
qr.add_data('https://sunnytseng.com/')
qr.make(fit=True)
img = qr.make_image(fill_color='gray')

# 獲取 QR 碼的尺寸
width, height = img.size

# 加載要嵌入的圖標
icon = Image.open('temp\\skateman.JPEG')
# icon = Image.open('temp\\skateman.ico')

# 設置圖標的新大小 (例如設置為 QR 碼大小的 1/4)
factor = 4
icon_width = width // factor
icon_height = height // factor
icon = icon.resize((icon_width, icon_height), Image.Resampling.LANCZOS)  

# 計算圖標放置的位置
position = ((width - icon_width) // 2, (height - icon_height) // 2)
img.paste(icon, position)
# img.paste(icon, position, icon) #.ico 透明度
img.save("temp\\pictQRcode.jpg")

"""
img：QR 碼的圖像對象。
icon：要粘貼的圖標圖片。
position：一個二元組 (x, y)，指定 icon 在 img 上的位置，即圖標的左上角應該粘貼到 img 的哪個位置。
第三個參數 icon：這個參數指定了一個掩碼，這裡我們使用 icon 自身作為掩碼。這意味著 icon 的透明部分將被保留，而非透明部分將被粘貼到 img 上。
"""

print("----------------------------------------", 'demo-text in qrcode', "-"*40)
# import qrcode
# vc_str = '''
# BEGIN:VCARD
# FN:Tzu-chien Tseng
# TEL;CELL:0933117508
# TEL;FAX:04-22553007
# EMAIL:tzuchientseng@gmail.com
# URL:https://tzuchientseng.github.io/sunny.github.io/
# ADR:Taichung
# END:VCARD
# '''
# img = qrcode.make(vc_str)
# img.save('temp/TextQRcode.jpg')
import qrcode
from PIL import Image

# vCard string
vc_str = '''
BEGIN:VCARD
FN:Tzu-chien Tseng
TEL;CELL:0933117508
TEL;FAX:04-22553007
EMAIL:tzuchientseng@gmail.com
URL:https://tzuchientseng.github.io/sunny.github.io/
ADR:Taichung
END:VCARD
'''

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Use high error correction to allow for embedding image
    box_size=10,
    border=4,
)

qr.add_data(vc_str)
qr.make(fit=True)
# Generate QR code image with specified colors
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
# Open the icon image
icon = Image.open('temp/line.png')
# Calculate the size of the icon to be embedded
img_width, img_height = img.size
icon_size = img_width // 2
icon = icon.resize((icon_size, icon_size), Image.Resampling.LANCZOS)
icon = icon.convert("RGBA")
icon_position = ((img_width - icon_size) // 2, (img_height - icon_size) // 2)
icon_mask = icon.split()[3] 
img.paste(icon, icon_position, icon_mask)
img.save('temp/TextQRcode.jpg')
"""
print("----------------------------------------", 'demo-Tesseract OCR(Optical Character Recognition)', "-"*40)
from PIL import Image
import pytesseract
text = pytesseract.image_to_string(Image.open('temp\\images.jpg'))
print(type(text), "  ", text)

print("----------------------------------------", 'demo-car demo', "-"*40)
from PIL import Image
import pytesseract
import time
carDict = {}
myPath = "    "
while True:
    carPlate = input("--scan--('q' to quit)")
    if carPlate == 'Q' or carPlate == 'q':
        break
    carPlate = myPath + carPlate
    keyText = pytesseract.image_to_string(Image.open(carPlate))
    if keyText in carDict:
        exitTime = time.asctime()
        print("Car enter time: ", keyText, ':', exitTime)
        del carDict[keyText]
    else:
        entryTime = time.asctime()
        print("Car out time: ", keyText, ':', entryTime)
        carDict[keyText] = entryTime

print("----------------------------------------", 'demo-recognize chinese', "-"*40)
from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('     '), 
                                   lang='chi_tra')
print(text)
with open('     ', 'w', encoding='utf-8') as fn:
    fn.write(text)
"""
