## Section 2.8 ##
Chapter = 2
Section = 8

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
a,b,c,d,e = map(int,input("5 Test scores : ").split())
score = [a,b,c,d,e]
avg = 0
for i in score:
    avg += i
print("average = %f" % (avg/5))

# Ex 2 : Dictionary 는 {} 로 감싸주기
print("\nEx 2\n")
days = {"01":31, "02":28, "03":31, "04":30, "05":31, "06":30, "07":31, "08":30, "09":31, "10":30, "11":31, "12":30}
avg = 0
print("average = %f" % ((days["02"]+days["04"]+days["06"]+days["08"]+days["10"]+days["12"])/6))