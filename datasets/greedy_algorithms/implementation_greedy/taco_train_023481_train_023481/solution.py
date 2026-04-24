I = lambda : map(int, input().split())
(c1, c2, c3, c4) = I()
I()
A = [min(a * c1, c2) for a in I()]
B = [min(b * c1, c2) for b in I()]
print(min(min(c3, sum(A)) + min(c3, sum(B)), c4))
