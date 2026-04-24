Maga and Alex are good at string manipulation problems. Just now they have faced a problem related to string. But it is not a standard string problem. They have no idea to solve it. They need your help.

A string is called unique if all characters of string are distinct.

String s_1 is called subsequence of string s_2 if s_1 can be produced from s_2 by removing some characters of s_2.

String s_1 is stronger than s_2 if s_1 is lexicographically greater than s_2.

You are given a string. Your task is to find the strongest unique string which is subsequence of given string.

Input:

first line contains length of string.
second line contains the string.

Output:

Output the strongest unique string which is subsequence of given string.

Constraints:

1 ≤ |S| ≤ 100000   

All letters are lowercase English letters.

SAMPLE INPUT
5
abvzx

SAMPLE OUTPUT
zx

Explanation

Select all subsequence of the string and sort them in ascending order. The greatest of all is zx.
