class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = Counter(tasks)
        max_heap = [count for count in count_map.values()]
        heapq.heapify_max(max_heap)

        time = 0
        q: deque[list[int, int]] = deque()
        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                count = heapq.heappop_max(max_heap) - 1
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(max_heap, q.popleft()[0])
        
        return time