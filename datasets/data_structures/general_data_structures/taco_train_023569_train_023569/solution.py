class Solution:

	def intersetPoint(self, head1, head2):
		a = head1
		b = head2
		while a != b:
			a = a.next if a else head2
			b = b.next if b else head1
		return a.data
