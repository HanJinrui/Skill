import math
import os
import random
import re
import sys

def choose2(n):
	return n * (n - 1) // 2

def choose3(n):
	return n * (n - 1) * (n - 2) // 6
n = int(input())
l = list(map(int, input().rstrip().split()))
d = {}
for stick in l:
	d[stick] = d.get(stick, 0) + 1
max_num = max(l)
mp_2 = [0] * (max_num + 1)
mp_2p = [0] * (max_num + 1)
mp_3 = [0] * (max_num + 1)
flatten = list(sorted(d.items()))
for (i, (stick1, cnt1)) in enumerate(flatten):
	for (sum3, sum3_cnt) in flatten[i + 1:]:
		if sum3_cnt < 3:
			continue
		rstick = stick1
		if sum3 > rstick * 3:
			break
		if cnt1 >= 3 and rstick * 3 == sum3:
			mp_3[sum3] += choose3(cnt1)
		missing_stick = sum3 - rstick
		mp_3[sum3] += cnt1 * mp_2[missing_stick]
		if rstick * 2 >= sum3:
			continue
		missing_stick -= rstick
		missing_one_cnt = d.get(missing_stick, 0) if missing_stick < rstick else 0
		if missing_one_cnt > 0 and cnt1 >= 2:
			mp_3[sum3] += choose2(cnt1) * missing_one_cnt
	for (stick2, cnt2) in flatten[:i]:
		sum_pair = stick1 + stick2
		if sum_pair > max_num:
			continue
		if sum_pair in d:
			mp_2p[sum_pair] += cnt1 * cnt2 * mp_2[sum_pair]
			if cnt1 >= 2 and cnt2 >= 2:
				mp_2p[sum_pair] += choose2(cnt1) * choose2(cnt2)
		mp_2[sum_pair] += cnt1 * cnt2
	if stick1 * 2 <= max_num and cnt1 >= 2:
		mp_2[stick1 * 2] = choose2(cnt1)
	if cnt1 >= 4 and stick1 * 2 in d:
		mp_2p[stick1 * 2] += cnt1 * (cnt1 - 1) * (cnt1 - 2) * (cnt1 - 3) // 24
res = 0
for (length, num_long) in d.items():
	if num_long >= 2:
		res += mp_2p[length] * choose2(num_long)
	if num_long >= 3:
		res += mp_3[length] * choose3(num_long)
print(res)
