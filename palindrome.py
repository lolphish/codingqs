class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len, low = 0, 0
        
        def helper(i, j):
            nonlocal max_len, low
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
            if j-i-1 > max_len:
                max_len, low = j-i-1, i+1
        
        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)
        return s[low: low+max_len]