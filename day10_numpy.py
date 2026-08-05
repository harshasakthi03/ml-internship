import numpy as np
import numpy as np

arr1 = np.array([10,20,30,40,50])

print(arr1)
print(type(arr1))
arr2 = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr2)
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
print(arr1.ndim)
print(arr1[0])
print(arr1[2])

print(arr2[0][1])
print(arr2[1][2])
print(arr1[1:4])

print(arr2[:,1])
print(arr1 + 5)

print(arr1 * 2)

print(arr1 / 2)

print(np.sum(arr1))

print(np.mean(arr1))

print(np.max(arr1))

print(np.min(arr1))