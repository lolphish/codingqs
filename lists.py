from collections import defaultdict

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def mergeTwoLists(list1: ListNode, list2: ListNode):
    if not list1: return list2
    if not list2: return list1
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

def mergeKLists(self, lists):
    k = len(lists)
    q = PriorityQueue(maxsize=k)
    dummy = ListNode(None)
    curr = dummy
    for list_idx, node in enumerate(lists):
        if node: q.put((node.val, list_idx, node))
    while q.qsize() > 0:
        poped = q.get()
        curr.next, list_idx = poped[2], poped[1]
        curr = curr.next
        if curr.next: q.put((curr.next.val, list_idx, curr.next))
    return dummy.next

def reconstructQueue(people):
    if not people: return []
    ans = []
    for person in sorted(people, key=lambda x:(-x[0],x[-1])):
        ans.insert(person[1], person)
    return ans

def merge(self, intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out

# maximum subarray Input: [-2,1,-3,4,-1,2,1,-5,4], Output: 6, Explanation: [4,-1,2,1] has the largest sum = 6.
def maxSubArray(self, nums):
    if not nums: return 0
    maxSoFar = maxHere = nums[0]
    for i in range(1, len(nums)):
        maxHere = max(nums[i], maxHere+nums[i])
        maxSoFar = max(maxSoFar, maxHere)
    return maxSoFar

# maximum product
class Solution(object):
    def maxProduct(self, words):
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

'''
given an array of n integers, check if the array has two  
nearby duplicate numbers (meaning if a [2] = 3, 
Then check if 3 occurs at most two positions after.
'''
def duplicate_numbers(l:list):
    d, res = defaultdict(), []
    for i, num in enumerate(l):
        if num in d and i-d[num] <2:
            res.append(num)
        d[num] = i
    return res

'''
Given [[0, 30],[5, 10],[15, 20]],
return 2.
'''
def minMeetingRooms(self, intervals):
    starts = sorted(i.start for i in intervals)
    ends = sorted(i.end for i in intervals)

    e = 0
    numRooms = available = 0
    for start in starts:
        while ends[e] <= start:
            available += 1
            e += 1
        if available:
            available -= 1
        else:
            numRooms += 1

    return numRooms


'''
output contest matches
Input: 8
Output: (((1,8),(4,5)),((2,7),(3,6)))
Explanation: 
First round: (1,8),(2,7),(3,6),(4,5)
Second round: ((1,8),(4,5)),((2,7),(3,6))
Third round: (((1,8),(4,5)),((2,7),(3,6)))
Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).

'''
def findContestMatch(self, n):
    R = tuple(range(1, n+1))
    while len(R) > 2:
        R = tuple((R[i],R[~i]) for i in xrange(len(R)/2))
    return str(R).replace(' ','')

'''
wiggle sort

'''
class Solution(object):
    def wiggleSort(self, a):
        if not a:
            return
        n = len(a)
        for i in range(1, n, 2):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]

            if i + 1 < n and a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]



'''
plus one linked list
Input:
1->2->3

Output:
1->2->4

'''


def plusOne(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    start = None

    node = head
    while node:
        if node.val < 9:
            start = node
        node = node.next

    if start:
        start.val += 1
        node = start.next
    else:
        new = ListNode(1)
        new.next = head
        node = head
        head = new

    while node:
        node.val = 0
        node = node.next

    return head

'''
ax^2 + bx + c
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]

'''
def sortTransformedArray(self, nums, a, b, c):
    nums = [x*x*a + x*b + c for x in nums]
    ret = [0] * len(nums)
    p1, p2 = 0, len(nums) - 1
    i, d = (p1, 1) if a < 0 else (p2, -1)
    while p1 <= p2:
        if nums[p1] * -d > nums[p2] * -d:
            ret[i] = nums[p1]
            p1 += 1
        else:
            ret[i] = nums[p2]
            p2 -=1
        i += d
    return ret


'''
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''
def findMissingRanges(self, A, lower, upper):
    result = []
    A.append(upper + 1)
    pre = lower - 1
    for i in A:
        if (i == pre + 2):
            result.append(str(i - 1))
        elif (i > pre + 2):
            result.append(str(pre + 1) + "->" + str(i - 1))
        pre = i
    return result
if __name__ == "__main__":
    a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(reconstructQueue(a))

    arr = [1, 2, 5, 3, 4, 5, 6, 5, 4, 6, 6, 5, 5]
    print(duplicate_numbers(arr))



    