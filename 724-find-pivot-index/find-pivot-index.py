class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        index = 0
        sumleft = 0
        sumright = total - nums[index]
        for i in range(1,len(nums)):
            if sumleft == sumright:
                return i - 1
            sumleft = sumleft + nums[i-1]
            sumright = sumright - nums[i]
            index = i
        if sumleft == sumright:
            return index
        return -1