Its Diwali time and Little Roy's family is having a lot of guests. Guests come in families. Each guest family has M members. Roy's task is to serve sweets to them. Roy has N different sweets and each sweet has some specific sweetness level S and quantity Q.

Each guest family will give R rupees (as a token of gratitude) to Roy if following conditions are satisfied:
The sweetness level of sweet served is greater than or equal to the
   members in the guest family
Every member should get sweet of one particular sweetness level
Every member should get equal quantity of sweets

where R = 100 * Quantity of sweet(s) each member had.

After each guest family has left, Roy's Mom makes sure that the quantity of sweets that guest family had is restored to its original value.

Your task is to find R - maximum amount in rupees Roy has after all the guests have come and left.

Input:

First line will contain integer N - number of different sweets.

Next N lines will contain two space separated integers S and Q

S - Sweetness level of the sweet (this will be distinct for each sweet)

Q - Quantity of that sweet

This is followed by an integer G - number of guest families.

Next G lines will contain integer M, indicating number of members in the guest family.

Output:

Print integer R in single line.

Constraints:

1 ≤ N, S, Q, G, M ≤ 1000000

SAMPLE INPUT
5
5 8
3 6
10 7
4 6
2 5
2
5
8

SAMPLE OUTPUT
100

Explanation

We have 2 families, first family has 5 members. According to condition 1, Roy can serve two sweets with sweetness level 5 and 10. According to condition 2, Roy can serve only one of these two sweets. According to condition 3, Roy can serve only 1 sweet to each member.

So, after first family R = 1*100 i.e. R = 100

For second family, we have only one sweet with sweetness level greater than or equal to 8, which is sweetness level 10. Quantity of this sweet is 7, but Roy has to serve equal number of sweets to each of the 8 members. Hence 0 sweets are served.

So after second family R = R + 0*100  (means he didn't get any rupees from second family)

Hence the output, 100.
