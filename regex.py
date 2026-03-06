import re

# pattern=re.compile('aaba')
# target='aabababaababbaababbaababaabbaa'
# matcher=re.finditer(pattern,target)
# for match in matcher:
#     print(match.start(),match.end(),match.group())

# target='aabababaababbaababbaababaabbaa'
# matcher=re.finditer('baa',target)
# for match in matcher:
#     print(match.start(),match.end(),match.group())

matcher=re.finditer('a*','aaababababaaaaaa')
for match in matcher:
    print(match.start(), match.end(), match.group())


"""
[abc]-either a or b or c
[a-z]
[A-z]
[0-9]
[a-zA-Z0-9]
[^a-zA-Z0-9]- ^ means special characters

\w = words
\W= remaining excluding words
\d=digit
\D=remaining all excluding digit
\s=space
\S=excluding space

Quantifiers
a
a+ - atleast 1 a
a? - atmost
a* - all a
a{m}-max
a{m,n}-max and min
"""


m=re.match('python','python is simple to learn')
print(m)

m=re.fullmatch('python is simple to learn','python is simple to learn')
print(m)

m=re.findall('simple','python is simple to learn')
print(m)

m=re.search('learn','python is simple to learn')
print(m)

m=re.split(' ','python is simple to learn')
print(m)

m=re.sub(' ','><','python is simple to learn')
print(m)

m=re.subn(' ','--','python is simple to learn')
print(m)









