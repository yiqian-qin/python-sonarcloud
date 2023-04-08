## Binary search approach

## Time Complexity: O(n log n)
## Space Complexity: O(1)

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        
        while left <= right:
            mid = (left + right) // 2
            count, prev = 1, position[0]
            
            for i in range(1, len(position)):
                if position[i] - prev >= mid:
                    count += 1
                    prev = position[i]
            
            if count >= m:
                left = mid + 1
            else:
                right = mid - 1
        
        return right