
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        
        def traverse(node, curr_path):
            if not node:
                return
            
            # Add current node to the path
            curr_path += str(node.val)
            
            # If node is a leaf, add path to the result
            if not node.left and not node.right:
                paths.append(curr_path)
                return
            
            # Traverse left and right children, passing updated path
            traverse(node.left, curr_path + "->")
            traverse(node.right, curr_path + "->")
            
        traverse(root, "")
        return paths
