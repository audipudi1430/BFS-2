# Approach:
# 1. Perform level order traversal (BFS) using a queue to traverse the tree level by level.
# 2. For each level, store all node values in a temporary list (level).
# 3. Append the last element of each level (rightmost node) to the result list.

# Time Complexity: O(N) — where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N) — for storing the queue and the result list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        result = []

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                level.append(node.val)
                
            if level:
                result.append(level[-1])  # Append rightmost node of the level
        
        return result