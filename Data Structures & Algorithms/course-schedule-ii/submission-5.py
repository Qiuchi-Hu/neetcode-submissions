class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> List[int]:

        preq_dict = {}

        for course, preq in prerequisites:
            if course not in preq_dict:
                preq_dict[course] = []

            preq_dict[course].append(preq)

        order = []

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for preq in preq_dict.get(course, []):
                if not dfs(preq):
                    return False

            visiting.remove(course)

            visited.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order