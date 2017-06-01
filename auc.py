import matplotlib.pyplot as plt
import numpy as np
from random import uniform
from bigfloat import *

def f(x):
    y = x**2
    return y

setcontext(quadruple_precision)
def monteCarloMethod(lowerbound, upperbound, randPoints, plotFunction=False):
    xAxis = np.arange(lowerbound, upperbound+1, 1).tolist()
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
        #yAxis.insert(0, f(n))
        n -= 1
    n = 1

    while n <= upperbound:
        if f(n) > upperlimit:
            upperlimit = f(n)
        #yAxis.append(f(n))
        n+= 1
    while n <= randPoints:
        #sX = randrange(lowerbound*1000, upperbound*1000+1000, increment*1000)*0.0001
        #sY = randrange(lowerlimit*1000, upperlimit*1000+1000, increment*1000)*0.0001
        sX = BigFloat(uniform(lowerbound, upperbound))
        sY = BigFloat(uniform(lowerlimit, upperlimit))
        if sY <= f(sX) and sY > 0:
            undercurve+=1
        if sY >= f(sX) and sY < 0:
            undercurve+=1
        if plotFunction:
            plt.plot([sX], [sY], marker='o', markersize=1, color="red")
        n += 1
    if plotFunction:
        # Axis
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        #-----
        plt.plot(xAxis, yAxis)
        plt.axis([lowerbound, upperbound, lowerlimit, upperlimit])
        plt.show()


    return((abs(upperlimit) + abs(lowerlimit)) * (abs(upperbound) + abs(lowerbound)) * undercurve / randPoints)

def rectangleMethod(lowerbound, upperbound, increment=0.0001, plotFunction=False):
    area = 0.0
    while lowerbound < upperbound:
        area += f(lowerbound)
        lowerbound += increment
    return(area*increment)

monteCarloCount = 0
rectangleCount = 0
i = 0.1
if __name__ == '__main__':
    mcm = 1
    am = 0
    rm = 0
    arrmcm = []
    arrrm = []
    arram = []
    for k in xrange(8):
        x = 10
        i = float(1.0/10**(k+1))
        mcm = monteCarloMethod(0, x, (x/i - x))
        rm = rectangleMethod(0, x, i)
        am = (x**3) /3
        print(k)
        arrmcm.append(mcm)
        arrrm.append(rm)
        arram.append(am)
        print mcm
    plt.plot(arrmcm,'r', label='MCM')
    plt.plot(arrrm,'b', label='RM')
    plt.plot(arram,'g', label='AM')
    plt.show()
#if __name__ == '__main__':
#    for i in xrange(7):
#        errorRectangle =  abs(rectangleMethod(-10, 10, 1.0/10**(i+1), False) - 100)
#        print("Rectangle: "+str()+str(errorRectangle))
#        errorMonteCarlo = abs( (monteCarloMethod(-10,10, 10**(i+1) ,1,False)) - 100)
#        print("Monte Carlo: "+str(errorMonteCarlo))
#        if errorMonteCarlo < errorRectangle:
#            monteCarloCount += 1
#        else: rectangleCount += 1
