A new deadly virus has infected large population of a planet. A brilliant scientist has discovered a new strain of virus which can cure this disease. Vaccine produced from this virus has various strength depending on midichlorians count. A person is cured only if midichlorians count in vaccine batch is more than midichlorians count of person. A doctor receives a new set of report which contains midichlorians count of each infected patient, Practo stores all vaccine doctor has and their midichlorians count. You need to determine if doctor can save all patients with the vaccines he has. The number of vaccines and patients are equal.
Example 1:
Input:
n = 5
vac[] = {123 146 454 542 456}
per[] = {100 328 248 689 200}
Output: 0
Explanation: Doctor cannot save all the patients.
Example 2:
Input:
n = 8
vac[] = {87 93 50 22 63 28 91 60}
per[] = {64 27 41 27 73 37 12 69}
Output: 1
Explanation: Doctor can save all the patients.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isPossible () which takes an array containing midichlorians count of people (per[]), an array containing the midichlorians count of vaccines (vac[]) and their size n as inputs. It returns 1 if all the patients can be saved and 0 otherwise.
 
Expected Time Complexity: O(nLogn).
Expected Auxiliary Space: O(1).
 
Constraints:
1<=n<=10^{5}

Starter code:
```python
#User function Template for python3

class Solution:
    def isPossible (self, per, vac, n):
        # your code here
```
