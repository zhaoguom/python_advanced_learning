a = {"zhaoguom": {"age": 13},
     "chenfen": {"age": 14}
     }

b = a.copy()
b["zhaoguom"]["age"] = 15

print(b)
print(a)

import copy
a = {"zhaoguom": {"age": 13},
     "chenfen": {"age": 14}
     }
b = copy.deepcopy(a)
b["zhaoguom"]["age"] = 15

print(b)
print(a)

default = b.setdefault("zhaoguom", "hahaha")
pass

default = b.setdefault("iris", "hahaha")
pass

print(b)
pass