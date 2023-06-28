## Section 2.3 ##
Chapter = 2
Section = 3 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1-(1)
print("""Ex 1-(1)\nBeautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.\n""")

# Ex 1-(2)
print("Ex 1-(2)\n")
str_var = ""
i = 0
for i in range(5):
    if i == 0 or i == 4:
        str_var += "@" * 6
    else:
        str_var += "@    @"
    str_var = str_var + "\n"
print(str_var)

# Ex 2
ans = "2020-12-25"
print("Ex 2\n")
print(ans.replace("-",""))

