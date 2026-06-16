class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = {}
        for task in tasks:
            m[task] = m.get(task, 0) + 1
        print(m.values())
        max_heap = list(m.values())
        heapq.heapify_max(max_heap)
        print(max_heap)

        time = 0
        q = deque()
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                putback = q.popleft()
                heapq.heappush_max(max_heap, putback[0])


        return time