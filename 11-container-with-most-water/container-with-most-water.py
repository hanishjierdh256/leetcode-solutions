class Solution:
    def maxArea(self, height: list[int]) -> int:
        leftpointer = 0
        rightpointer = len(height)-1
        maxarea = 0
        while leftpointer != rightpointer:
            left = height[leftpointer]
            right = height[rightpointer]
            calcarea = min(left, right) * (rightpointer - leftpointer)
            maxarea = max(maxarea, calcarea)
            if left < right:
                leftpointer += 1  
            else: 
                rightpointer -= 1

        return maxarea
        