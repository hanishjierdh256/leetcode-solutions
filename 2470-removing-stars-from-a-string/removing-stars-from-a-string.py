class Solution:
    def removeStars(self, s: str) -> str:
        list1 = []
        for c in s:
            if c == "*":
                list1.pop()
            else:
                list1.append(c)
        return "".join(list1)
