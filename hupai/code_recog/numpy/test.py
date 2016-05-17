import numpy as np

a = np.array([[6, 7, 1, 6],
              [1, 0, 2, 3],
              [7, 8, 2, 1],
              [1, 3, 5, 6]])

print(np.sum(a, axis=1))
# 乘法
print(2 * a)
# del
np.delete(a, 1, 0)
print(a)
print(a.shape)

print(a[1:-1, 1:-1])
