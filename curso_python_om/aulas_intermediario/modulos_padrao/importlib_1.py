import importlib

import importlib_m

print(importlib_m.variavel)

for i in range(10):
    importlib.reload(importlib_m)
    print(i)

print('Fim')