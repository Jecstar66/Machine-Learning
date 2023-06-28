import numpy as np
import pandas as pd

## Section 4.5 ##
Chapter = 4
Section = 5
print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# Ex 1
print("\nEx 1\n")
data = {"국어":[82,89,91,84,88],
        "수학":[91,94,100,92,94],
        "영어":[95,84,99,90,89]
}
df_score1 = pd.DataFrame(data,columns=list(data.keys()))
df_score1.index = ["Kim", "Lee", "Park", "Jung", "Choi"]
df_score1.index.name = "이름"
print(df_score1.index)
df_score2 = df_score1.reset_index()
print(df_score2)

df_score2 = df_score2.set_index("이름")
print(df_score2)

# Ex 2
print("\nEx 2\n")
data2 = {"반":[1,3,2,3,1],
        "번호":[1,2,3,4,5],
        "국어":[82,89,91,84,88],
        "수학":[91,94,100,92,94],
        "영어":[95,84,99,90,89]
}
df_score3 = pd.DataFrame(data2,columns=list(data2.keys()))
df_score4 = df_score3.set_index(["반","번호"])
df_score4["평균"] = df_score4.mean(axis=1)
print(df_score4)
df_score5 = df_score3.set_index(["반","번호"])
df_score5 = df_score5.unstack(["반"])
df_score5.columns.names = ['과목', '반']
print(df_score5)
df_score5.loc["평균",:] = df_score5.mean()
print(df_score5)

