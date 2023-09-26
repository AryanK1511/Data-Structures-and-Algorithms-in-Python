# ========== EASY ==========
# Link: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        l1_curr_ptr = list1
        l2_curr_ptr = list2
        curr = mergedList

        while l1_curr_ptr is not None and l2_curr_ptr is not None:
            if l1_curr_ptr.val <= l2_curr_ptr.val:
                curr.next = l1_curr_ptr
                l1_curr_ptr = l1_curr_ptr.next
            else:
                curr.next = l2_curr_ptr
                l2_curr_ptr = l2_curr_ptr.next
            curr = curr.next

        if l1_curr_ptr is not None:
            curr.next = l1_curr_ptr
        elif l2_curr_ptr is not None:
            curr.next = l2_curr_ptr
        
        return mergedList.next
        
