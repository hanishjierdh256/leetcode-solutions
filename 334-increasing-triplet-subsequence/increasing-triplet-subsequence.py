class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = nums[0]
        second = float('inf')
        flag = False
        for i in range (1, len(nums)):
            if nums[i] < first:
                first = nums[i]
            if nums[i] > first and nums[i] < second:
                second = nums[i]
                flag = True
            if nums[i] > first and nums[i] > second:
                return True
        return False
