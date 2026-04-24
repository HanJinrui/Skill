The cost of stock on each day is given in an array price[] of size n. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
Note: 
The output format is as follows - (buy_day sell_day) (buy_day sell_day)
For each input, the output should be in a single line, i.e. It's important to move to a new/next line for printing the output of other test cases.
Example 1:
Input:
n = 7
price[] = { 100, 180, 260, 310, 40, 535, 695 }
Output:
(0 3) (4 6)
Explanation:
We can buy stock on day 1 and sell it on day 4, 
We can buy another stock on day 5 and sell it on day 7, 
which will give us maximum profit.
Example 2:
Input:
n = 10
price[] = {23, 13, 25, 29, 33, 19, 34, 45, 65, 67}
Output:
(1 4) (5 9)
Explanation:
We can buy stock on day 1 and sell it on day 4, 
We can buy another stock on day 5 and sell it on day 9, 
which will give us maximum profit.
Your Task:
Complete stockBuySell()  function and print all the days with profit in a single line. And if there is no profit then print "No Profit". You do not require to return since the function is void.
Expected Time Complexity: O(n)Expected Auxiliary Space: O(n)
Constraints:
2 <= n <= 10^{4}
0 <= price[i] <= 10^{4}

Starter code:
```python
#User function Template for python3







def stockBuySell(price, n):

    # code here
```
