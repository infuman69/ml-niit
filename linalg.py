import numpy as np

a= np.array([[1,2],[3,4]])

print("Rank of a:", np.linalg.matrix_rank(a))

print("Trace of a:", np.trace(a))

print("Determinant of a:", np.linalg.det(a))

print("Inverse of a:", np.linalg.inv(a))

print("Power of a:",np.linalg.matrix_power(a,3))