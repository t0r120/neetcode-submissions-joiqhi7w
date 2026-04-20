class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mp = {}

        for i in range(len(nums)):
#Si el valor de i en la pocision i esta en mp y el indice i - el valor de la llave el posicion es <= k
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
#Sino la clave en la pocisiob del valor del indice en nums será igual al indice i
            mp[nums[i]] = i

        return False
                    
