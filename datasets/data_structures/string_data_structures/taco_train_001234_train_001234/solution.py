n = eval(input())

mq = set(input().split())

_ = eval(input())

c = 0
while _:
	_ -= 1
	if mq.issubset(set(input().split())):
		c += 1
print(c)
