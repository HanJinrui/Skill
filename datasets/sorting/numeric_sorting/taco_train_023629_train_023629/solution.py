a = abs
(A, B, C, D) = map(int, (input() + ' ' + input()).split())
print(a(A * D - B * C) / max(a(A + B) + a(C + D) + 1e-09, a(A - B) + a(C - D)))
