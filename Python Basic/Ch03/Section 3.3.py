## Section 3.3 ##
Chapter = 3
Section = 3 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
import numpy as np
ar = np.arange(6).reshape((2,3))
print(ar)
print(ar.max())
print(ar.sum(axis=1))
print(ar.max(axis=1))
print(ar.mean(axis=0))
print(ar.min(axis=0))

# Ex 2
print("\nEx 2\n")
ar = np.array([[  1,    2,    3,    4],
       [ 46,   99,  100,   71],
       [ 81,   59,   90,  100]])
eng = np.argsort(ar[1])
print(ar[:,eng])
