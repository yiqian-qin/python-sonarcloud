# Solution using BFS( breath first search)

class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 1)])
        visited = set([(0, 1)])
        level = 0
        
        while queue:
            size = len(queue)
            for i in range(size):
                pos, speed = queue.popleft()
                
                if pos == target:
                    return level
                
                # action accelerate
                np, ns = pos+speed, speed*2
                if (np, ns) not in visited and np > 0:
                    queue.append((np, ns))
                    visited.add((np, ns))
                
                # action reverse
                np, ns = pos, -1 if speed > 0 else 1
                if (np, ns) not in visited:
                    queue.append((np, ns))
                    visited.add((np, ns))
                    
            level += 1