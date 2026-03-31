class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        
    def mergeSortHelper(self, pairs: List[Pair], left : int, right : int):
        # Caso base
        if left >= right:
            return pairs
        
        #Encuentra la mitad de la lista
        mid = (left + right) // 2

        # Divide la seccion izquierda de la lista
        self.mergeSortHelper(pairs, left, mid)

        # Divide la seccion derecha de la lista
        self.mergeSortHelper(pairs, mid + 1, right)

        # Une cada sublista con la funcion auxiliar merge
        self.merge(pairs, left, mid, right)

        return pairs

    # Crea la función auxiliar merge
    def merge(self, array, left, mid, right):
        # Apuntador de los valores de la subllista izquierda
        L = array[left : mid + 1]
        # Apuntador de los valores de la subllista derecha
        R = array[mid + 1 : right + 1]

        # Crea los apuntadores internos para L y R
        i = 0
        j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1