## Section 2.5 ##
Chapter = 2
Section = 5

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
a, b = 2, 56 
if a % 2 == 0:
    print("a is even")
else:
    print("a is odd")
if (b>=10) and (b<100) and (b%2 ==0):
    print("b is 2-digit even")
else:
    print("b is not a 2-digit even")
    
# Ex 2
print("\nEx 2\n")
y = int(input("Press the year.  "))
if y % 4 == 0 :
    if y % 100 == 0:
        if y % 400 == 0:
            print("leap year!")
        else:
            print("not a leap year")
    else :
        print("leap year!")
else:
    print("not a leap year")
    
# Ex 3
print("\nEx 3\n")
c = 8
if c >= 8:
    print("A")
elif c >= 5:
    print("B")
else:
    print("C")
    
# Ex 4
print("\nEx 4\n")
watermelon = float(input("weight of the watermelon(kg) : "))
if watermelon >= 10:
    print("1등급")
elif watermelon >= 7:
    print("2등급")
elif watermelon >= 4:
    print("3등급")
else:
    print("4등급")
    
# Ex 5
print("\nEx 5\n")
y_a, y_b = 0, 0
x_a = input("자백? ")
x_b = input("자백? ")
if x_a == "O" and x_b == "O":
    y_a, y_b = 5, 5    
elif x_a == "X" and x_b == "X":
    y_a, y_b = 1, 1
else:
    if x_a == "O":
        y_a, y_b = 0, 10
    else:
        y_a, y_b = 10, 0
print("A 복역 : %d년, B 복역 : %d년" % (y_a, y_b))