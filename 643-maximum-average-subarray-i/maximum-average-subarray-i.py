class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        lastaverage = sum(nums[0:k])/k
        maxaverage = sum(nums[0:k])/k
        for i in range(1, len(nums)-k+1):
            lastaverage = lastaverage - nums[i-1]/k + nums[i+k - 1]/k
            maxaverage = max(maxaverage, lastaverage)
        return maxaverage
            
