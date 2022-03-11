from a7_include import *
from hash_map import *

m = HashMap(10, hash_function_2)
for i in range(100, 200, 10):
    m.put(str(i), str(i * 10))
print(m.get_keys())
m.resize_table(1)
print(m.get_keys())
m.put('200', '2000')
m.remove('100')
m.resize_table(2)
print(m.get_keys())
