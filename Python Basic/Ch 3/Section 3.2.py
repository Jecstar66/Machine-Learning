## Section 3.2 ##
Chapter = 3
Section = 2 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
import numpy as np
arr = np.hstack([np.zeros((3,3)),np.ones((3,2))])
arr2 = np.arange(10,160,10, dtype = 'f').reshape(3,-1)
ans = np.tile(np.vstack([arr,arr2]),(2,1))
print(ans)