Given a sorted linked list of distinct nodes (no two nodes have the same data) and an integer X. Count distinct triplets in the list that sum up to given integer X.
Note: The Linked List can be sorted in any order.
Example 1:
Input: LinkedList: 1->2->4->5->6->8->9, X = 17
Output: 2
Explanation: Distinct triplets are (2, 6, 9) 
and (4, 5, 8) which have sum equal to X i.e 17.
Example 2:
Input: LinkedList: 1->2->4->5->6->8->9, X = 15
Output: 5
Explanation: (1, 5, 9), (1, 6, 8), (2, 4, 9), 
(2, 5, 8), (4, 5, 6) are the distinct triplets
Your Task:  
You don't need to read input or print anything. Complete the function countTriplets() which takes a head reference and X as input parameters and returns the triplet count
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ Number of Nodes ≤ 10^{3} 
1 ≤ Node value ≤ 10^{4}

Starter code:
```python
#User function Template for python3

def countTriplets(head,x):
    # code here
```
