class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiouAEIOU"
        sbool = [False] * len(s)
        for i in range(len(s)):
            sbool[i] = True if s[i] in vowels else False
        windowsum = sum(sbool[:k])
        maxvowel = windowsum
        n = len(sbool)
        for i in range(k, len(sbool)):
            windowsum = windowsum - sbool[i-k] + sbool[i]
            maxvowel = max(maxvowel,windowsum)
            if maxvowel == k:
                return maxvowel
        return maxvowel