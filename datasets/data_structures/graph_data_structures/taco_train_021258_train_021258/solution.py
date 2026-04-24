class Solution:

	def findSequences(self, start, end, wordList):
		from collections import deque
		wordlist = set(wordList)
		q = deque()
		q.append([start, [start]])
		alphabets = 'abcdefghijklmnopqrstuvwxyz'
		res = []
		while q:
			temp = []
			for _ in range(len(q)):
				(word, lst) = q.popleft()
				if word == end:
					res.append(lst)
					continue
				for ind in range(len(word)):
					for letter in alphabets:
						new = word[:ind] + letter + word[ind + 1:]
						if new in wordlist:
							temp.append(new)
							q.append([new, lst + [new]])
			for newword in temp:
				wordlist.discard(newword)
		return res
