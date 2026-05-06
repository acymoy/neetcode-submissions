class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        for i in range(1, len(nums)):
            l.append(l[i - 1] * nums[i - 1])
        
        res = [0 for _ in range(len(nums))]
        current_right = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = current_right * l[j]
            current_right *= nums[j]
        return res