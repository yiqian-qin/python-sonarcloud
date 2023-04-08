# Define the TreeNode class with val, left, and right attributes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Define the method to recursively construct the BST
    def constructBST(self, nums, low, high):
        # Base case: return None when low > high
        if low > high:
            return None
        
        # Find the middle element and set it as the root
        mid = (low + high) // 2
        root = TreeNode(nums[mid])
        
        # Recursively construct the left and right subtrees
        root.left = self.constructBST(nums, low, mid - 1)
        root.right = self.constructBST(nums, mid + 1, high)
        
        # Return the root
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Call the recursive function to construct the BST
        return self.constructBST(nums, 0, len(nums) - 1)