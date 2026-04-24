n = int(input())
a = list(map(int,input().split()))
s = [1]*n
a.sort(reverse=True)
for i in range(1,n):
	for j in range(i):
		if a[j]%a[i]==0  and s[i]<s[j]+1:
			s[i] = s[j]+1
r = max(s)
if r==1:
	print(-1)
else:
	print(r)
