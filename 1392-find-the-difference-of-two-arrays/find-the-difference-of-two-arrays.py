class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer1 = [num for num in set1 if num not in set2]
        answer2 = [num for num in set2 if num not in set1]
        return [answer1,answer2]