## Section 3.1 ##
Chapter = 3
Section = 1 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
import numpy as np
ar = np.array([[10, 20, 30, 40], [50, 60, 70 ,80]])
print(ar)

# Ex 2
print("\nEx 2\n")
m = np.array([[ 0, 1, 2, 3, 4],
            [ 5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14]])
print(m[1,2])
print(m[-1,-1])
print(m[1,1:3])
print(m[1:,2])
print(m[:2,3:])

# Ex 3
print("\nEx 3\n")
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(x[x % 3 == 0])
print(x[x % 4 == 1])
print(x[(x % 3 == 0) & (x % 4 == 1)]) # and는 numpy array 연산 X