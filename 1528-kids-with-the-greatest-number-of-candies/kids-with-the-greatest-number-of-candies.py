class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        arr1 = []
        largest = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= largest:
                arr1.append(True)
            else:
                arr1.append(False)
        return arr1