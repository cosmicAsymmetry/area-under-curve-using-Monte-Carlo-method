import matplotlib.pyplot as plt
from random import randint

rangex = input("Enter Range: ")
randPoints = input("Number of Random Points: ")
def firstQuadrent(rangex, randPoints):
    # 0 < x,y < infinity
    xAxis = range(0, rangex+1)
    yAxis = []
    n = 0
    sX = 0
    sY = 0
    undercurve = 0 
    upperlimit = 0
    
    def f(x):
        y = x
        return y
    
    while n <= rangex:
        if f(n) > upperlimit:
            upperlimit = f(n)
        yAxis.append(f(n))
        n+=1
    n = 0 
    while n <= randPoints:
        sX = randint(0,rangex)
        sY = randint(0, upperlimit)
        if sY <= f(sX):
            undercurve+=1
        plt.plot([sX], [sY], marker='o', markersize=3, color="red")
        n+=1
    plt.plot(xAxis, yAxis)
    plt.axis([0, rangex, 0, upperlimit])
    
    print(undercurve)
    print("Area = "+str(upperlimit * rangex * undercurve / randPoints))

def secondQuadrent(rangex, randPoints):
    # 0 < y < infinity && -infinity < x < 0
    xAxis = range(rangex,1)
    yAxis = []
    n = 0
    sX = 0
    sY = 0
    undercurve = 0 
    upperlimit = 0
    
    def f(x):
        #Abs Function
        if x > 0:
            y = x
        else:
            y = -1*x
        return y
    
    while n >= rangex:
        if f(n) > upperlimit:
            upperlimit = f(n)
        yAxis.append(f(n))
        n-=1
    n = 0 
    while n <= randPoints:
        sX = randint(rangex,0)
        sY = randint(0, upperlimit)
        if sY <= f(sX):
            undercurve+=1
        plt.plot([sX], [sY], marker='o', markersize=3, color="red")
        n+=1
    plt.plot(xAxis, yAxis)
    plt.axis([0, rangex, 0, upperlimit])
    
    print(undercurve)
    print("Area = "+str((-1)*upperlimit * rangex * undercurve / randPoints))

def thirdQuadrent(rangex, randPoints):
    # -infinity < x,y < 0
    xAxis = range(rangex, 1)
    yAxis = []
    n = 0
    sX = 0
    sY = 0
    undercurve = 0 
    lowerlimit = 0
    
    def f(x):
        y = x
        return y
    
    while n >= rangex:
        if f(n) < lowerlimit:
            lowerlimit = f(n)
        yAxis.append(f(n))
        n-=1
    n = 0 
    while n <= randPoints:
        sX = randint(rangex, 0)
        sY = randint(lowerlimit,0)
        if sY >= f(sX):
            undercurve+=1
        plt.plot([sX], [sY], marker='o', markersize=3, color="red")
        n+=1
    plt.plot(xAxis, yAxis)
    plt.axis([rangex, 0, lowerlimit, 0])
    
    print(undercurve)
    print("Area = "+str(lowerlimit * rangex * undercurve / randPoints))

def fourthQuadrent(rangex, randPoints):
    # -infinity < y < 0 && 0 < x < infinity
    xAxis = range(0, rangex+1)
    yAxis = []
    n = 0
    sX = 0
    sY = 0
    undercurve = 0 
    lowerlimit = 0
    
    def f(x):
        y = -x
        return y
    
    while n <= rangex:
         if f(n) < lowerlimit:
            lowerlimit = f(n)
         yAxis.append(f(n))
         n+=1
    n = 0 
    while n <= randPoints:
        sX = randint(0, rangex+1)
        sY = randint(lowerlimit,0)
        if sY >= f(sX):
            undercurve+=1
        plt.plot([sX], [sY], marker='o', markersize=3, color="red")
        n+=1
    plt.plot(xAxis, yAxis)
    plt.axis([rangex, 0, lowerlimit, 0])
    
    print(undercurve)
    print("Area = "+str(lowerlimit * rangex * undercurve / randPoints))
fourthQuadrent(rangex, randPoints)
"""
if rangex < 0:
    thirdQuadrent(rangex, randPoints)
else:
    firstQuadrent(rangex, randPoints)
"""
plt.show()
