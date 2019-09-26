
import numpy as np
a=np.array([1,2])
print(a.shape)
a=np.array([[1,2]])
print(a.shape)
a=np.array([[[1,2]]])
print(a.shape)

a=np.array([[1],[2]])
print(a.shape)
a=np.array([[[1],[2]]])
print(a.shape)

a=np.array([[[1]],[[2]]])
print(a.shape)

import numpy as np
x = np.array([1,2])
print(x.shape)
y = np.expand_dims(x, axis=0)
print(y.shape)
y = np.expand_dims(x, axis=1)
print(y.shape)