## Section 2.10 ##
Chapter = 2
Section = 10

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
grade = [4,3,2,3,4]
weight = [3,3,1,2,2]
GPA = 0
for (X,W) in zip(grade,weight):
    GPA += X*W
GPA /= sum(weight)
print("GPA = %.2f" % GPA)

# Ex 2
print("\nEx 2\n")
X = [6,5,4,7,3,5]
avg = sum(X)/len(X)
var = 0
for x in X:
    var += pow(x-avg,2)/len(X)

print("var = %.2f" % var)

# Ex 3
print("\nEx 3\n")
x = [
  ["길동", 90],
  ["철수", 80],
  ["영수", 70],
  ["방자", 60],
]
print(list(zip(*x))[0])
# Additional Sol.
# x = [
# ["길동", 90],
# ["철수", 80],
# ["영수", 70],
# ["방자", 60],
# ]
# x1, x2, x3, x4 = x
# x14 = list(zip(x1, x2, x3, x4))
# name, score = x14 
