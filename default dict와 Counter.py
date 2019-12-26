from collections import Counter

text = list("gallahad")
text
c = Counter(text)

print(c)
c= Counter(red=4, blue=2)
print(c)
print(list(c.elements()))

