# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using BFS. Initialize a queue with root node and parent is None
# Iterate over the queue until not empty and then iterate over the size of the queue and pop the node in the queue
# Then check if the node value == x or node value == y and parent is not None then found_x will be True and found_y will be True
# Check if the nodes left and right are not None and if the node.left is x or y and node.right is x or y then return False because they would have the same parent
# Then append the node left and right to queue and parent as node
# Once we iterate that level we check if both x and y are found at that level then we return True if only one is found we return False because the cousins need to be at same level
# Return False in the end


from collections import deque
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        queue = deque([(root, None)])
        while queue:
            size = len(queue)
            found_x = False
            found_y = False
            for i in range(size):
                node, parent = queue.popleft()
                if node.val == x:
                    found_x = True
                if node.val == y:
                    found_y = True
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            if found_x and found_y:
                return True
            if found_x or found_y:
                return False 
        return False
# BFS

class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y:int) -> bool:
        self.level_x = -1
        self.level_y = -1
        self.flag = False

        def helper(root, level):
            if not root or self.flag:
                return
            if root.left and root.right:
                if root.left.val == x and root.right.val == y:
                    self.flag = True
                if root.left.val == y and root.right.val == x:
                    self.flag = True
            if root.val == x:
                self.level_x = level
            if root.val == y:
                self.level_y = level
            helper(root.left, level + 1, x, y)
            helper(root.right, level + 1, x, y)
            

        helper(root, 0, x, y)
        if self.flag:
            return False
        return self.level_x == self.level_y
#DFS
        
