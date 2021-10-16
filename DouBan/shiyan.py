import numpy as np
a = np.array([[1,2,3],[4,5,6]])
# print(a)
d = np.array([7,8,9])
a = np.insert(a,1,d,0)
print(a)