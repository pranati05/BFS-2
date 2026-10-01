# Time Complexity : O(N)
# Space Complexity : O(D)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using BFS. Initialize a queue containing root as a node inside the queue.
# Iterate over the queue until it is not empty
# We need a size variable and then iterate over the size of the queue and pop the node and push its left and right child to the queue
# Only append the last node value of each level to res by having condition if size - 1 == i


from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
# BFS

class Solution:
    def rightSideView(self, root: TreeNode | None) -> List[int]:
        res = []
        if not root:
            return res

        self.helper(root, 0, res)
        return res

    def helper(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append(root.val)
        self.helper(root.right, level + 1, res)
        self.helper(root.left, level + 1, res)     

        