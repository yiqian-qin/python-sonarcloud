# Since the buildings with an ocean view can only be seen from the buildings to the right with a smaller height, we should iterate through the buildings from right to left and keep track of the maximum height we have seen so far. If the current building is higher than the maximum height we have seen so far, we add the index of that building to our result list and update our maximum height. Finally, we return the result list in reverse order to get the indices sorted in increasing order.

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        return res[::-1]