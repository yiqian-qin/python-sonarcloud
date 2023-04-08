'''Average Value of Even Numbers That Are Divisible by Three

Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.

Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000'''


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                ans += nums[i]
                count += 1
        return ans // count if count else 0
