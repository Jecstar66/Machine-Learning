import datetime as dt
import dateutil.parser as parser
import dateutil.relativedelta as delta

## Section 2.15 ##
Chapter = 2
Section = 15

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1 
print("\nEx 1\n")
x = dt.datetime(year=2000,month=6,day=23)
print(x.strftime("%Y년 %m월 %d일 %A"))

# Ex 2 
print("\nEx 2\n")
born = dt.datetime(year=2000,month=6,day=23)
now = dt.datetime.now()

diff = int(now.strftime("%Y%m%d")) - int(born.strftime("%Y%m%d"))
age = diff // 10000 
print("My age is %d." % age)

# Ex 3
print("\nEx 3\n")
now = dt.datetime.now()
next_birth = dt.datetime(year = now.year+1, month = 6, day = 23)
diff = next_birth - now
print("Remaining days : %d" % diff.days)
print("Remaining minutes : %d" % (diff.days*1440+diff.seconds/60))

# Ex 4
print("\nEx 4\n")
t0 = dt.datetime(year = 2000, month = 2, day = 1)
t1 = t0+delta.relativedelta(months = 1)
diff = t1 - t0
if diff.days == 29:
    print("leap year")
else:
    print("not a leap year")

t2 = dt.datetime(year = 2000, month = 3, day = 1) - dt.timedelta(days=1)
t3 = t2 + delta.relativedelta(years = 1)
print(t3.date())