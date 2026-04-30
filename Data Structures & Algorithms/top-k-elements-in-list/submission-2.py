class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {} 
        for n in nums:
            m[n] = m.get(n, 0) + 1
        print(m)

        bucket = [[] for _ in range(len(nums))]
        for item in m.keys():
            bucket[m[item] - 1].append(item)
        print(bucket)

        result = []
        for b in bucket[::-1]:
            for j in b:
                result.append(j)
                if len(result) == k:
                    return result

        return result
