class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} 

        for i in range(len(nums)):
            if nums[i] not in m.keys():
                m[target - nums[i]] = i
            else:
                return [m[nums[i]], i]