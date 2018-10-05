'''
Reverse a List
'''
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev

def reverseList(head):
    return helper(head)

def helper(node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return helper(n, node) 