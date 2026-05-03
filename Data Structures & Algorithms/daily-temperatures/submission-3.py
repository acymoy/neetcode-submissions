class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)

        for i in range(len(temperatures), -1, -1):
            j = i + 1
            while j < len(temperatures):
                # if the current j value is greater
                if temperatures[i] < temperatures[j]:
                    results[i] = j - i
                    break
                # if there is not greater value in list
                if not results[j]:
                    break
                # otherwise skip forward by j days
                else:
                    j += results[j]
        return results