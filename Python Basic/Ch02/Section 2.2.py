## Section 2.2 ##
Chapter = 2
Section = 2 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
ans_1 = 5e8
ans_2 = 5.6e3
ans_3 = -2.1e2
ans_4 = -3.4e-1
print("Ex 1\nAns 1. %s\tAns 2. %s\tAns 3. %s\tAns 4. %s\n" % (ans_1,ans_2,ans_3,ans_4))

# Ex 2
print("Ex 2\nHand-written Question.\n")

# Ex 3
print("Ex 3\nHand-written Question.\n")

# Ex 4. Binary Representation
def ftob(x):
    ans = ""
    int_x = int(x)
    ans += ans + bin(int(x))
    if x == int_x:
        return ans
    else:
        ans += "."
        float_x = x - int_x
        while(float_x != 0):
            if float_x >= 0.5:
                ans += "1"
                float_x -= 0.5
            else:
                ans += "0"
            float_x *= 2
    return ans
        

ans_1 = bin(13)
ans_2 = bin(129)
ans_3 = ftob(0.8) 
ans_4 = ftob(1.25)
print("\nEx 4\nAns 1. %s\tAns 2. %s\tAns 3. %s\tAns 4. %s\n" % (ans_1,ans_2,ans_3,ans_4)) ## Boolean formating -> %s

