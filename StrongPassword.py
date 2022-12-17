import math
import os
import random
import re
import sys


def minimumNumber(n, password):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    lower_case = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
    upper_case = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
    special_characters = "!,@,#,$,%,^,&,*,(,),-,+,".split(",")
    
    digits = 0
    lc = 0
    uc = 0
    sc = 0
    
    for i in password:
        if i in lower_case:
            lc += 1
            continue
        if i in upper_case:
            uc += 1
            continue
        if i in special_characters:
            sc +=1
            continue
        if int(i) in numbers:
            digits += 1
            continue
        
    missing_chars = 0
    min_l = 6
    diff = n - min_l
        
    if digits == 0:
        missing_chars = missing_chars + 1
    if lc == 0:
        missing_chars = missing_chars + 1
    if uc == 0:
        missing_chars = missing_chars + 1
    if sc == 0:
        missing_chars = missing_chars + 1
          
    print(missing_chars)
    if diff >= 0:
        return missing_chars
    if abs(diff) >= missing_chars:
        return abs(diff)
    if abs(diff) < missing_chars:    
        return missing_chars
        
if __name__ == '__main__':
    n = int(input().strip())

    password = input()
    answer = minimumNumber(n, password)
    print(answer)