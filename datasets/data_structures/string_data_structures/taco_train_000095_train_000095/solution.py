import re

class Solution:

	def sentenceWord(self, text):
		no_of_sentences = re.split('[.?!]+', text)
		no_of_words = text.strip().split(' ')
		return (len(list(filter(lambda x: len(x) != 0, no_of_sentences))), len(no_of_words))
