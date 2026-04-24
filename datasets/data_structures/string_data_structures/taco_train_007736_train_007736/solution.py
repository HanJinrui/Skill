import re
regex = '[aeiou]{3,}'
for _ in range(int(input())):
	string = input()
	match = re.search(regex, string)
	if match == None:
		print('Sad')
	else:
		print('Happy')
