class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0
        maxnum = 0
        for i in range (len(nums)):
            if (nums[i] == 0):
                zeros += 1
            while (zeros > 1):
                if (nums[left] == 0):
                    zeros -= 1
                left += 1
            maxnum = max(i - left,maxnum)
        return maxnum