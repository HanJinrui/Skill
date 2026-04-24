t=eval(input());d=set();i=0
while i<t:d.add(input());i+=1
print(len(d))
d=sorted(d)
for i in d:
	print(i)
