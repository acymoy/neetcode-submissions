class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        print('hello')
        print(top, bottom)
        while top <= bottom:
            v_midpoint = (bottom + top) // 2
            print(v_midpoint)
            print(matrix[v_midpoint][0], matrix[v_midpoint][-1])

            # target is in that row
            if matrix[v_midpoint][0] <= target and matrix[v_midpoint][-1] >= target:
                print('target is in row', v_midpoint)
                l, r = 0, len(matrix[v_midpoint]) - 1
                while l <= r:
                    midpoint = (l + r) // 2
                    if matrix[v_midpoint][midpoint] == target:
                        return True
                    elif matrix[v_midpoint][midpoint] > target:
                        r = midpoint - 1
                    else:
                        l = midpoint + 1
                return False
            # target is not in that row
            elif matrix[v_midpoint][0] >= target:
                bottom = v_midpoint - 1
            else:
                top = v_midpoint + 1


        return False