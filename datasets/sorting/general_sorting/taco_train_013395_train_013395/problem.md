Protection of the Indian border and safe transport of items from one point to another along the border are the paramount jobs for the Indian army. However they need some information about the protection status along the length of the border. The border can be viewed as the real x-axis. Along the axis, Indian army has N checkpoints for lookout. 
We know that each checkpoint is located at an integer location xi. Each checkpoint must have a fleet of armed men which are responsible for guarding the neighboring areas of the checkpoint and provide military assistance of all kinds. The size of the fleet is based on the location of the checkpoint and how active the region is for terrorist activities.

Given the number of armed men assigned at the i^th checkpoint, as pi, this information is available for all checkpoints. 
With the skills of the armed men, it is known that if for the i^th checkpoint, the length on the x axis that they can defend is a closed interval [xi-pi, xi+pi].
Now, your task is to transport some military items from position S to the end position E on the x-axis.
Input:
First line of the input contains 3 integers N, S and E. N is the number of checkpoints that the Indian Army has on the border.
Then N lines follow. i^th line contains 2 integers, xi and pi.

Output:
Print the total distance of the x-axisfrom S to E, that is not protected by the armed forces.

Constraints:
1 ≤ N ≤ 10^5
1 ≤ xi, pi ≤ 10^18
xi + pi ≤ 10^18
1 ≤ S ≤ E ≤ 10^18

SAMPLE INPUT
5 229 8419
1795 95
4873 720
3149 81
6101 2325
3674 629

SAMPLE OUTPUT
2626
