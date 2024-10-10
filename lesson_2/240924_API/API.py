"""
API 查詢系統
使用策略模式(Strategy Pattern)替代if-else與switch
1. Apple_stock_API
"""
from abc import ABC, abstractmethod  # "Abstract Base Classes"（抽象基類）
from Apple_stock_API import AppleStock  # 匯入自訂的 AppleStock 策略類別

# 抽象策略類別
class QueryStrategy(ABC):
    @abstractmethod
    def execute(self):  # abstract method 需要 override
        pass

# AppleStock 已經在 Apple_stock_API.py 中定義

class QueryStrategy2(QueryStrategy):
    def execute(self):
        print("執行策略 2 的查詢邏輯")

class QueryStrategy3(QueryStrategy):
    def execute(self):
        print("執行策略 3 的查詢邏輯")

class QueryStrategy4(QueryStrategy):
    def execute(self):
        print("執行策略 4 的查詢邏輯")

class QueryStrategy5(QueryStrategy):
    def execute(self):
        print("執行策略 5 的查詢邏輯")

# 查詢上下文，用來執行不同的策略
class QueryContext:
    def __init__(self, strategy: QueryStrategy):  # 型別註解（Type Annotation）
        self._strategy = strategy
    
    def set_strategy(self, strategy: QueryStrategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

def main():
    # 模擬 Java enum class，儲存不同的策略
    strategies = {
       '1': AppleStock(),  # 使用 Apple_stock_API 的策略類別
       '2': QueryStrategy2(),
       '3': QueryStrategy3(),
       '4': QueryStrategy4(),
       '5': QueryStrategy5(),
    }

    # 提示選單
    prompt_str = """
    Welcome API-query:
        0 -> quit
        1 -> 查詢 當日 Apple 股票
        2 -> 查詢策略 2
        3 -> 查詢策略 3
        4 -> 查詢策略 4
        5 -> 查詢策略 5
    """
    print(prompt_str)
    
    while (choice := input('Enter the number: ').strip()) != '0':
        try:
            if choice in strategies:
                context = QueryContext(strategies[choice])  # 建立策略上下文
                context.execute_strategy()  # 執行選擇的策略
            else:
                raise ValueError("Invalid number entered.")
        except ValueError as e:        
            print(f'Error: {e}. Please enter a valid number!')

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()

