(_, k) = map(int, input().split())
s = input()[-k:]
print(s.replace(')', '(', s.count(')') - k // 2))
