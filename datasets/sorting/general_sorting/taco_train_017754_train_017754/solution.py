from collections import deque
from typing import List
from sys import stdout

class ContestParser:

	def __init__(self):
		self.buffer = deque()

	def next_token(self) -> str:
		if len(self.buffer) == 0:
			self.buffer.extend(input().split())
		return self.buffer.popleft()

	def next_int(self) -> int:
		return int(self.next_token())
parser = ContestParser()

def ask(v: int) -> int:
	print('? {}'.format(v))
	stdout.flush()
	return parser.next_int()

def answer(v: int) -> int:
	print('! {}'.format(v))
n = parser.next_int()
left = 1
right = n
while left < right:
	mid = (left + right) // 2
	b_1 = ask(mid)
	b_2 = ask(mid + 1)
	if b_1 < b_2:
		right = mid
	else:
		left = mid + 1
answer(left)
