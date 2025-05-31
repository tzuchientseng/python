"""
class ListNode {
    int val;
    ListNode next;
    
    ListNode() {}
    
    ListNode(int val) {
        this.val = val;
    }
    
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p, q, curr = l1, l2, dummyHead
        carry = 0
        
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            _sum = carry + x + y
            carry = _sum // 10
            curr.next = ListNode(_sum % 10)
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummyHead.next

def main():
    # Test cases
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result is not None:
        print(result.val, end=" ")
        result = result.next
    print()

    l3 = ListNode(0)
    l4 = ListNode(0)
    result2 = solution.addTwoNumbers(l3, l4)
    while result2 is not None:
        print(result2.val, end=" ")
        result2 = result2.next
    print()

    l5 = ListNode(9)
    l5.next = ListNode(9)
    l5.next.next = ListNode(9)
    l5.next.next.next = ListNode(9)
    l5.next.next.next.next = ListNode(9)
    l5.next.next.next.next.next = ListNode(9)
    l5.next.next.next.next.next.next = ListNode(9)

    l6 = ListNode(9)
    l6.next = ListNode(9)
    l6.next.next = ListNode(9)
    l6.next.next.next = ListNode(9)

    result3 = solution.addTwoNumbers(l5, l6)
    while result3 is not None:
        print(result3.val, end=" ")
        result3 = result3.next
    print()

if __name__ == "__main__":
    main()
