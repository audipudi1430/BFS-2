# Approach:
# 1. Perform level order traversal (BFS) while keeping track of each node's parent.
# 2. In each level, check if both x and y are found and store their respective parents.
# 3. If both are found in the same level but have different parents -> they are cousins.

# Time Complexity: O(N) — where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N) — for storing the queue used in BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = collections.deque([(None, root)])  # (parent, node)

        while q:
            qLen = len(q)
            findX = findY = False
            parentX = parentY = None

            for i in range(qLen):
                parent, node = q.popleft()

                if node:
                    if node.val == x:
                        findX = True
                        parentX = parent
                    if node.val == y:
                        findY = True
                        parentY = parent

                    q.append([node, node.left])
                    q.append([node, node.right])
            
            if findX and findY:
                return parentX != parentY  # Cousins -> Same level, Different parents
            if findX or findY:
                return False  # Found only one -> Not cousins
        
        return False  # If both not found
