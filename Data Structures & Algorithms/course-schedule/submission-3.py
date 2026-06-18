class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        for course, prereq in prerequisites:
            course_map[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                # cycle detected
                return False
            
            if not course_map:
                return True
            
            visited.add(course)
            for prereq in course_map[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            course_map[course] = []
            return True
            
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

            
