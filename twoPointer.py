# trapping rain water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftCursor, rightCursor = 0, len(height) - 1
        leftMax, rightMax, storedWater = 0, 0, 0

        while (leftCursor <= rightCursor):
            leftMax = max(leftMax, height[leftCursor])
            rightMax = max(rightMax, height[rightCursor])
            if leftMax < rightMax:
                storedWater += leftMax - height[leftCursor]
                leftCursor += 1
            else:
                storedWater += rightMax - height[rightCursor]
                rightCursor -= 1

        return s