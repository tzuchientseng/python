"""
print("----------------------------------------", 'demo-(ListNode+LinkedList)', "-"*40)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
print("----------------------------------------", 'demo-List Node', "-"*40)
class Node():
    """Node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n1.next = n2
n2.next = n3
ptr = n1
while ptr:
    print(ptr.data)
    ptr = ptr.next

print("----------------------------------------", 'demo-Linked_list', "-"*40)
class Node():
    """Node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Linked_list():
    """Linked_list"""
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()

print("----------------------------------------", 'demo-Adding node at begining', "-"*40)
class Node():
    """Node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Linked_list():
    """Linked_list"""
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def begining(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

link = Linked_list()
link.head = Node(5)
n2 = Node(10)
n3 = Node(15)
link.head.next = n2
n2.next = n3
link.print_list()
print("New head Linked list")
link.begining(100)
link.print_list()

print("----------------------------------------", 'demo-Adding node at ending', "-"*40)
class Node:
    """節點"""
    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標

class Linked_List:
    """鏈結串列"""
    def __init__(self):
        self.head = None  # 鍵結串列第 1 個節點

    def print_list(self):
        """列印鏈結串列"""
        ptr = self.head  # 指標指向鏈結串列第1個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def append(self, new_data):
        """在串列尾部插入新節點"""
        new_node = Node(new_data)  # 建立新節點
        if self.head is None:  # 如果是空的，表示鏈結串列是空的
            self.head = new_node  # 所以head就可以直接指向此新節點
            return
        last_ptr = self.head  # 確定最後指標是鏈結串列頭部
        while last_ptr.next:  # 移動指標直到最後
            last_ptr = last_ptr.next
        last_ptr.next = new_node  # 將最後一個節點的指標指向新節點

# 測試鏈結串列
link = Linked_List()
link.head = Node(5)  # 節點1
n2 = Node(15)  # 節點2
n3 = Node(25)  # 節點3
link.head.next = n2  # 節點1指向節點2
n2.next = n3  # 節點2指向節點3

# 列印鏈結串列
link.print_list()

print("新的鏈結串列")
link.append(168)  # 插入新的節點
link.print_list()  # 列印新的鏈結串列

print("----------------------------------------", 'demo-insert new node', "-"*40)
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None # 自定義的屬性，用於存儲下一個節點的地址

class LinkedList:
    def __init__(self) -> None:
        self.head = None  # First node
    
    def print_list(self):
        ptr = self.head  # point to head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    
    def between(self, pre_node, newdata):
        '''Insert a new node between two nodes'''
        if pre_node is None:
            print("Previous node is missing")
            return
        # Create and insert new node
        new_node = Node(newdata)
        new_node.next = pre_node.next  # New node points to the next node of pre_node
        pre_node.next = new_node  # pre_node points to the new node

# Create linked list and nodes
link = LinkedList()
link.head = Node(5)  # Node 1
n2 = Node(15)  # Node 2
n3 = Node(25)  # Node 3

link.head.next = n2  # Node 1 points to Node 2
n2.next = n3  # Node 2 points to Node 3

# Print initial linked list
link.print_list()

print("New linked list")
# Insert new node after n2
link.between(n2, 100)

# Print updated linked list
link.print_list()

print("----------------------------------------", 'demo-Remove the node', "-"*40)
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None # 自定義的屬性，用於存儲下一個節點的地址

class LinkedList:
    def __init__(self) -> None:
        self.head = None  # First node
    
    def print_list(self):
        ptr = self.head  # point to head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def append(self, new_data):
        """在串列尾部插入新節點"""
        new_node = Node(new_data)  # 建立新節點
        if self.head is None:  # 如果是空的，表示鏈結串列是空的
            self.head = new_node  # 所以head就可以直接指向此新節點
            return
        last_ptr = self.head  # 確定最後指標是鏈結串列頭部
        while last_ptr.next:  # 移動指標直到最後
            last_ptr = last_ptr.next
        last_ptr.next = new_node  # 將最後一個節點的指標指向新節點
    
    def rm_node(self, rmkey):
        # Temporary pointer
        ptr = self.head

        # If head node itself holds the key to be deleted
        if ptr and ptr.data == rmkey:
            self.head = ptr.next
            return

        # Search for the key to be deleted, keep track of the previous node
        while ptr:
            if ptr.data == rmkey:
                break
            prev = ptr
            ptr = ptr.next
        
        # If key was not present in the linked list
        if ptr is None:
            return

        # Unlink the node from the linked list
        prev.next = ptr.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create linked list and add elements
link = LinkedList()
link.ending(5)
link.ending(15)
link.ending(25)

# Print the linked list
print("Initial linked list:")
link.print_list()

# Remove the node with value 15
link.rm_node(15)

# Print the updated linked list
print("Linked list after removing node with value 15:")
link.print_list()

print("----------------------------------------", 'demo-Cyclic linked_list', "-"*40)
class Node:
    # 節點
    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標

n1 = Node(5)
n2 = Node(15)
n3 = Node(25)

n1.next = n2  # 節點 1 指向節點 2
n2.next = n3  # 節點 2 指向節點 3
n3.next = n1  # 末端節點指向起始節點

ptr = n1  # 建立指標節點
counter = 1

while counter <= 6:
    print(ptr.data)  # 列印節點
    ptr = ptr.next  # 移動指標到下一個節點
    counter += 1

print("----------------------------------------", 'demo-Doubly linked list', "-"*40)
class Node:
    '''節點'''
    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 向後指標
        self.previous = None  # 向前指標

class DoubleLinkedList:
    '''雙向鏈結串列'''
    def __init__(self):
        self.head = None  # 鏈結串列頭部的節點
        self.tail = None  # 鏈結串列尾部的節點

    def add_double_list(self, new_node):
        '''將節點加入雙向鏈結串列'''
        if isinstance(new_node, Node):
            if self.head == None:  # 先確定這item是節點
                self.head = new_node  # 頭是new_node
                new_node.previous = None  # 指向前方
                new_node.next = None  # 指向後方
                self.tail = new_node  # 尾節點也是new_node
            else:  # 處理雙向鏈結串列不是空的
                self.tail.next = new_node  # 尾節點指標指向new_node
                new_node.previous = self.tail  # 新節點前方指標指向先前尾節點
                self.tail = new_node  # 新節點成為尾節點
        return

    def print_list_from_head(self):
        '''從頭部列印雙向鏈結串列'''
        ptr = self.head  # 指標指向鏈結串列第1個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def print_list_from_tail(self):
        '''從尾部列印雙向鏈結串列'''
        ptr = self.tail  # 指標指向鏈結串列尾部的節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.previous  # 移動指標到前一個節點

# 建立節點
n1 = Node(5)  # 節點 1
n2 = Node(15)  # 節點 2
n3 = Node(25)  # 節點 3

# 建立雙向鏈結串列並加入節點
double_link = DoubleLinkedList()
for n in [n1, n2, n3]:
    double_link.add_double_list(n)

# 從頭部列印雙向鏈結串列
print("從頭部列印雙向鏈結串列")
double_link.print_list_from_head()

# 從尾部列印雙向鏈結串列
print("從尾部列印雙向鏈結串列")
double_link.print_list_from_tail()

print("----------------------------------------", 'demo-HW', "-"*40)
