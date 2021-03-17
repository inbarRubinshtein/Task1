# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:05:17 2021

@author: inbar
"""


def exponent (x):
    num = 1.0
    power = x
    assembly=1.0
    i=1.0
    while (i<171):
        num += (power/assembly)
        power = power*x
        i+=1.0
        assembly=assembly*i
    return num

def abss(x,y):
    diff = x-y
    if diff>0.0:
        return diff
    return diff*-1.0

    
def Ln(x):
    if x>0.0:
        y_n = x-1.0
        y_n_1 = y_n+2*((x-exponent(y_n))/(x+exponent(y_n))) 
        while (abss(y_n,y_n_1)>0.001):
            y_n = y_n_1
            y_n_1 = y_n+2*((x-exponent(y_n))/(x+exponent(y_n))) 
        return y_n_1   
    return 0.0

def  XtimesY(x,y):
    if x>0.0:
        num = float('%0.6f' % exponent(y*Ln(x)))
        return num
    return 0.0

def sqrt (x,y):
    if x=0:
        return 1.0
    elif y<0:
        return 0.0
    num = float('%0.6f' % XtimesY(y,1/x))
    return num

def calculate(x):
    if x>0.0:
        cal = exponent(x)*XtimesY(7.0, x)*XtimesY(x, -1.0)*sqrt(x, x)
        return cal
    return 0.0
''''
try:
    number = float(input("Enter a number:"))
    result = calculate(float(number))
    print(result)
    
except:
    result = 0.0
    print(result)
    
    ''''''