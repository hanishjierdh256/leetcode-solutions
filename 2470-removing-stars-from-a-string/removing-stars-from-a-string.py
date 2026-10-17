class Solution:
    def removeStars(self, s: str) -> str:
        list1 = []
        counter = 0
        for i in range(len(s)):
            if s[i] == "*":
                list1.pop()
            else:
                list1.append(s[i])
        return "".join(list1)
