import pandas as pd
## Section 4.1 ##
Chapter = 4
Section = 1 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# Ex 1
print("\nEx 1\n")
sr = pd.Series([1,3,4,5], index = ["a", "v", "i", "s"])
sr2 = pd.Series([7,-1,0,2], index = ["a","x","i","s"])
print(sr+sr2)
print(sr-sr2)
print(sr*sr2)
print(sr/sr2)

# Ex 2
print("\nEx 2\n")
data = {
        "이름" : ["김병준", "양승준", "김준석", "이우제", "전병관"],
        "나이" : [23,21,21,22,22],
        "지역" : ["서울", "대전", "대전", "서울", "경기"],
        "키" : [178, 176.2, 170.3, 173.1, 175.2],
        "보직" : ["통신", "통신", "운전", "통신", "운전"]
}

df = pd.DataFrame(data, index = data["이름"], columns = list(data.keys()))
print(df.T)

# Ex 3
print("\nEx 3\n")
data = {
    "국어": [80, 90, 70, 30],
    "영어": [90, 70, 60, 40],
    "수학": [90, 60, 80, 70],
}
columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]
df = pd.DataFrame(data, index=index, columns=columns)

print(df["수학"])
print(df[["국어","영어"]])
df["평균"] = df.mean(axis=1) # axis = 1 : 행별 연산 (현재 : 행은 학생 이름으로 이루어진 index 배열)
print(df["평균"])
df.loc["방자","수학"] = 80

df["평균"] = (df["국어"]+df["수학"]+df["영어"])/3
print(df)
print(df[:"춘향"])
print(df.loc["향단"])

