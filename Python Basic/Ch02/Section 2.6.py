## Section 2.6 ##
Chapter = 2
Section = 6

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
def Ex1_1(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"

def Ex1_2(y):
    if y % 4 == 0 :
        if y % 100 == 0:
            if y % 400 == 0:
                return "윤년"
            else:
                return "평년"
        else :
            return "윤년"
    else:
        return "평년"
    
print(Ex1_1(13), Ex1_2(2024))

# Ex 2
print("\nEx 2\n")
def days1(month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    else:
        return 28
print(days1(11))

# Ex 3
print("\nEx 3\n")
def days2(year, month):
    if month != 2:
        return days1(month)
    else :
        if Ex1_2(year) == "윤년":
            return 29
        else:
            return 28
print(days2(2016,2))

# Ex 4
print("\nEx 4\n")
a, b, c = map(int, input("a, b, c : ").split())
def diffsum(a,b,c):
    return abs((a+b+c)-(pow(a,2)+pow(b,2)+pow(c,2)))
print(diffsum(a,b,c))

# Ex 5. global variable : must be included in function declaration!!
print("\nEx 5\n")
m = 0 
def diffsum2(a,b,c):
    global m
    if abs((a+b+c)-(pow(a,2)+pow(b,2)+pow(c,2))) > m :
        m = abs((a+b+c)-(pow(a,2)+pow(b,2)+pow(c,2)))
    return abs((a+b+c)-(pow(a,2)+pow(b,2)+pow(c,2)))
diffsum2(a,b,c)
print("m = %d" % m)