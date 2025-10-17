# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not (head.next):
            return 0
        # Length of LinkedList
        n = 0
        curr = head
        while curr:
            n = n + 1
            curr = curr.next
        
        m = int (n // 2)

        maxTwinSum = float(-inf)

        #Reverse the linked list from middle:
        prev = None
        curr = head
        i = 0
        while i < m:
            curr = curr.next
            i = i + 1
        
        if n % 2 != 0:
            curr = curr.next

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        revHead = prev

        twinSum = float(-inf)
        i = 0
        while i < m:
            twinSum = max(twinSum, head.val + revHead.val)
            head = head.next
            revHead = revHead.next
            i += 1
        
        return twinSum
        
        

        


        
        
        
