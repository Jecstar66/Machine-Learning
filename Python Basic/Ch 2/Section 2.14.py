from sys import getsizeof

## Section 2.14 ##
Chapter = 2
Section = 14

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1 
print("\nEx 1\n")
today = "2023-01-14"
birthday = "2000-06-23"

today = today.split("-")
birthday = birthday.split("-")
age = 0

if int(today[0]) == int(birthday[0]):
    age = 1
else:
    age = int(today[0])-int(birthday[0])
    if int(today[1]) >= int(birthday[1]):
        if int(today[2]) >= int(birthday[2]):
            pass
        else:
            age -= 1
    else:
        age -= 1
print(age)