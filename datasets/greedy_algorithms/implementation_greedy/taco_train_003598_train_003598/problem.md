The Chef commutes to work every day using the city's underground metro. The schedule for the trains has recently been changed and he wants to know how long it will take to travel from the station nearest to his house and the station nearest to his restaurant.

The Chef doesn't want to change the route he took before, so he simply has to find out how long it will take to reach his restaurant along his usual route. This route is given by a sequence of stations s_{0}, s_{1}, ..., s_{n} where s_{0} is the station where the Chef enters the metro and s_{n} is the station where the Chef exits the metro.

Trains are scheduled to run between every two consecutive stations s_{i-1} and s_{i}. Such a schedule is specified by three integers x_{i}, l_{i}, and f_{i}. This means that the first train on this line starts operating at time x_{i}. The time it takes this train to travel from s_{i-1} and s_{i} is exactly l_{i} units. Finally, a train departs from station s_{i-1} every f_{i} minutes following the previous train. That is, a train departs at time x_{i}, x_{i}+f_{i}, x_{i}+2f_{i}, and so on.

The Chef is very experienced at navigating the metro so the time it takes him to transfer between trains at a given station  is essentially zero. Thus, if the Chef arrives at a station, say s_{i}, the moment that the train from s_{i} to s_{i+1} is scheduled to depart, he skillfully hops on this next train. However, if the Chef arrives when no train to s_{i+1} is scheduled to depart, he must wait until the scheduled departure time.

Help the Chef figure out how long it will take him to travel from station s_{0} to station s_{n}. You may assume that the Chef is already at station s_{0} at time 0.

------ Input ------ 

The first line consists of a single integer denoting the number of test cases (at most 50). Each test case begins with a line containing a single integer n between 1 and 1000 indicating the number of lines the Chef must traverse (so there are n+1 stations s_{0}, s_{1}, ..., s_{n}). The next n lines describe the train schedules between stations, one per line. The i'th such line gives the values x_{i}, l_{i}, and f_{i} for the train that travels between stations s_{i-1} and s_{i}.

The x_{i} values will be between 0 and 1000 and the l_{i} and f_{i} values will be between 1 and 1000.

------ Output ------ 

For each test case you are to output a single integer denoting the minimum time t for which the Chef can reach station s_{n} using the given route. Remember, the Chef starts at s_{0} at time 0.

----- Sample Input 1 ------ 
3
2
0 4 7
0 6 5
2
0 1 2
6 2 10
2
1 2 3
0 2 3
----- Sample Output 1 ------ 
11
8
5
