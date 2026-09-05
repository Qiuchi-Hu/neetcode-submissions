class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> List[int]:

        prep_dict = {}
        prep_count = [0]*numCourses
        for course, prep in prerequisites:
            if not prep in prep_dict:
                prep_dict[prep] = []
            prep_dict[prep].append(course)
            prep_count[course]+=1
        
        order = []
        process = deque()
        for course in range(numCourses):
            if prep_count[course] == 0:
                process.append(course)
        
        while process:
            course = process.popleft()
            order.append(course)
            if course in prep_dict:
                for following in prep_dict[course]:
                    prep_count[following]-=1
                    if prep_count[following] ==0:
                        process.append(following)
        
        if sum(prep_count) == 0:
            return order
        else:
            return []
        
            