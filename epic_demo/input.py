"""
在 Python 中，如果你想透過系統命令行傳遞變數（類似於在 Java 中運行 fileName.java a b），你可以使用 sys.argv 來獲取命令行參數。以下是一個範例，展示了如何透過命令行參數傳遞變數給 Python 腳本：

創建一個 Python 腳本（例如 script.py），內容如下：
python
Copy code
import sys

def main():
    # 獲取命令行參數
    args = sys.argv[1:]  # sys.argv[0] 是腳本名，其他的是傳遞的參數
    
    if len(args) < 2:
        print("Usage: script.py <arg1> <arg2>")
        return
    
    arg1 = args[0]
    arg2 = args[1]
    
    # 打印傳遞的參數
    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")

if __name__ == "__main__":
    main()
在命令提示符（cmd）中運行該腳本，傳遞參數給它：
sh
Copy code
python script.py a b
此時，script.py 將接收到兩個參數 a 和 b，並輸出：

less
Copy code
Argument 1: a
Argument 2: b
將輸出重定向到文件
如果你想將輸出保存到文件中，可以使用重定向符號 >。例如：

sh
Copy code
python script.py a b > output.txt
這樣，腳本的輸出將被保存到 output.txt 文件中。

設置命令提示符編碼為 UTF-8
如果你需要在命令提示符中處理中文目錄或文件名，可以先設置編碼為 UTF-8：

sh
Copy code
chcp 65001
"""
