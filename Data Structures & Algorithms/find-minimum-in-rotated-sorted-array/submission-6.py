class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find midpoint -> if nums[m] is less than nums[m - 1] (and nums[m + 1] is less than nums[m]?) return nums[m]

        # compare midpoint to two pointers:
        # if nums[l] > nums[midpoint] -> minimum HAS to be on the left side
            # search left side
        # else (nums[l] < nums[midpoint]) -> minimum could be on either side
            # if nums[r] < nums[midpoint] -> search right
            # otherwise (nums[r] > nums[midpoint]) -> search left

        l, r = 0, len(nums) - 1

        while l <= r:
            midpoint = (r + l) // 2
            if nums[midpoint] < nums[midpoint - 1] or r - l == 0:
                return nums[midpoint]

            if nums[l] > nums[midpoint]:
                r = midpoint - 1
            else:
                if nums[r] < nums[midpoint]:
                    l = midpoint + 1
                else:
                    r = midpoint - 1