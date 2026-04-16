# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def breadthFirstOrder(root):
            
            queue = deque()
            sub_lists = []

            if root:
                queue.append(root)
            
            
            while len(queue) > 0:
                level = []
                #Iterate in range of 0 to queue length
                for i in range(len(queue)):
                    curr = queue.popleft()
                    #Agregar sublista
                    level.append(curr.val)
                    
                    #existe algo en en left?
                    if curr.left:
                        queue.append(curr.left)
                    #Existe algo en right?
                    if curr.right:
                        queue.append(curr.right)
            
                sub_lists.append(level)

            return sub_lists

        return breadthFirstOrder(root)

        