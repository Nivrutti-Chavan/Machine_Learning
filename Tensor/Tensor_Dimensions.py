import numpy as np

#0D Tensor/Scalar
a=np.array(5)

print(a)
print(a.ndim)

#1DTensor/Vector
D_1=np.array([1,2,3,4])

print(D_1)
print(D_1.ndim)

#2D Tensor/Metrics
D_2=np.array([[1,2,3],[4,5,6]])
print(D_2)
print(D_2.ndim)

# 3D Tensor
D_3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(D_3)
print(D_3.ndim)


# N-D Tensor (Example: 4D)
N_D = np.array([
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ],
    [
        [[9, 10], [11, 12]],
        [[13, 14], [15, 16]]
    ]
])

print(N_D)
print(N_D.ndim)