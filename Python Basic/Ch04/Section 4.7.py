import numpy as np
import pandas as pd

## Section 4.7 ##
Chapter = 4
Section = 7
print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# Ex 1
print("\nEx 1\n")
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
})
groups = df2.groupby(df2.key1)
grdf = pd.DataFrame(groups["data1"].sum())
print(grdf)

# Ex 2
print("\nEx 2\n")
# https://steadiness-193.tistory.com/42
import seaborn as sns
iris = sns.load_dataset("iris")
print(iris.groupby(iris.species).agg("mean"))

# Ex 3
print("\nEx 3\n")
tips = sns.load_dataset("tips")
tips['tip_pct'] = tips['tip'] / tips['total_bill']

print(tips.pivot_table("tip_pct",["day","time"],"size"))
print(tips.tip_pct.groupby([tips.day,tips.time]).mean().unstack(0))
print(tips.tip_pct.groupby(tips["size"]).mean().sort_values(ascending=False))

# Ex 4
print("\nEx 4\n")
titanic = sns.load_dataset("titanic")

titanic["type"] = pd.qcut(titanic.age,3,labels=["Low", "Medium", "High"])
print(titanic)
def live_ratio(x):
        return x.sum() / len(x)
print(titanic.groupby([titanic.sex, titanic["class"], titanic.type])["survived"].agg(live_ratio).unstack("class"))
print(titanic.groupby(["sex", "class"])["survived"].agg(live_ratio))