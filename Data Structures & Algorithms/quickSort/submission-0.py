# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) -1
        self.coreQuickSort(pairs, s, e)

        return pairs

    def coreQuickSort(self, arr, s, e):

        if e - s + 1 <= 1:

            return
        
        p = arr[e]
        l = s

        for i in range(s, e):

            if arr[i].key < p.key:
                temp = arr[l]

                arr[l] = arr[i]
                arr[i] = temp

                l += 1

        arr[e] = arr[l]
        arr[l] = p
        

        self.coreQuickSort(arr, s, l - 1)
        self.coreQuickSort(arr, l + 1, e)

    
    


        