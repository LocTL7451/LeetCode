### 2492. Minimum Score of a Path Between Two Cities
### https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
"""
Runtime | 1977 ms
Beats | 25.78%
Memory | 66.3 MB
Beats | 74.12%
"""

import math
# My approach for this question is to first create a graph containing all the connected edges including city 1 and city n 
# We then search for the minimum edge cost in the graph which will be our solution. 
class Solution:
    def minScore(self, n, roads):
        retDistance = (10**5)+2
        connectedGraph = [[] for i in range(n+1)]
        for edge in roads:
            # Creating the graph that contains the node outgoing edges are connected to, as well as the weight of the corresponding edge
            connectedGraph[edge[0]].append((edge[1], edge[2])) 
            connectedGraph[edge[1]].append((edge[0], edge[2]))
        print(connectedGraph)
        
        # First we want to ensure that we are not visiting each node more than once with the exception of node 1 and node n
        # 0 indicating we have not visited it
        visitedArr = [0]*(n+1)
        # Here we will be implementing a queue structure to traverse through the graph to find the minimum edge value that lead node 1 to node n
         
        self.queue = []
        # First queuing up all nodes connected to node 1 
        self.pushQueue(1)
        visitedArr[1] = 1
        while len(self.queue) != 0:
            currentNode = self.popQueue()
            for destinationNode, weight in connectedGraph[currentNode]:
                retDistance = min(retDistance,weight)
                # Queue the desination node as the current node and traverse that iteratively
                if visitedArr[destinationNode] == 0:
                    visitedArr[destinationNode] = 1
                    self.pushQueue(destinationNode)
        
        return retDistance

        
    def pushQueue(self, value):
        self.queue.append(value)
        print("Successfully Pushed value: {}".format(value))
        
    def popQueue(self):
        return(self.queue.pop())
            
n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
Sol = Solution()
print(Sol.minScore(n, roads))