# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:37:53 2017

@author: AILAB-PC-01
"""
import math
import random

def generate():
    x = random.uniform(-10,10)
    return x

def evaluate(x,y):
    e = (((4-(2.1*(x**2))+((x**4)/3))*(x**2))+(x*y)+((-4+(4*(y**2)))*(y**2)))
    return e

def generateNew(y):
    yy = random.uniform(-10,10)
    tempY = y + yy
    return tempY

if __name__ == '__main__':
    
    T = 9999999999
    CX = generate()
    CY = generate()

    BX = CX
    BY = CY
    Eb = evaluate(BX,BY)
    while T > 1:
        #generate new state
        NX = generateNew(CX)
        NY = generateNew(CY)
        
        #evaluate new state
        En = evaluate(NX,NY)
        #evaluate current state
        Ec = evaluate(CX,CY)
        
        if En < Ec:
            CX = NX
            CY = NY
            if En < Eb:
                BX = CX
                BY = CY
                Eb = Ec
        else:
            r = random.random()
            delE = En - Ec
            if r < math.exp(-delE/T):
                CX = NX
                CY = NY
        T = T * 0.9999

    print "X1 =",BX
    print "X2 =",BY
    print "F(X1,X2) =",Eb

        