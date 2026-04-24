inp = lambda : list(map(int, input().split()))
l1 = inp()
(a, b) = inp()
print(['NO', 'YES'][inp()[a - 1] < inp()[-b]])
