import numpy as np
import pandas as pd

## Section 4.8 ##
Chapter = 4
Section = 8
print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# Ex 1
print("\nEx 1\n")
np.random.seed(0)
df = pd.DataFrame({
    "date": pd.date_range("2020-12-25", periods=100, freq="D"), 
    "value": np.random.randint(100, size=(100,))
})
df.index = df.date
print(df.resample("M").sum())