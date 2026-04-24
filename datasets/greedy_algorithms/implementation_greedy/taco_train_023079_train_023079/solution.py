from itertools import accumulate
I = lambda : map(int, input().split())
I()
print(len(set(accumulate(I())) & set(accumulate(I()))))
