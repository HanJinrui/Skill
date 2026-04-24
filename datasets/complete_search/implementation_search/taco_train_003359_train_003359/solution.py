i = lambda : {*input().split()}
i()
(a, b) = (i(), i())
(c, d) = sorted([min(a), min(b)])
print([c + d, min({'9'} | a & b)][len(a & b) > 0])
