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
