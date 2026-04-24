def find_strongest(s):
	alphabet = "zyxwvutsrqponmlkjihgfedcba"
	r = ""
	for c in alphabet:
		i = s.find(c)
		if i != -1:
			r = r + s[i]
			s = s[i:]
			continue
	return r

length = int(input().rstrip("\n"))
input = input().rstrip("\n")
print(find_strongest(input))
