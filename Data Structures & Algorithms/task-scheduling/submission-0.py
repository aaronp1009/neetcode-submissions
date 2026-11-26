class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We will use a maxHeap and a queue to determine when tasks are available

        # Python does not have a maxHeap, so create a count map of the tasks then convert each count to opposite sign
        counts = Counter(tasks) # Will make the counts hashmap
        maxHeap = [-cnt for cnt in counts.values()]
        # Heapify this
        heapq.heapify(maxHeap) # Now we have this ready, next have queue for easy tracking

        q = deque() # Double ended queue, should store [taskCount, availableTime]
        time = 0 # We start at t = 0

        while maxHeap or q:
            time += 1

            if maxHeap: # We have something in our maxHeap to pop and process a task
                taskCount = 1 + heapq.heappop(maxHeap) # Add 1 since we made everything negative
                if taskCount: # So this was not a 0, add to our queue
                    q.append([taskCount, time + n])
            
            # handle our queue now, moving back to heap if needed
            if q and q[0][1] == time: # Check if available
                heapq.heappush(maxHeap, q.popleft()[0]) # Index 0 has the actual count
        
        return time