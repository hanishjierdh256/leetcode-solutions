class Solution:
    def reverseWords(self, s: str) -> str:
        s += " "
        sentence = []
        temp = []
        for i in range(len(s)):
            if s[i] not in " ":
                temp.append(s[i])
            else:
                sentence.insert(0, "".join(temp))
                temp = []
        sentence = [x for x in sentence if x != "" ]
        return " ".join(sentence)        