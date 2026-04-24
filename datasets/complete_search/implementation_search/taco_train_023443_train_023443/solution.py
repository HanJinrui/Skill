n=eval(input())
pat=list(input())
numbers=list(range(1,n+1))
i=j=0
while len(numbers)!=1:
	if pat[i]=='b':
		del numbers[j]
		j=j-1
	i=i+1
	j=j+1
	if i>=len(pat):i=0
	if j>=len(numbers):j=0

print(numbers[0])
