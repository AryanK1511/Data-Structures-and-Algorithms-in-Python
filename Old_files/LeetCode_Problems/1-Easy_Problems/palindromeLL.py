# ========== EASY ==========
# Link: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ""
        curr = head
        while curr:
            s += str(curr.val)
            curr = curr.next

        if s == s[::-1]:
            return True
        else:
            return False