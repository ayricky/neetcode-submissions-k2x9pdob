class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(set)
        for course, prereq in prerequisites:
            premap[course].add(prereq)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if not premap[node]:
                return True

            visited.add(node)
            for prereq in premap[node]:
                if not dfs(prereq):
                    return False
            
            visited.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
