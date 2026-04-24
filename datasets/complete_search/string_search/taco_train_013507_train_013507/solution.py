import re
t = 'abacaba'
p = '(?<!abac)(?<!abacab)' + ''.join((f'({x}|\\?)' for x in t)) + '(?!caba)(?!bacaba)'
for s in [*open(0)][2::2]:
	s = t in s and s or re.sub(p, t, s, 1)
	print(('NO', 'YES ' + s.replace('?', 'd'))[s.find(t) == s.rfind(t) >= 0])
