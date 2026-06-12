class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        
        can_do = [[] for i in range(numCourses)]

        for prereq in prerequisites:
            can_do[prereq[1]].append(prereq[0])
            indegree[prereq[0]]+=1

        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        nodes_visited = 0
        while queue:
            top = queue.popleft()
            nodes_visited += 1

            for num in can_do[top]:
                indegree[num] -= 1
                if indegree[num] == 0:
                    queue.append(num)

        return nodes_visited == numCourses

        
        