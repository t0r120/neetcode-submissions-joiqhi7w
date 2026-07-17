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
        # correspondera al indice de la lista nums
        # Usamos la funcion get para obtener el valor de alguna llave.
        #Si no existe, le agregar el valor 0. 
        #Así, Busca la llave que es el indice de nums
        # Si es un nuevo valor le agrega cero y le suma uno
        for num in nums:
            helper[num] = 1 + helper.get(num, 0)
        
        # {1:1, 2:2, 3:3}
        #Creamos un array
        arr = []
        #iteramos por la llave y por el valor haciendo uso de items()
        for num, hlp in helper.items():
        #Organizamos los items en sublistas y las unimos a arr
            arr.append([hlp,num])
        # [[1,1],[2,2],[3,3]]
        #ORdenamos
        arr.sort()
        [[3,3],[2,2],[1,1]]
        #Guardamos en un array vacio para guardar solo el valor de K
        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
            #[3,2]
        return res





        