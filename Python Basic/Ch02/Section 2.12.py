## Section 2.12 ##
Chapter = 2
Section = 12

print("\n<Section {0}.{1}>\n".format(Chapter, Section))
# Ex 1 : OOP
print("\nEx 1\n")
class triangle:
  def __init__(self,b,h):
    self.b = b
    self.h = h
    
  def area(self):
    return 1/2*self.b*self.h

A = triangle(6,3)
print(A.area)   # method에 대한 정보 (object의 메모리상 위치, method 명 등)
print(A.area()) # method 결과 값이 나옴!!

# Reference. Python의 Garbage Collection(GC)
# https://velog.io/@zihs0822/Python%EC%9D%98-GC%EC%99%80-GIL

# Ex 2
print("\nEx 2\n")
class Square_Prism:
  def __init__(self,a,b,h):
    self.a = a
    self.b = b
    self.h = h
    
  def volume(self):
    return self.a*self.b*self.h

  def surface(self):
    return 2*(self.a*self.b+self.b*self.h+self.h*self.a)
  
B = Square_Prism(b=3,a=4,h=5) # Variable의 순서(order)를 argument 상에서 바꿀 수 있다.
print(B.volume())
print(B.surface())
print(B.b)

# Ex 3 : Method Overriding
print("\nEx 3\n")
class Character(object):

    def __init__(self):
        self.life = 1000
        self.strength = 10
        self.intelligence = 10

    def attacked(self):
        self.life -= 10
        print("공격받음! 생명력 =", self.life)

    def attack(self):
        print("공격!")
  
class Warrior(Character):

    def __init__(self):
        super(Warrior, self).__init__()
        self.strength = 15
        self.intelligence = 5

    def attacked(self):
        self.life -= 8
        print("공격받음! 생명력 =", self.life)
        
    def attack(self):
        print("육탄 공격!")
        
class Wizard(Character):

    def __init__(self):
        super(Wizard, self).__init__()
        self.strength = 5
        self.intelligence = 15
        
    def attacked(self):
        self.life -= 12
        print("공격받음! 생명력 =", self.life)
        
    def attack(self):
        print("마법 공격!")

Kris = Warrior()
Kris.attacked()

# Ex 4 
print("\nEx 4\n")
class Car:
  def __init__(self):
    self.max_speed = 160
    self.speed = 0
  
  def speed_up(self):
    if self.speed + 20 <= self.max_speed:
      self.speed += 20
      print("Current speed = %d" % self.speed)
    else:
      self.speed = self.max_speed
      print("Current speed = %d" % self.speed)
            
  def speed_down(self):
    if self.speed - 20 >= 0:
      self.speed -= 20
      print("Current speed = %d" % self.speed)
    else:
      self.speed = 0
      print("Current speed = %d" % self.speed)

C = Car()
C.speed_up()
C.speed_down()


# Ex 5
print("\nEx 5\n")
class SportCar(Car):
  def __init__(self):
    super(SportCar,self).__init__()
    self.max_speed = 200
  
  def speed_up(self):
    if self.speed + 45 <= self.max_speed:
      self.speed += 45
      print("Current speed = %d" % self.speed)
    else:
      self.speed = self.max_speed
      print("Current speed = %d" % self.speed)
  
  def speed_down(self):
    if self.speed - 45 >= 0:
      self.speed -= 45
      print("Current speed = %d" % self.speed)
    else:
      self.speed = 0
      print("Current speed = %d" % self.speed)

class Truck(Car):
  def __init__(self):
    super(Truck,self).__init__()
    self.max_speed = 100
  
  def speed_up(self):
    if self.speed + 15 <= self.max_speed:
      self.speed += 15
      print("Current speed = %d" % self.speed)
    else:
      self.speed = self.max_speed
      print("Current speed = %d" % self.speed)
  
  def speed_down(self):
    if self.speed - 15 >= 0:
      self.speed -= 15
      print("Current speed = %d" % self.speed)
    else:
      self.speed = 0
      print("Current speed = %d" % self.speed)

S = SportCar()
S.speed_up()
S.speed_down()
T = Truck()
T.speed_up()
T.speed_down()    

# Ex 6. Special Method
print("\nEx 6\n")
class Student:
  def __init__(self, ID, name, math, eng):
    self.ID = ID
    self.name = name
    self.math = math
    self.eng = eng
  
  def __repr__(self):
    return "%s  %10d" % (self.name, self.ID)
    
  def __str__(self):
    return self.name
  
  def __getitem__(self,subject):
    if subject == "math":
      return self.math
    if subject == "english":
      return self.eng
    
  def avg(self):
    print (self.math + self.eng) / 2
    
obj = Student(20190106,"Jack",100,80)

print(repr(obj)) # VSCODE는 repr을 써야 __repr__ method가 호출됨. Jupyter 환경은 아닌 듯...
print(str(obj))
print(obj["math"]) # Index에 접근 시 자동으로 __getitem__ method 호출.
  
