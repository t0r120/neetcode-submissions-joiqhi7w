class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        memory = counter = 0
        #res = a cnt y cnt es igual a 0
        
        for num in nums:
            if num == 0:
                memory = max(memory, counter)
                counter = 0
            else:
                counter += 1
        return max(memory, counter)