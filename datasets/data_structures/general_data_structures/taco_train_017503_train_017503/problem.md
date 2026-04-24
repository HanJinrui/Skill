Meera teaches a class of $n$ students, and every day in her classroom is an adventure. Today is drawing day!

The students are sitting around a round table, and they are numbered from $1$ to $n$ in the clockwise direction. This means that the students are numbered $1,2,3,\ldots,n-1,n$, and students $1$ and $n$ are sitting next to each other.

After letting the students draw for a certain period of time, Meera starts collecting their work to ensure she has time to review all the drawings before the end of the day. However, some of her students aren't finished drawing! Each student $\boldsymbol{i}$ needs $t_i$ extra minutes to complete their drawing. 

Meera collects the drawings sequentially in the clockwise direction, starting with student ID $\boldsymbol{x}$, and it takes her exactly $1$ minute to review each drawing. This means that student $\boldsymbol{x}$ gets $0$ extra minutes to complete their drawing, student $x+1$ gets $1$ extra minute, student $x+2$ gets $2$ extra minutes, and so on. Note that Meera will still spend $1$ minute for each student even if the drawing isn't ready. 

Given the values of $t_1,t_2,\ldots,t_n$, help Meera choose the best possible $\boldsymbol{x}$ to start collecting drawings from, such that the number of students able to complete their drawings is maximal. Then print $\boldsymbol{x}$ on a new line. If there are multiple such IDs, select the smallest one.

Input Format

The first line contains a single positive integer, $n$, denoting the number of students in the class. 

The second line contains $n$ space-separated integers describing the respective amounts of time that each student needs to finish their drawings (i.e., $t_1,t_2,\ldots,t_n$).

Constraints

$1\leq n\leq10^5$
$0\leq t_i\leq n$

Subtasks

$1\leq n\leq10^4$ for $30\%$ of the maximum score.

Output Format

Print an integer denoting the ID number, $\boldsymbol{x}$, where Meera should start collecting the drawings such that a maximal number of students can complete their drawings. If there are multiple such IDs, select the smallest one.
Sample Input 1
3
1 0 0
Sample Output 1
2
Explanation 1

Meera's class has $n=3$  students:

If $x=1$ , then only two students will finish.
The first student needs  $t_1=1$ extra minute to complete their drawing. If Meera starts collecting here, this student will never finish their drawing. Students  $2$ and $3$ 's drawings are already finished, so their drawings are ready when she collects them in the second and third minutes.

If $x=2$ , then all three students will finish.
The second student needs $t_2=0$  extra minutes, so the drawing is ready for Meera to collect. The next (third) student's drawing is also ready one minute later, as $t_3=0$ . Meera then proceeds to the next (first) student, who needed $t_1=1$ extra minute. Because she already spent two minutes collecting the work of the other two students, the first student's drawing has already been completed for $2-1=1$ minute.

If $x=3$ , then all three students will finish.
The third student needs $t_3=0$ extra minutes, so the drawing is ready for Meera to collect. The next (first) student's drawing is also ready one minute later, as  $t_1=1$ and  $1$ minute passed while Meera collected the third student's drawing. She then proceeds to the next (second) student, whose drawing was already completed (as $t_2=0$ )

Starting with student IDs $x=2$   or  $x=3$ will result in a maximum number of completed drawings (i.e.,$3$ ). Because there are two equally valid answers, we choose the smaller ID, $2$, and print it as our answer.

Sample Input 2
3
0 1 2
Sample Output 2
1
