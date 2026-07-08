class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        matches = {}
        for num in nums:
            matches[num] = matches.get(num, 0) + 1
            if matches[num] > 1:
                return True
                
        return False
        
        