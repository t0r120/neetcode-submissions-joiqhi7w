class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Dado un array de numeros
        #Y un entero K
        #Retorna los k elementos mas frecuentes en el array

        # K NOS AYUDARA EN LA LONGITUD DE LA LISTA.

        helper = {}
        # 1.- Diccionario. Nos ayuda a tener un conteo de las apariciones
        
        # 2.- Este bucle itera por el len(de nums) 
        # En cada iteración, la llave del diccionario helper, 
        # correspondera al indice de la lista nums y se le asignara
        # el valor de num
        for num in nums:
            helper[num] = 1 + helper.get(num, 0)
        
        
        arr = []
        for num, hlp in helper.items():
            arr.append([hlp,num])
        arr.sort()
        
        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res





        