## Section 2.7 ##
Chapter = 2
Section = 7

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
for i in range(1,11):
    print("*"*i)

# Ex 2
print("\nEx 2\n")
for i in range(10,0,-1):
    print("*"*i)

# Ex 3
print("\nEx 3\n")
for i in range(1,20):
    print("*"*min(i,20-i))
  
# Ex 4
print("\nEx 4\n")
for i in range(11):
    print(f"{'*'*min(2*i+1,21-2*i):^11}")

# Ex 5
print("\nEx 5\n")
day1 = 1024
list = list()
for i in (2,0.5):
    for j in (2,0.5):
        for k in (2,0.5):
            list.append(int(day1*i*j*k))
print(list)
       
# Ex 6
print("\nEx 6\n")
flag = False
for a in (1,11):
    for b in (1,11):
        for c in (1,11):
            if a**3+b**3 == c**3:
                flag = True
                print("clap!")
if flag == False:
    print("Nothing happens...")
    
# Ex 7
print("\nEx 7\n")
n = int(input("n = "))
sum = 0
temp = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        temp += j
    sum += temp
    temp = 0
print("sum = %d" % sum)