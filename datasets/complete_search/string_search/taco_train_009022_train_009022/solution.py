import re
print(max((len({*x}) for x in re.split('[A-Z\n]', [*open(0)][1]))))
