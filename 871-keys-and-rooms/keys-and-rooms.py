from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = {0}
        queue = deque([0])
        while queue:
            for i in range(len(queue)):
                innerList = rooms[queue[0]]
                for j in range(len(innerList)):
                    if innerList[j] not in visited:
                        visited.add(innerList[j])
                        queue.append(innerList[j])
                queue.popleft()
        
        return True if len(visited) == len(rooms) else False
                



