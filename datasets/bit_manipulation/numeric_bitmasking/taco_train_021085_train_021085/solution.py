from sys import stdin
from functools import lru_cache
input = stdin.readline

def xor2ptnr_1(inpstr):
	val = int(inpstr)
	sb = f'0{val:b}'.rsplit('11')
	if '1' in sb[-1]:
		return val
	return int('01'.join((s.replace('01', '11') for s in sb)), 2)
N = int(input())
Ays = set(map(xor2ptnr_1, input().split()))
print(N - len(Ays))
