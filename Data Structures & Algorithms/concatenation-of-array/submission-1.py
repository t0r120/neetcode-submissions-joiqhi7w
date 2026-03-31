# Crear un array ans de longitud 2n(2 * la entrada)
# Donde ans[i] se igual a nums[i] (Que sean iguales en orden)
"""
Ejemplo Input: nums = [22,21,20,1]

Output: [22,21,20,1,22,21,20,1]
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []  # Lista vacía
        for i in range(2):   #realizará dos bucles, especificamente esta prueba pide eso
            for j in range(len(nums)): # J itera sobre la longitud de nums
                ans.append(nums[j])   # AGregando los valores
        return ans # REspuesta



        