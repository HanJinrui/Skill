def solution(s1, s2, i):
	if i == len(s2):
		return 0
	mop = abs(s2[i] - s1[i]) + solution(s1, s2, i + 1)
	for x in range(i + 1, len(s1)):
		s1[i], s1[x] = s1[x], s1[i]
		mop = min(mop, 1 + abs(s2[i] - s1[i]) + solution(s1, s2, i + 1))
		s1[i], s1[x] = s1[x], s1[i]
	return mop
	

def main():
	for _ in range(int(input())):
		s1, s2 = list(map(ord, input())), list(map(ord, input()))
		print(solution(s1, s2, 0))

main()
