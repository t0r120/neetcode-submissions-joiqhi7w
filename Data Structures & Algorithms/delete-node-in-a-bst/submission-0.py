# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root):
            curr  = root
            while curr.left and curr:
                curr =  curr.left
            return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
    


        #REcursivamente deletear nodo
        if not root:
            return None #Caso base no hay nodo

        #Buscar Nodo     
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        #key es mayor que el valor del nodo?
            #Si -> nodo.right = delete(nodo.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        #key es menor que el valor del nodo?
            #NO -> nodo.left = delete(nodo.left, key)
        else:
            if not root.right:
                return root.left
        # Si nodo tiene un hijo o no tiene ninguno
            # Si no existe el roor.left:
                #retorna right
            elif not root.left:
                return root.right
            #Si no existe el root.right:
                #retorna left
            else:
                min_node = self.findMin(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root
        # Si nodo tiene dos hijos
            #minNode = Buscar nodo minimo

            #root.val = minNode.val
            #root.right = remover nodo minimo
        # retorna root
        