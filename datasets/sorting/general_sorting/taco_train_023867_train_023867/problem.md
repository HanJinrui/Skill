All the students in NIT are very lazy. They want to have maximum time for rest. But due to college rules, they must maintain 75% attendance at the end of every week.

Given the schedule of a week, tell them what is the maximum amount of time they might have for resting.

NOTE:

Each day has 24 hrs. i.e. 24x60x60 seconds.

Classes can of any duration from 1 sec to 24 hrs.

Time of any 2 classes on same day will never intersect.

Constraints:

1 ≤ t ≤ 10

1 ≤ n ≤ 2000

Where n is the total number of classes in the week and t is number of test cases.

Input:

First line of input will be an integer t, the number of test cases.

Each test case will contain 7 lines i.e. the schedule of each day.

First integer in each line will denote the number of classes on that day , say ni , followed by 2xni integers denoting start and end time of each class in seconds ( where 0 represents 12:00 at night and 60 represents 12:01 at night).

Output:

For each test case output the Maximum amount of time in seconds students have for resting.

SAMPLE INPUT
1
3 60 70 80 90 100 200
3 50 70 100 120 150 200
3 50 80 90 100 200 220
3 80 100 110 115 200 210
3 10 20 40 50 60 100
3 10 50 60 80 90 100
3 50 80 90 100 200 300

SAMPLE OUTPUT
604555

Explanation

Resting time will be maximum when students attend:
Day 1 – first 2 classes
Day 2 – first 2 classes
Day 3 – all 3 classes
Day 4 – all 3 classes
Day 5 – first 2 classes
Day 6 – last 2 classes
Day 7 – first 2 classes.
Total classes the attended is 16 = 75% of 21.
