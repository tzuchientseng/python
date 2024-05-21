import sys

# 獲取命令行參數列表
arguments = sys.argv

# 第一個參數是腳本本身的名稱，所以實際的參數從第二個開始
if len(arguments) > 1:
    user_input = arguments[1]
    print("系統輸入:", user_input)
else:
    print("請在命令行中輸入參數")
