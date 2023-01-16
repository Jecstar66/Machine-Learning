## Section 2.4 ##
Chapter = 2
Section = 4

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1-(1)
print("\nEx 1-(1)\n")
name = input("name : ")
age = int(input("age : "))
print("%s is %d years old\n" % (name, age))

# Ex 1-(2)
print("\nEx 1-(2)\n")
a, b = 10, 3
print("%d / %d = %.3f\n" % (a,b,a/b))

# Ex 2-(1)
print("\nEx 2-(1)\n")
a, b = 3, 12
print("'''\n%8d\nx%7d\n--------\n%8d\n'''" % (a,b,a*b))

# Ex 2-(2)
print("\nEx 2-(2)\n")
a, b = 123456, 7890
print(f"'''\n{a:>10,}\n+{b:>9,}\n----------\n{a+b:>10,}\n'''")

# Ex 3
print("\nEx 3\n")
print("{0} is {1} years old\n".format(name,age))
a, b = 10, 3
print("{} / {} = {:>.3f}\n".format(a,b,a/b))
a, b = 3, 12
print("'''\n{:>8}\nx{:>7}\n--------\n{:>8}\n'''".format(a,b,a*b))
a, b = 123456, 7890
print("'''\n{:>10,}\n+{:>9,}\n----------\n{:>10,}\n'''".format(a,b,a+b))

# Ex 4
print("\nEx 4\n")
print(f"{name} is {age} years old\n")
a, b = 10, 3
print(f"{a} / {b} = {a/b:>.3f}\n")
a, b = 3, 12
print(f"'''\n{a:>8}\nx{b:>7}\n--------\n{a*b:>8}\n'''")
a, b = 123456, 7890
print(f"'''\n{a:>10,}\n+{b:>9,}\n----------\n{a+b:>10,}\n'''")
