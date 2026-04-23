# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #root es un TreeNOde
        #Target Sum es un valor externo a verificar
        if not root:
            return False
        
        #DOs caminos, usar una pila usar una cola.
        #Usamos una tupla. Para validar el nodo actual y 
        stack = [(root, targetSum - root.val)]

        #Mientras haya algo en la pila
        while stack:
            #Desempaqueta la pila y guarda los valores de la tupla en una variable
            node, curr_sum = stack.pop()
            #Si ya no hay nodos hijo y la suma de sus nodos 
            #dio 0(o sea que la sumde los nodos menos el target dio cer)
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            # Nodo izquierdo
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
        return False

            

        
        