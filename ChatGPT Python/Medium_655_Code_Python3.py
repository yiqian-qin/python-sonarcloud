
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_height(node):
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        def update_res(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.res[row][mid] = str(node.val)
            update_res(node.left, row+1, left, mid-1)
            update_res(node.right, row+1, mid+1, right)

        height = get_height(root)
        width = 2**height - 1
        self.res = [[""] * width for _ in range(height)]
        update_res(root, 0, 0, width-1)
        return self.res
