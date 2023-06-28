import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager

## git commit practice ##
## Section 5.1 ##
Chapter = 5
Section = 1 

print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# Ex 1
print("\nEx 1\n")

plt.title("Ex 5.1.1")
X = np.linspace(-np.pi,np.pi,50)
Y = np.cos(X)
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(X,Y,"ro--",label = "Y")
plt.grid(True)
Y2 = 2*np.cos(X)
Y3 = -3*np.cos(X)
plt.plot(X,Y2,"bD-.",label = "Y2")
plt.plot(X,Y3,"gs:",label = "Y3") 

plt.legend()
plt.show()

# Ex 2
print("\nEx 2\n")

def plt_setting():
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    
plt.title("Ex 5.1.2")
X = np.linspace(-np.pi,np.pi,50)
Y = np.cos(X)

plt.subplot(3,1,1)
plt.plot(X,Y,"ro--",label = "Y")
plt_setting()

Y2 = 2*np.cos(X)
Y3 = -3*np.cos(X)

plt.subplot(3,1,2)
plt.plot(X,Y2,"bD-.",label = "Y2")
plt_setting()

plt.subplot(3,1,3)
plt.plot(X,Y3,"gs:",label = "Y3") 
plt_setting()


plt.show()

# Ex 3
print("\nEx 3\n")
# http://matplotlib.org/gallery.html