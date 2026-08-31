class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash_prereq = {}

        for course, prereq in prerequisites:
            if not course in hash_prereq:
                hash_prereq[course] = []

            hash_prereq[course].append(prereq)
        
        path = set()
        visited = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True
            
            if course in hash_prereq:
                path.add(course)
                prereqs = hash_prereq[course]
                for pre in prereqs:
                    if not dfs(pre):
                        return False
                path.remove(course)

            visited.add(course)
            return True

        
        for course in hash_prereq.keys():
            if course not in visited and not dfs(course):
                return False
        
        return True

