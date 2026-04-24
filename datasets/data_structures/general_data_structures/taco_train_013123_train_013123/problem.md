A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then process $\textit{q}$ queries, where each query is one of the following $3$ types: 

1 x: Enqueue element $\boldsymbol{x}$ into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.

Input Format

The first line contains a single integer, $\textit{q}$, denoting the number of queries. 

Each line $\boldsymbol{i}$ of the $\textit{q}$ subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query $\textit{type}$, but only query $1$ is followed by an additional space-separated value, $\boldsymbol{x}$, denoting the value to be enqueued.

Constraints

$1\leq q\leq10^5$  
$1\leq type\leq3$  
$1\leq|x|\leq10^9$  
It is guaranteed that a valid answer always exists for each query of type $3$.

Output Format

For each query of type $3$, print the value of the element at the front of the queue on a new line. 

Sample Input
STDIN   Function
-----   --------
10      q = 10 (number of queries)
1 42    1st query, enqueue 42
2       dequeue front element
1 14    enqueue 42
3       print the front element
1 28    enqueue 28
3       print the front element
1 60    enqueue 60
1 78    enqueue 78
2       dequeue front element
2       dequeue front element

Sample Output
14
14

Explanation

Perform the following sequence of actions:

Enqueue $\textbf{42}$; $\textit{queue}=\{42\}$.
Dequeue the value at the head of the queue, $\textbf{42}$; $\mbox{queue}=\{\}$.
Enqueue $\mathbf{14}$; $\textit{queue}=\{14\}$.
Print the value at the head of the queue, $\mathbf{14}$; $\textit{queue}=\{14\}$.
Enqueue $28$; $queue=\{14,28\}$.
Print the value at the head of the queue, $\mathbf{14}$; $queue=\{14,28\}$.
Enqueue $\mbox{60}$; $queue=\{14,28,60\}$.
Enqueue $78$; $queue=\{14,28,60,78\}$.
Dequeue the value at the head of the queue, $\mathbf{14}$; $queue=\{28,60,78\}$.
Dequeue the value at the head of the queue, $28$; $queue=\{60,78\}$.
