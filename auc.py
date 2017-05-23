import matplotlib.pyplot as plt
import numpy as np
from random import randrange

def f(x):
    y = x
    return y

def monteCarloMethod(lowerbound, upperbound, randPoints, increment, plotFunction=True):
    xAxis = np.arange(lowerbound, upperbound+increment, increment).tolist()
    yAxis = []
    sX = 0.0
    sY = 0.0
    undercurve = 0.0 
    upperlimit = 0.0
    lowerlimit = 0.0
    n = 0.0
    
    while n >= lowerbound:
        if f(n) < lowerlimit:
            lowerlimit = f(n)
        yAxis.insert(0, f(n))
        n-= increment
    n = increment  
    
    while n <= upperbound:
        if f(n) > upperlimit:
            upperlimit = f(n)
        yAxis.append(f(n))
        n+= increment
    n = 0
    
    while n <= randPoints:
        sX = randrange(lowerbound*100, upperbound*100+100, increment*100)*0.01
        sY = randrange(lowerlimit*100, upperlimit*100+100, increment*100)*0.01
        if sY <= f(sX) and sY > 0:
            undercurve+=1
        if sY >= f(sX) and sY < 0:
            undercurve+=1
        if plotFunction:
            plt.plot([sX], [sY], marker='o', markersize=1, color="red")
        n += increment
    if plotFunction:
        # Axis
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        #-----
        plt.plot(xAxis, yAxis)
        plt.axis([lowerbound, upperbound, lowerlimit, upperlimit])
        plt.show()
    

    return((abs(upperlimit) + abs(lowerlimit)) * (abs(upperbound) + abs(lowerbound)) * undercurve / randPoints)

def rectangleMethod(lowerbound, upperbound, increment=0.0001, plotFunction=True):
    area = 0.0
    while lowerbound < upperbound:
        area += abs(f(lowerbound)*increment)
        lowerbound += increment
    return(area)

monteCarloCount = 0
rectangleCount = 0
if __name__ == '__main__':
    for i in xrange(7):
        errorRectangle =  abs(rectangleMethod(-10, 10, 1.0/10**(i+1), False) - 100)
        print("Rectangle: "+str()+str(errorRectangle))
        errorMonteCarlo = abs( (monteCarloMethod(-10,10, 10**(i+1) ,1,False)) - 100)
        print("Monte Carlo: "+str(errorMonteCarlo))
        if errorMonteCarlo < errorRectangle:
            monteCarloCount += 1
        else: rectangleCount += 1

