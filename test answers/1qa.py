# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 07:17:39 2018

@author: King
"""
import pandas as pd
pd.read_csv('transactional.log',engine='python')
t=int(input())
total=0
while t!=0:
    c, n=input().split()
    n=int(n)
    if c=='D':
        total+=n
    elif c=='W':
        total-=n
    t-=1
print(total)