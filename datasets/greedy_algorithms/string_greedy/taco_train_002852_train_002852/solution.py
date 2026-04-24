import re
line = input()
s = re.findall('[^a]+', line)
res = []
if len(s):
	for i in s[0]:
		res.append(chr(ord(i) - 1))
	print(line.replace(s[0], ''.join(res), 1))
else:
	print(line[:-1], 'z', sep='')
