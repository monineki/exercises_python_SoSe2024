import numpy as np



a = np.arange( 1, 13)

a = np.reshape( a, [3,2,2])

print (a)

M = np.eye(5)
M [3:, :2] = 2
M[:2, 3:] = 3 
print(M)