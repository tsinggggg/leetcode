class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        def neighbours(k):
            return [(x[1],x[2]) for x in times if x[0] == k]
        
        visited = set()
        queue = [K]
        def zero():
            return 0
        time = collections.defaultdict(zero)
        
        
        while queue:
            curr = queue.pop(0)
            curr_time = time[curr]
            visited.add(curr)
                        
            n = neighbours(curr)
            
            for x,y in n:
                if x not in visited or curr_time + y < time[x]:
                    queue.append(x)
                    visited.add(x)
                    time[x] = curr_time + y
        
        
        if len(visited) < N:
            return -1
        else:
            return max(time.values())
                        
        
        
        
        
