class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rights = {"R":[], "D":[]}
        i = 0
        for i, senator in enumerate(senate):
            if senator == "R":
                rights["R"].append(i)
            else:
                rights["D"].append(i)
        n = len(senate)
        while len(rights["D"]) != 0 and len(rights["R"]) != 0:
            if rights["R"][0] < rights["D"][0]:
                rights["D"].pop(0)
                rights["R"].pop(0)
                rights["R"].append(n)
                n = n + 1
            else:
                rights["R"].pop(0)
                rights["D"].pop(0)
                rights["D"].append(n)
                n = n + 1
        return "Radiant" if len(rights["D"]) == 0 else "Dire"
        



            
        