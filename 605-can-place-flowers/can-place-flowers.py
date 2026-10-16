class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed2 = [0]
        flowerbed2 += flowerbed
        flowerbed2.append(0)
        m = 0
        for i in range(1, len(flowerbed2)-1):
            if flowerbed2[i-1] == 0 and flowerbed2[i+1] == 0 and flowerbed2[i] == 0:
                m += 1
                flowerbed2[i] = 1
        return True if m >= n else False

        return flowerbed2