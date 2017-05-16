import matplotlib.pyplot as plt
import numpy as np
from random import randint

lowerbound = input("Enter lower bound: ")
upperbound = input("Enter upper bound: ")
randPoints = input("Number of Random Points: ")

xAxis = range(lowerbound, upperbound+1)
yAxis = []
sX = 0
sY = 0
undercurve = 0 
upperlimit = 0
lowerlimit = 0
n = 0
def f(x):
    y = x
    return y
#------
while n >= lowerbound:
    if f(n) < lowerlimit:
        lowerlimit = f(n)
    yAxis.insert(0, f(n))
    n-=1
n = 1  
#------
while n <= upperbound:
    if f(n) > upperlimit:
        upperlimit = f(n)
    yAxis.append(f(n))
    n+=1
n = 0

while n <= randPoints:
    sX = randint(lowerbound,upperbound)
    sY = randint(lowerlimit, upperlimit)
    if sY <= f(sX) and sY > 0:
        undercurve+=1
    if sY >= f(sX) and sY < 0:
        undercurve+=1
    plt.plot([sX], [sY], marker='o', markersize=3, color="red")
    n+=1
#-----Axis
x = np.linspace(0.2,10,100)

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
#-----
plt.plot(xAxis, yAxis)
plt.axis([lowerbound, upperbound, lowerlimit, upperlimit])

print(undercurve)
print(abs(upperlimit) + abs(lowerlimit))
print(abs(upperbound) + abs(lowerbound))
print(undercurve / randPoints)
print(randPoints)
print("Area = "+str((abs(upperlimit) + abs(lowerlimit)) * (abs(upperbound) + abs(lowerbound)) * undercurve / randPoints))
plt.show()