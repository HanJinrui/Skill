class Solution:

	def BalancedString(self, N):
		lcalpha = 'abcdefghijklmnopqrstuvwxyz'
		parity = sum(map(int, str(N))) % 2
		tail = (N - 1) % 26 + 1
		th = (tail + 1 - parity) // 2
		return (N - 1) // 26 * lcalpha + lcalpha[:th] + lcalpha[26 + th - tail:]
