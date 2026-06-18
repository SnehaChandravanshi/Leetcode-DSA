# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        def helper(s, e):
            if s > e:
                return None
            m = s + (e-s) // 2
            node = TreeNode(l[m])
            node.left = helper(s, m-1)
            node.right = helper(m+1, e)
            return node
        return helper(0, len(l)-1)
    