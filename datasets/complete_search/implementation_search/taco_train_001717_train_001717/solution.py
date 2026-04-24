import sys
(n, a, b, c) = map(int, sys.stdin.read().split())
sys.stdout.write(str([0, min(c, a + b, 3 * a), min(2 * c, b, 2 * a), min(3 * c, b + c, a)][n % 4]))
