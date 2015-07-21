#!/usr/bin/python

def failRate(x, y, z):
    testNumber=[]
    filepath="temp0/output"+str(x)+".txt"
    f=open(filepath, "r")
    testNumber=testNumber+f.readlines()
    f.close()
    filepath="temp0/output"+str(y)+".txt"
    f=open(filepath, "r")
    testNumber=testNumber+f.readlines()
    f.close()
    filepath="temp0/output"+str(z)+".txt"
    f=open(filepath, "r")
    testNumber=testNumber+f.readlines()
    f.close()
    print testNumber

failRate(1,2,3)
    