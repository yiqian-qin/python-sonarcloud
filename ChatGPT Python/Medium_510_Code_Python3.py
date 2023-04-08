
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # if node has a right child, find and return the leftmost child of the right child
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        # if node doesn't have a right child, find the first ancestor whose left child is also an ancestor of node
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
