if __name__=='__main__':
	names = []
	for i in range(0,int(input())):
		names.append(input())
	s_names=sorted(names)
	numlist = []
	output = []
   # print(s_names)
	for i in s_names:
		if i not in output:
			output.append(i)
			numlist.append(1)
		else:
			numlist[output.index(i)] += 1

	for i in range(0,len(output)):
		print(output[i],numlist[i])
