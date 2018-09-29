# 12345 = Twelve Thousand Three Hundred Fourty Five
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num or num <= 0:
            return "Zero"
        
        def helper(num):
            tens = ["","One","Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            twenties = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            hundreds = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            res = ""
            if num < 10:
                res = tens[num] + " "
            elif num < 20:
                res = twenties[num-10] + " "
            elif num < 100:
                res =  hundreds[num//10] + " " + helper(num%10)
            elif num < 1000:
                res = helper(num//100) + " Hundred " + helper(num%100)
            elif num < 1000000:
                res =  helper(num//1000) + " Thousand " + helper(num%1000)
            elif num < 1000000000:
                res = helper(num//1000000) + " Million " + helper(num%1000000)
            else:
                res = helper(num//1000000000) + " Billion " + helper(num%1000000000)
            return res.strip()
        
        return helper(num)
# Input: [0,1,0,3,12] --> Output: [1,3,12,0,0]
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index+=1
        
        while zero_index < len(nums):
            nums[zero_index] = 0
            zero_index+=1

# Given numbers, return k most frequent nums Input: nums = [1,1,1,2,2,3], k = 2 Output: [1,2]
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [key for key,val in Counter(nums).most_common(k)]