import random
import numpy as np
import pandas as pd

## Section 4.1 ##
Chapter = 4
Section = 1 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# Ex 1
print("\nEx 1\n")
s = pd.Series([1,2,3,4], index = ["A", "B", "C", "D"])
print(s.items()[0])