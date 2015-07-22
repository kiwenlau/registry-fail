#!/usr/bin/python

import sys

imageNumber=sys.argv[1]
# each benchmark runs 3 times, each image push and pull for 10 times
baseNumber=imageNumber*3*10

def calculateRate(testNumber):
    sum = 0
    for n in testNumber :
        sum = sum + int(n.rstrip("\n"))
    #print sum
    return (sum - 870)/float(sum)

def readfile(filepath):
    f=open(filepath, "r")
    lines=f.readlines()
    f.close()
    return lines    
    
   
        

def failRate(x, y, z):
    testNumber=[]  
    testNumber=testNumber+readfile("temp0/output"+str(x)+".txt")
    testNumber=testNumber+readfile("temp0/output"+str(y)+".txt")
    testNumber=testNumber+readfile("temp0/output"+str(z)+".txt")
    #print testNumber
    print calculateRate(testNumber)

failRate(1,2,3)
failRate(4,5,6)
failRate(7,8,9)
failRate(10,11,12)
    