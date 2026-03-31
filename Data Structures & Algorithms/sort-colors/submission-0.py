class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        const = [0,0,0] 
        for k in nums:
            const[k] += 1
        
        i = 0

        for n in range(len(const)):
            for j in range(const[n]):
                nums[i] = n
                i += 1

