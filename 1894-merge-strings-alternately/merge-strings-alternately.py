class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        icut = min(len(word1), len(word2))
        for i in range(icut):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.append(word1[icut:]) if len(word1) > len(word2) else merged.append(word2[icut:])
        return "".join(merged)
        