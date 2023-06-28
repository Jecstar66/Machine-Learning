## Section 2.11 ##
Chapter = 2
Section = 11

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1
print("\nEx 1\n")
data = {
    "철수": 98,
    "영희": 80,
    "순이": 100,
    "돌이": 70,
}
avg = 0
for k, v in data.items():
  print("%s" % k, "%10d" % v)
  avg += v/len(data)
print("="*16)
print("평균", "%10.0f" % avg)