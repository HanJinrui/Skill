input()
s = {int(x) for x in input().split()}
I = [input().split() for x in range(int(input()))]
for x in I:
	eval('s.' + x[0] + '(' + ','.join(x[1:]) + ')')
print(sum(s))
