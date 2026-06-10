class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            # courses that a prerequisite could unlock
            adj[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            prereq = queue.popleft()
            result.append(prereq)
            for course in adj[prereq]:
                # check off dependency of course on prereq
                in_degree[course] -= 1
                # if all prereqs for course are met, add it to queue
                if in_degree[course] == 0:
                    queue.append(course)
        
        if len(result) == numCourses: return result
        return []

