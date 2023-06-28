import numpy as np
import pandas as pd

## Section 4.3 ##
Chapter = 4
Section = 3
print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# Ex 1
print("\nEx 1\n")
data = {
        "이름" : ["김병준", "양승준", "김준석", "이우제", "전병관"],
        "나이" : [23,21,21,22,22],
        "지역" : ["서울", "대전", "대전", "서울", "경기"],
        "키" : [178, 176.2, 170.3, 173.1, 175.2],
        "보직" : ["통신", "통신", "운전", "통신", "운전"]
}

df = pd.DataFrame(data, index = data["이름"], columns = list(data.keys()))
print(df.loc[["김병준","양승준"]])
print(df.loc[[False, True, True, False, True]])
print(df.loc[df["나이"] >= 22])
print(df.loc[df["나이"] == 21, ["보직"]])
print(df.loc[:, "지역"])
