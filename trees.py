# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive valid BST
class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        st = deque()
        pre = None
        while root != null or stack:
            while root != null:
                st.append(root)
                root = root.left
            
# stack method (can be applied to other problems)
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        st = deque()
        pre = None
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True


# check if tree t is a subtree of s
def isSubtree(s, t):
    if not s: return False
    if isSame(s,t): return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)

def isSame(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)