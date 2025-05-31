# 策略模式（Strategy Pattern）
# "Abstract Base Classes"（抽象基類）
from abc import ABC, abstractmethod

# 定義一個查詢策略的抽象基類 (bass class)
class QueryStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# 定義多個具體的查詢策略
class QueryStrategy1(QueryStrategy):
    def execute(self):
        print("查詢功能 1 的資訊...")
        # 模擬呼叫 API 或顯示網頁資訊
        print("呼叫第 1 個 API 或顯示相關資訊")

class QueryStrategy2(QueryStrategy):
    def execute(self):
        print("查詢功能 2 的資訊...")
        # 模擬呼叫 API 或顯示網頁資訊
        print("呼叫第 2 個 API 或顯示相關資訊")

class QueryStrategy3(QueryStrategy):
    def execute(self):
        print("查詢功能 3 的資訊...")
        # 模擬呼叫 API 或顯示網頁資訊
        print("呼叫第 3 個 API 或顯示相關資訊")

class QueryStrategy4(QueryStrategy):
    def execute(self):
        print("查詢功能 4 的資訊...")
        # 模擬呼叫 API 或顯示網頁資訊
        print("呼叫第 4 個 API 或顯示相關資訊")

class QueryStrategy5(QueryStrategy):
    def execute(self):
        print("查詢功能 5 的資訊...")
        # 模擬呼叫 API 或顯示網頁資訊
        print("呼叫第 5 個 API 或顯示相關資訊")

# 定義一個上下文類來管理查詢策略
class QueryContext:
    def __init__(self, strategy: QueryStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: QueryStrategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

# 主程式
def main():
    print("歡迎光臨查詢系統")
    
    strategies = {
        "1": QueryStrategy1(),
        "2": QueryStrategy2(),
        "3": QueryStrategy3(),
        "4": QueryStrategy4(),
        "5": QueryStrategy5()
    }

    while True:
        print("\n請選擇要查詢的資訊：")
        print("0. 離開")
        for key in strategies:
            print(f"{key}. 查詢功能 {key}")
        
        choice = input("請輸入您的選擇: ").strip()

        if choice == "0":
            print("謝謝使用，再見！")
            break
        elif choice in strategies:
            context = QueryContext(strategies[choice])
            context.execute_strategy()
        else:
            print("無效的選擇，請再試一次。")

if __name__ == "__main__":
    main()

