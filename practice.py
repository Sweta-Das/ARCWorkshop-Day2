import numpy as np

n1 = np.array([100, 200, 300, 400])
print(n1)

import Modules

a = Modules.Birds["name"]
print(a)



import camelcase

c = camelcase.CamelCase()
txt = "hello everyone"

print(c.hump(txt))