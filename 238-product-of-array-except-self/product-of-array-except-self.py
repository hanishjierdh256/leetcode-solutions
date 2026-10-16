class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        leftproduct = [1] * len(nums)
        rightproduct = [1] * len(nums)
        nums.insert(0, 1)
        nums.insert(len(nums), 1)
        answer = []
        numsreverse = nums[::-1]
        for i in range (1, len(nums)-2):
            leftproduct[i] = nums[i] * leftproduct[i-1]
            rightproduct[i] = numsreverse[i] * rightproduct[i-1]
        rightproduct.reverse()
        for i in range (0, len(leftproduct)):
            answer.append(leftproduct[i] * rightproduct[i])
        return answer
