from collections import Counter as C
F = lambda s, t: sum((C(s) & C(t)).values())
(s, t) = (input(), input())
(n, m) = (F(s, t), F(s.lower(), t.lower()))
print(n, m - n)
