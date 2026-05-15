# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head



        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        


        prev,cur = None, slow.next
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        res = head

        first, second = head, prev
        while second:
            temp = first.next
            temp1 = second.next

            first.next = second
            second.next = temp

            first = temp
            second = temp1
