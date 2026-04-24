n,m = list(map(int,input().split()))
initial = list(map(int,input().split()))
target = list(map(int,input().split()))
current_index = 0
target_index = target.index(initial[0])
for i in range(1,m+1):
	direction,shift = input().split()
	shift = int(shift)
	if direction == "L":
		current_index -= shift
		current_index %= n
	else:
		current_index += shift
		current_index %= n
	if current_index == target_index:
		print(i)
		exit(0)
print(-1)
