Goodland is a country with a number of evenly spaced cities along a line.  The distance between adjacent cities is $unrecognized$ unit.  There is an energy infrastructure project planning meeting, and the government needs to know the fewest number of power plants needed to provide electricity to the entire list of cities.  Determine that number.  If it cannot be done, return -1.

You are given a list of city data.  Cities that may contain a power plant have been labeled $unrecognized$.  Others not suitable for building a plant are labeled $unrecognized$.  Given a distribution range of $unrecognized$, find the lowest number of plants that must be built such that all cities are served.  The distribution range limits supply to cities where distance is less than k.

Example 

$unrecognized$ 

$unrecognized$   

Each city is $unrecognized$ unit distance from its neighbors, and we'll use $unrecognized$ based indexing.  We see there are $unrecognized$ cities suitable for power plants, cities $unrecognized$ and $unrecognized$.  If we build a power plant at $unrecognized$, it can serve $unrecognized$ through $unrecognized$ because those endpoints are at a distance of $unrecognized$ and $unrecognized$.  To serve $unrecognized$, we would need to be able to build a plant in city $unrecognized$ or $unrecognized$.  Since none of those is suitable, we must return -1.  It cannot be done using the current distribution constraint.

Function Description  

Complete the pylons function in the editor below.    

pylons has the following parameter(s):  

int k: the distribution range  
int arr[n]: each city's suitability as a building site  

Returns  

int: the minimum number of plants required or -1  

Input Format

The first line contains two space-separated integers $unrecognized$ and $unrecognized$, the number of cities in Goodland and the plants' range constant. 

The second line contains $unrecognized$ space-separated binary integers where each integer indicates suitability for building a plant.  

Constraints

$unrecognized$
Each $unrecognized$.

Subtask

$unrecognized$ for $unrecognized$ of the maximum score.

Output Format

Print a single integer denoting the minimum number of plants that must be built so that all of Goodland's cities have electricity.  If this is not possible for the given value of $unrecognized$, print $unrecognized$.

Sample Input
STDIN         Function
-----         --------
6 2           arr[] size n = 6, k = 2
0 1 1 1 1 0   arr = [0, 1, 1, 1, 1, 0]

Sample Output
2

Explanation

Cities $unrecognized$, $unrecognized$, $unrecognized$, and $unrecognized$ are suitable for power plants.  Each plant will have a range of $unrecognized$. If we build in cities $unrecognized$ cities, $unrecognized$ and $unrecognized$, then all cities will have electricity.
