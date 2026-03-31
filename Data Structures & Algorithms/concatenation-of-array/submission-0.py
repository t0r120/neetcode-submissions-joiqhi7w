class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_list = []
        for i in range(len(nums)):
            ans_list.append(nums[i])
        ans_list.extend(nums)
        return ans_list
        