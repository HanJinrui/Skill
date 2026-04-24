MOD = 10 ** 9 + 7

def solve(head):
	x = 0
	while head:
		x = x * 10 + head.data
		head = head.next
	return x

def multiplyTwoList(head1, head2):
	a = solve(head1)
	b = solve(head2)
	return a * b % MOD
