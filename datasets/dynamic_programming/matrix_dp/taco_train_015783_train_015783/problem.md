Areesha likes to play interesting games with her friend Adam.
The game they played last evening is about building a number with n digits.

They start with a number without any digits.
There will be n moves.
In each move players append one digit to a number — so a new digit will be the last digit after the move.
The only rule is: after every appended digit, the number has to be divisible by this digit.
It implies that they can never add a digit 0.

Adam thinks the game is easy, because there are many numbers they can get at the end.
But how many are there?
Count numbers they can get, modulo 2^{32}.

Input format
The only line of the input contains one integer n — the number of times players will append a digit.

Output format
Print the number of numbers Adam and Areesha can get, modulo 2^{32}.

Constraints

1 ≤ n ≤ 10^{18}

SAMPLE INPUT
2

SAMPLE OUTPUT
41

Explanation

For n = 2 there are 41 possible numbers:
$11, 12, 15, 21, 22, 24, 25, 31, 32, 33, 35, 36, 41, 42, 44, 45, 48, 51, 52, 55, 61,$
$62, 63, 64, 65, 66, 71, 72, 75, 77, 81, 82, 84, 85, 88, 91, 92, 93, 95, 96, 99$
