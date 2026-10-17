class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0) 
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] !=0:
                nums[index] = nums[i]
                index += 1
        for i in range(index,n):
            nums[i] = 0