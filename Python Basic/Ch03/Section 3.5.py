## Section 3.5 ##
Chapter = 3
Section = 5 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
import random 
import numpy as np
# Ex 1
print("\nEx 1\n")
print(np.random.randint(2, size = 10))
print(np.random.randint(7, size = 100).sum()/100)

# Ex 2
print("\nEx 2\n")
print((10000*(1+np.random.randn(250)/100)).round(2))