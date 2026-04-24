import sys
for line in sys.stdin:
	i=line.find('//')
	if i==-1:
		print(line.replace('->','.'), end=' ')
	else:
		print(line[:i].replace('->','.')+line[i:], end=' ')
