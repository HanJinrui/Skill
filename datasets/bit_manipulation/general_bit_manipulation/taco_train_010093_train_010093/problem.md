N coders decided to go for a trip for the upcoming weekend. They chose Crater Lake National Park in Oregon, USA as their destination, because they all like to take a lot of photos and the beautiful nature gives them a chance to do so.

In order to capture some memories from the trip, they wanted to take the greatest number of distinct meaningful photos from their trip. Since they all are math geeks, they consider two photos different if and only if the sets of coders on both photos are different. Moreover, they consider a photo meaningful if and only if there is at least one coder on the photo.

However, not all coders like each other. In more detail, there are P pairs of coders who don't like each other very much, so they don't want to appear together on any photo, otherwise the whole trip will be ruined!

Your task, as you obviously take part in the trip, is to calculate the maximum number of distinct meaningful photos that can be taken in such a way that the trip will not be ruined.

Input format:

In the first line, there is a single integer T denoting the number of test cases to handle. Then, description of T tests follow. In the first line of each such description, two integers N and P are given. Then P lines follow, each one consisting of two distinct integers A and B denoting a single pair of coders who don't like each other.

Output format:

Output exactly T lines, and in the i^th of them, print a single integer denoting the answer to the i^th test case.

Constraints:

1 ≤ T ≤ 10
1 ≤ N ≤ 15
1 ≤ P ≤ N * (N-1) / 2
1 ≤ A, B ≤ N 
A ≠ B 
All pairs of coders given in a single test are distinct.

SAMPLE INPUT
1
3 1
1 2

SAMPLE OUTPUT
5

Explanation

In the only test case, there are N = 3 coders and one pair of coders who don't like each other. The maximal number of photos the coders can take is 5, and the following sets of coders can appear on a single photo: {1}, {2}, {3}, {1, 3}, {2,3}.
