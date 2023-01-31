### defaultdict
defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

```python
from collections import defaultdict
d = defaultdict(int)

for letter in s:
    d[letter] += 1
	
# iteration
for k,v in d.items():
	print("{}: {}".format(k,v))
```
