class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp=[]
        for i in range(0, len(nums)):
            if nums[i] in temp:
                return True
            else:
                temp.append(nums[i])
        return False