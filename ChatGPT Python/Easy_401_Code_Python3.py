
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(n: int) -> int: # Function to count number of bits that are 1 in an integer
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        # Looping through all possible combinations of hours and minutes and adding to result list if number of on bits is equal to turnedOn
        res = []
        for h in range(0, 12):
            for m in range(0, 60):
                if count_bits(h) + count_bits(m) == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
