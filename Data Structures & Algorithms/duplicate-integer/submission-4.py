class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() 
        # Un set con los numeros vistos(No permite duplicados)

        for num in nums: #Iterar sobre la lista de numeros
            if num in seen: #Si num existe en seen es repetido
                return True
            seen.add(num) 
            #Agrega de 0 hasta la len de la lista los numeros
        return False # Si num no esta en seen ninguno es repetido