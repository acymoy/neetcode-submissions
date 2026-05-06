class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            m[n] = 1 + m.get(n, 0)
        
        bucket = [[] for _ in range(len(nums))]
        for key, v in m.items():
            bucket[v - 1].append(key)

        result = []
        for n in range(len(bucket) - 1, -1, -1):
            for v in bucket[n]:
                result.append(v)
                if len(result) == k:
                    return result

        return result
    