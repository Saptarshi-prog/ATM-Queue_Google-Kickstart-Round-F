# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:03:13 2020

@author: 91842
"""
T = int(input())
for i in range(T):
    N,X = [int(i) for i in input().split()]
    Ai = list(map(int,input().split()))
    
    B = []
    for j in range(N):
        B.append(j+1)
    
    C = []

    j=0
    
    while len(B)>0:
        if Ai[j]<=X:
            C.append(B[j])
            B.remove(B[j])
            Ai.remove(Ai[j])
        else:
            x = B[j]
            y = Ai[j]
            B.remove(x)
            Ai.remove(y)
            
            B.append(x)
            Ai.append(y-X)
    D = " ".join(map(str,C))
    
    print("Case #"+str(i+1)+": "+D)
