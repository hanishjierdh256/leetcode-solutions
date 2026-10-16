class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        vowel = "aeiouAEIOU"
        for i in range (len(s)):
            if s[i] in vowel:
                vowels.append(s[i])
        vowelnum = len(vowels)-1
        ans = []
        for i in range (len(s)):
            if s[i] in vowel:
                ans.append(vowels[vowelnum])
                vowelnum += -1
            else:
                ans.append(s[i])
        return "".join(ans)