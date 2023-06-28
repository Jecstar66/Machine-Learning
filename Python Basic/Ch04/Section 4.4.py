import numpy as np
import pandas as pd

## Section 4.4 ##
Chapter = 4
Section = 4
print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# Ex 1
print("\nEx 1\n")
import seaborn as sns
titanic = sns.load_dataset("titanic")
titanic.head()
print(titanic.count())

# Ex 2
print("\nEx 2\n")

print(titanic["sex"].value_counts().sort_values())
print(titanic["age"].value_counts().sort_values())
print(titanic["class"].value_counts().sort_values())
print(titanic["alive"].value_counts().sort_values())

# Ex 3
print("\nEx 3\n")
print(titanic["age"].mean())
print(titanic[titanic.sex=="female"]["age"].mean())
print(titanic[(titanic.sex=="female") & (titanic["class"] == "First")]["age"].mean())

# Ex 4
print("\nEx 4\n")
titanic["category1"] = titanic.apply(lambda x : x.sex if x.age >= 20 else "child", axis = 1)
print(titanic)

# Ex 5
print("\nEx 5\n")
titanic["category1"] = titanic.apply(lambda x : x.sex if x.age >= 20 else "child", axis = 1)

titanic["age"] = round(titanic["age"].fillna(titanic["age"].mean()),2)
print(titanic.age)

# Ex 6
print("\nEx 6\n")
titanic["category2"] = titanic["sex"] + titanic["age"].astype(int).astype(str)
print(titanic["category2"])

# Ex 7
print("\nEx 7\n")
bins = [1, 20, 30, 50, 70, 100]
labels = ["미성년자", "청년", "중년", "장년", "노년"]
titanic["분류"] = pd.cut(titanic["age"],bins=bins,labels=labels)
df = pd.value_counts(titanic["분류"].sort_values())/titanic["분류"].count()
print(df)

# Ex 8
print("\nEx 8\n")
titanic["category3"] = titanic.apply(lambda x : "미성년자" if x.age < 20 else x["분류"]+(" 남성" if x.sex == "male" else " 여성"), axis = 1)
print(titanic.category3)