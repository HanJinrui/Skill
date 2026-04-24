Kabra is a very good friend of JP. So JP has assigned him a task. Given an array, two operations can be performed on it. They are
1) L X : Rotate the array towards left by X.
2) R X : Rotate the array towards right by X.
Now you will be given 2 arrays containing N unique elements. The first one is the inital array(A) and the second one is target array(T).
Also you will be given a list of M operations having ids from 1 to M to be serially performed on it. If after performing any operation the array becomes same as the target array print the id of the operation. If it is not possible print "-1"(without quotes).

Input format:
First line will contain two space separated integers N and M.
Second line will contain N space separated integers Ai denoting the initial array.
Third line will contain N space separated integers Ti denoting the target array.
Next M lines contain the operations of type 1 or 2.

Output format:
Print a single line containing the required answer.

Constraints:
1 ≤ N , M ≤ 10^5
1 ≤ Ai ,  Ti  ≤ 10^9
1 ≤ X ≤ 1000
Note: It is guaranteed that the initial and target arrays are different.
Note: Target array will always be a rotated version of the initial array

SAMPLE INPUT
4 4
2 1 3 4
3 4 2 1
R 1
L 2
L 1
L 5

SAMPLE OUTPUT
3

Explanation

The initial array is 2 1 3 4. Target array is 3 4 2 1.
After the first operation the array becomes 4 2 1 3.
After the second operation it becomes 1 3 4 2.
After the third operation it becomes 3 4 2 1. At this moment the array is equal to the target array hence the answer is 3.
