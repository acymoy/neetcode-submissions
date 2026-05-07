class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # initialize two pointers for the beginning and end of subarray
        # get the midpoint and compare to the target -> if target, return midpoint

        # if midpoint is greater than left side -> cycle ends on the right side
            # compare to left pointer value -> if target is greater than, search left
        # if midpoint is greater than right side -> cycle (rotation on right)
            # compare to right pointer value -> if target is less than search right


        l, r = 0, len(nums) - 1

        while l <= r:
            m = ((r + l) // 2)
            if nums[m] == target:
                return m
            
            # left sorted portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1



        