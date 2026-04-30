class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not len(nums):
            return []

        products_to_left = []
        current_product = 1
        for i in range(len(nums)):
            if not i:
                products_to_left.append(1)
            else:
                current_product *= nums[i - 1]
                products_to_left.append(current_product)

        products_to_right = [0 for _ in range(len(nums))]
        current_product = 1
        for i in range(len(nums), 0, -1):
            if i - 1 == len(nums) - 1:
                products_to_right[i - 1] = 1
            else:
                current_product *= nums[i]
                products_to_right[i - 1] = current_product
            
        result = []
        for i in range(len(nums)):
            result.append(products_to_right[i] * products_to_left[i])

        return result