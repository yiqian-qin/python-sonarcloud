
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level, max_sum, max_level = 1, float('-inf'), 1
        queue = [root]
        while queue:
            level_sum = sum(node.val for node in queue)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return max_level
