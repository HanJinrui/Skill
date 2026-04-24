It’s the company's 3^rd anniversary, and everyone is super-excited about it. There is a tradition in the company, that the interns decide the seating arrangement of all the members. The requirements of this order are:
The CEO of the company must sit in the middle. (In case of even number of team members, he can sit on either central position.)
The CTO and the COO must sit on the ends of the row.
The sum of the absolute height difference of adjacent members should be minimum.

Bhargav wants to steal the show by coming up with the minimum sum of absolute height difference of the heights of all the members while satisfying first 2 conditions. Since he is a product management intern, he does not know anything about computer programs. Please help him before a software engineer intern solves this.

Input Format: 

ceo_height coo_height cto_height

total number of team members (excluding above three)

height_array (excluding above three)

Output Format:

Minimum sum of absolute height difference

Constraints:

1 ≤ number of team members ≤ 20

1 ≤ heights ≤ 100

SAMPLE INPUT
13 17 11
2
12 10

SAMPLE OUTPUT
10

Explanation

Optimal order: 11 10 13 12 17 -> 1+3+1+5 = 10
