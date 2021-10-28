# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] 
# indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create a adjacency list for all the courses
        preReqMap = { i : [] for i in range(numCourses)}
        
        for i,j in prerequisites:
            print(i,j)
            preReqMap[i].append(j)
        
        # Set to keep track of current courses in recursion
        visited = set()
        
        def dfs(course):
            # If a course which is part of current recursion is visited again then
            # this indicates there is (cycle) and one of it's prereq course is dependent on it 
            # so we return false
            if course in visited : 
                return False
            
            # If course has no preReq we return True
            if preReqMap[course] == []:
                return True
            
            # Adding course to visited set 
            visited.add(course)
            
            # Perform DFS on all it's prereq courses 
            for i in preReqMap[course]:
                if not dfs(i) : return False
            
            # Remove course from visited if all it's preReq courses are checked 
            visited.remove(course)
            
            # As now it's known that this course can be taken we can make it's preReq list empty for efficiency
            preReqMap[course] = []

            return True
        
        # Perform dfs on all courses as courses my from a disconnected graph
        for j in range(numCourses):
            if not dfs(j) : return False
        
        return True