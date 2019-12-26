from collections import deque
from collections import OrderedDict

deque_list = deque()
for i in range(5):
    deque_list.appendleft(i)

print(deque_list)

s=deque(reversed(deque_list))
print(s)

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k,v)



d = OrderedDict()

d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k,v)



def sort_by_key(t):
    return t[0]

from collections import Ordereddict

d = dict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in OrderedDict(sorted(d.items(), key=sort_by_key)).items():
    print(k, v)
