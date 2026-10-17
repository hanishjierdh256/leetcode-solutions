class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        slist = list(s)
        scounter = 0
        for i in range(len(t)):
            if scounter < len(slist) and t[i] == slist[scounter]:
                scounter += 1
        return True if len(slist) == scounter else False