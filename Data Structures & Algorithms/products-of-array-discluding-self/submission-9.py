class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[i - 1] * nums[i - 1])
        
        current_right = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = current_right * res[j]
            current_right *= nums[j]
        return res