class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxaltitude = 0
        currentaltitude = 0
        for i in range(len(gain)):
            currentaltitude = gain[i] + currentaltitude
            maxaltitude = max(maxaltitude,currentaltitude)
        return maxaltitude