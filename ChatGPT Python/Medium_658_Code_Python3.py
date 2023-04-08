# We are given a sorted array and a point x, and we have to find k closest elements from the array


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # Binary search for finding the index, which is closest to the given x
        # Lower bound will be the left-most index, which will be closest to x
        # Upper bound will be the right most index, closest to x
        
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
                
        # Initializing two pointers
        
        low = left - 1
        high = left
        
        # Loop until k closest elements are found
        
        while k:
            if low < 0:
                high += 1  
            elif high == len(arr) or abs(arr[low] - x) <= abs(arr[high] - x):
                low -= 1
            else:
                high += 1 
            k -= 1
                
        return arr[low+1:high]