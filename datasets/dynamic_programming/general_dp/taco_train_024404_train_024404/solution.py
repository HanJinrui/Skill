def is_k_palin(str, k):
	if len(str) == 1:
		return 0
	start = 0
	end = len(str) - 1
	while start <= end:
		if str[start] != str[end]:
			if k > 0:
				k -= 1
				if str[start] == str[end - 1]:
					start -= 1
				else:
					end += 1
			else:
				return 0
		start += 1
		end -= 1
	return 1
