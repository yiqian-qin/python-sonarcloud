# Sort the courses by the last day in ascending order
# Use a priority queue to store the duration of each course, with the longest course on top
# Iterate through the sorted courses and add each course's duration to a running total
# If the running total exceeds the current course's last day, pop the longest course from the priority queue
# Keep track of the number of courses taken and return it at the end

import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        pq = []
        total_time = 0
        for duration, last_day in courses:
            total_time += duration
            heapq.heappush(pq, -duration)
            if total_time > last_day:
                total_time += heapq.heappop(pq)
        return len(pq)