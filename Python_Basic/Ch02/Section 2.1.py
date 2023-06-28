## Section 2.1 ##
Chapter = 2
Section = 1 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
ans_1 = 3*2-8/4
ans_2 = 25*6/3+17
ans_3 = 39021 - 276920 / 12040
ans_4 = pow(2,6) - 10%6
print("Ex 1\nAns 1. %d\tAns 2. %d\tAns 3. %d\tAns 4. %d\n" % (ans_1,ans_2,ans_3,ans_4))

# Ex 2
ans_1 = 12-(5*7+1)
ans_2 = 5*(8+(10-6)/2)
ans_3 = 48320 - ((365-5*9)/16)*987
ans_4 = pow(((pow(3,4) - 3*7) % 5 + 4),2)
print("Ex 2\nAns 1. %d\tAns 2. %d\tAns 3. %d\tAns 4. %d\n" % (ans_1,ans_2,ans_3,ans_4))

# Ex 3
ans_1 = (3>0,2!=3,1<=2)
ans_2 = (2==4,2<1,0!=0)
print("Ex 3")
print(ans_1 + ans_2)

# Ex 4
ans_1 = (5<=6) & (3==4)
ans_2 = (2!=1) | (3>=4)
ans_3 = (5<=6) & ((0==0)|(3<4))
print("\nEx 4\nAns 1. %s\tAns 2. %s\tAns 3. %s\n" % (ans_1,ans_2,ans_3)) ## Boolean formating -> %s

# Ex 5
print("Ex 5")
x, y, z, j, k, i = map(int, input("Insert the numbers : ").split()) ## Integer Inputs -> Using map function
ans_1 = pow(2*x-1,2)+1
ans_2 = pow(x,2*y)*(z+10)
ans_3 = ((j==0) & (0<k)) | (i<=100)
print("Ans 1. %s\tAns 2. %s\tAns 3. %s" % (ans_1,ans_2,ans_3))
