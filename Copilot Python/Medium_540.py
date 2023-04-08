'''Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # O(n) time, O(1) space
        # for i in range(0, len(nums), 2):
        #     if i == len(nums) - 1:
        #         return nums[i]
        #     if nums[i] != nums[i+1]:
        #         return nums[i]

        # O(log n) time, O(1) space
        # binary search
        # if len(nums) == 1:
        #     return nums[0]
        # if nums[0] != nums[1]:
        #     return nums[0]
        # if nums[-1] != nums[-2]:
        #     return nums[-1]
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
        #         return nums[mid]
        #     if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return nums[left]

        # O(log n) time, O(1) space
        # binary search
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid+1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
