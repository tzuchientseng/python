"""
使用策略模式(Strategy Pattern)替代if-else與switch
1. 當需要新增或修改查詢行為（策略）時，只需新增或修改對應的策略類別，而不需要更改主邏輯。這符合開放-封閉原則（Open-Closed Principle），即程式對擴展開放、對修改封閉。
2. 每個策略類別只負責一件事，即實現某一特定的查詢邏輯。這樣的設計使得每個類別的職責單一且清晰，符合單一職責原則（Single Responsibility Principle）。
---

# API 查詢系統
=> 策略方法
0 -> quit
1 -> 查詢所有名稱 
2 -> 查詢台北市結婚110年年齡分布
3 -> 查詢台北市結婚110年教育程度分布
4 -> 查詢台北市結婚110年年齡+教育程度分布
5 -> 查詢台北市離婚111年教育程度分布
6 -> 新策略
---
"""
from abc import ABC, abstractmethod  # "Abstract Base Classes"（抽象基類）
# 匯入自訂的 策略類別
from API_1 import All_tags
from API_2 import Age_Marrige
from API_3 import Edu_Marrige
from API_4 import Age_Edu_Marrige
from API_5 import Edu_Divorce

# 抽象策略類別
class QueryStrategy(ABC):
    @abstractmethod
    def execute(self):  # abstract method 需要 override
        pass
class QueryStrategy_toDo(QueryStrategy):
    def execute(self):
        print("---Not done yet---")

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
       '1': All_tags(),
       '2': Age_Marrige(),
       '3': Edu_Marrige(),
       '4': Age_Edu_Marrige(),
       '5': Edu_Divorce(),
       '6': QueryStrategy_toDo(),
    }

    # 提示選單
    prompt_str = """
---------------------------------------------------------------
        Welcome API-query:
            0 -> quit
            1 -> 查詢所有名稱 
            2 -> 查詢台北市結婚110年年齡分布
            3 -> 查詢台北市結婚110年教育程度分布
            4 -> 查詢台北市結婚110年年齡+教育程度分布
            5 -> 查詢台北市離婚111年教育程度分布
            6 -> 新策略
---------------------------------------------------------------
    """
    print(prompt_str)
    
    while (choice := input('Enter the number: ').strip()) != '0':
        try:
            if choice in strategies:
                context = QueryContext(strategies[choice])  # 建立策略上下文
                context.execute_strategy()  # 執行選擇的策略

                print(prompt_str)
            else:
                raise ValueError("Invalid number entered.")
        except ValueError as e:        
            print(f'Error: {e}. Please enter a valid number!')

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
