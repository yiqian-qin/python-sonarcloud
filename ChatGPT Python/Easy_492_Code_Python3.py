
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        sqrt_area = int(math.sqrt(area)) # square root of area. Convert to an integer.
        while area % sqrt_area != 0: # keep decrementing until it is divisible by the sqrt_area
            sqrt_area -= 1
        return [area // sqrt_area, sqrt_area] # return the length and width
