# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        d = ListNode(0)
        l3 = d
        
        carry = 0
        while l1 != None and l2 != None:
            value = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            
            l3.next = ListNode(value) 
            l3 = l3.next

            l1 = l1.next                        
            l2 = l2.next
            

        while l1 != None:
            value = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            
            l3.next = ListNode(value) 
            l3 = l3.next
            l1 = l1.next
            
        while l2 != None:
            value = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            
            l3.next = ListNode(value)             
            l3 = l3.next
            l2 = l2.next
        
        if carry != 0:
            l3.next = ListNode(carry) 
            
            
        return d.next