class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            if s1 != s2:
                heapq.heappush_max(stones, abs(s1 - s2))

        return heapq.heappop_max(stones) if len(stones) else 0


