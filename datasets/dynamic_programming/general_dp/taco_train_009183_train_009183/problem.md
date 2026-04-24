Agon Packers and Movers specialize in moving large number luggages from one place to another.

The luggages are packed by the Packers, and after they're done with the job, the Movers take over.

First, the Packers put the packages they have packed in a single line, one behind the other, and then the Movers come one by one to pick the packages.
A Mover can come only once, can only pick the first few packages in the line, and then take them with him. He might also choose not to pick any. Another Mover comes, and repeats the process, till all the packages are taken. The Movers need to carry of all the packages.

The Movers are a friendly lot, and care about each other - so their goal is to minimize the maximum load that any Mover gets.
You are given the number of movers M in the first line.
The next line contains the number of packages P.
The next line contains the weight of the P package (in Kilograms) in order - first weight representing of first package in the line, separated by space.

You need to print the maximum load any mover carries in the best possible case, in accordance with their goal.

Constraints:
1 ≤ M ≤ 15
1 ≤ P ≤ 250
Weight of each Package (W): 1 ≤ W ≤ 10000

Examples:
1)
INPUT
5
5
1 1 1 2 1

OUTPUT
2

Explanation: There are 5 movers, and doesn't matter what the split is, one mover needs to carry at least 2 kilograms

2)
INPUT
2
4
5 10 21 20

OUTPUT
36

Explanation: 36 is the best case among all the splits possible (happens when the first guy picks 5, 10 and 21)

SAMPLE INPUT
2
5
200 25 974 564 429

SAMPLE OUTPUT
1199
