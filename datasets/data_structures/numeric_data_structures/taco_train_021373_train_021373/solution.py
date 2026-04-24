from typing import Optional

class Solution:

	def primeList(self, head: Optional['Node']) -> Optional['Node']:

		def isPrime(n):
			for i in range(2, int(n ** 0.5) + 1):
				if n % i == 0:
					return False
			return True

		def getPrime(n):
			i = 0
			if n == 1:
				return 2
			while True:
				if n - i > 1 and isPrime(n - i):
					return n - i
				if isPrime(n + i):
					return n + i
				i += 1
			return -1
		cur = head
		while cur:
			cur.data = getPrime(cur.data)
			cur = cur.next
		return head
