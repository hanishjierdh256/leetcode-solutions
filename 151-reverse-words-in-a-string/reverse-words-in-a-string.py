class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        revlist = []
        for i in range(len(slist)):
            revlist.insert(0, slist[i])
        return " ".join(revlist)