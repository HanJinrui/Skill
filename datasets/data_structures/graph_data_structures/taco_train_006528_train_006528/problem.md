Given a reference of a node in a connected undirected graph. Return a clone of the graph.
Each node in the graph contains a value (Integer) and a list (List[Node]) of its neighbors.
For Example :    
class Node {
    public int val;
    public List neighbors;
}
Example 1:
Input:
adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: 1
Explanation: The graph is cloned successfully.
Example 2:
Input:
adjList = [[2],[1]]
Output: 1
Explanation: The graph is cloned successfully.
Your Task:
You don't need to read input or print anything. Your task is to complete the function cloneGraph( ) which takes a node will always be the first node of the graph as input and returns the copy of the given node as a reference to the cloned graph.
Note: After the user will returns the node of the cloned graph the system will automatically check if the output graph is perfectly cloned or not.The output is 1 if the graph is cloned successfully. Otherwise output is 0. You can't return a reference to the original graph you have to make a deep copy of that.
Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(N).
Constraints:
1 <=Number of nodes<= 100
1 <=Node value<= 100

Starter code:
```python
#User function Template for python3



class Solution():

    def cloneGraph(self, node):

        #your code goes here
```
