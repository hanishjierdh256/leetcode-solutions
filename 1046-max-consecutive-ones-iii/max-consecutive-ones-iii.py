class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        maxnum = 0
        for i in range (len(nums)):
            if (nums[i] == 0):
                zeros += 1
            while (zeros > k):
                if (nums[left] == 0):
                    zeros -= 1
                left += 1
            maxnum = max(i - left + 1,maxnum)
        return maxnum