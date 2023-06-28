import numpy as np
import pandas as pd

## Section 4.6 ##
Chapter = 4
Section = 6
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

data2 = {
        "성명" : ["김병준", "양승준", "이담학", "김경태", "김준석"],
        "전공" : ["전기전자","컴공","무공","전기전자","간호"],
        "지역" : ["서울", "대전", "서울", "서울", "대전"],
        "무게" : [70, 65, 80, 80, 60],
        "보직" : ["통신", "통신", "통신", "통신", "운전"]
}
df2 = pd.DataFrame(data2, index = data2["성명"], columns = list(data2.keys()))

dfm = pd.merge(df,df2,left_on=["이름","지역","보직"],right_on=["성명","지역","보직"],how="outer")
print(dfm)

# Ex 2
print("\nEx 2\n")
np.random.seed(0)
df_result1 = pd.DataFrame(np.random.randint(0,100, (6,2)), columns=['매출', '비용'], index=[str(i+1) +'월' for i in range(6)])
df_result2 = pd.DataFrame(np.random.randint(0,100, (6,2)), columns=['매출', '비용'], index=[str(i+7) +'월' for i in range(6)])
df_result1["이익"] = df_result1["매출"] - df_result1["비용"]
df_result2["이익"] = df_result2["매출"] - df_result2["비용"]
df_year = pd.concat([df_result1,df_result2])
print(df_year)
df_year.loc["All"] = df_year.sum()
print(df_year)