from node import node

def longestConsecutive(root):
   return max(consecutiveDfs(root.left,root.val, 1), consecutiveDfs(root.right, root.val, 1)) if root else 0

def consecutiveDfs(node, parent, count):
   if not node:
      return count
   count = count + 1 if node.val-parent == 1 else 1
   return max([consecutiveDfs(node.left, node.val, count),consecutiveDfs(node.left, node.val, count), count])



def longestUnivaluePath(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # Time: O(n)
    # Space: O(n)
    longest = [0]

    def traverse(node):
        if not node:
            return 0
        left_len, right_len = traverse(node.left), traverse(node.right)
        left = (left_len + 1) if node.left and node.left.val == node.val else 0
        right = (right_len + 1) if node.right and node.right.val == node.val else 0
        longest[0] = max(longest[0], left + right)
        return max(left, right)

    traverse(root)
    return longest[0]
if __name__ == "__main__":
   a = node(1)
   a.right = node(3)
   a.right.left = node(2)
   a.right.right = node(4)
   a.right.right.right = node(5)
   print(a)
   print(longestConsecutive(a))