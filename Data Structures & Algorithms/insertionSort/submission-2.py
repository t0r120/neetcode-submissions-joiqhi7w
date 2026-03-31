# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for b in range(len(pairs)):
            a = b-1
            while a >= 0 and pairs[a].key > pairs[a+1].key:
                temp_var = pairs[a+1]
                
                pairs[a+1] = pairs[a]
                pairs[a] = temp_var
                
                a -= 1
            res.append(pairs[:])
        return res