# 先下載二支必要程式
# langconv.py http://mahaljsp.asuscomm.com/files/langconv.py
# zh_wiki.py http://mahaljsp.asuscomm.com/files/zh_wiki.py
import codecs # Coders + Decoders
from langconv import Converter
def convert(target, ls):
    for l in ls:
        # zh-hant : 轉繁体字
        # zh-hans : 轉簡体字
        zhContent = Converter('zh-hant').convert(l)
        print(zhContent, end="")
        target.write(zhContent)
files = ['train','test']
count = []
for file in files:
    source = codecs.open(f'{file}.csv','r', 'utf-8')
    target = codecs.open(f'{file}_tc.csv','w', 'utf-8')
    lines = source.readlines()
    count.append(len(lines))
    convert(target, lines)
    target.close()
    source.close()
print(f"總筆數 : {count}")
