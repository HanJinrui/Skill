(_, s) = (input(), set(input().split()))
for _ in range(int(input())):
	tokens = input().split()
	getattr(s, tokens[0])(set(input().split()))
print(sum(map(int, s)))
