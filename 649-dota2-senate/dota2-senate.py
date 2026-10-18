class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        dire = []
        radiant = []
        for i in range (len(senate)):
            if senate[i] == "D":
                dire.append(i)
            else:
                radiant.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                dire.pop(0)
                radiant.append(radiant.pop(0) + n)
            else:
                radiant.pop(0)
                dire.append(dire.pop(0) + n)
        return "Radiant" if len(dire) == 0 else "Dire"