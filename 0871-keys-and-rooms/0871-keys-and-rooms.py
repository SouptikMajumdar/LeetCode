class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        currKeys = {0: 0, -1: -1}
        toVisit = 0
        while len(set(currKeys.values())) != 1:
            if -1 in currKeys:
                currKeys.pop(-1)

            newKeys = rooms[toVisit]
            if len(currKeys.keys()) == len(rooms):
                break
            
            for key in newKeys:
                if key not in currKeys: 
                    currKeys[key] = 0
            
            currKeys[toVisit] = 1
            toVisit = list(filter(lambda key: currKeys[key] == 0, currKeys))
            if len(toVisit) != 0:
                toVisit = toVisit[0]
            else:
                break
            
        return len(currKeys) == len(rooms)