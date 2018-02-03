# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:55:18 2018

@author: Tung
"""

dit={}
dit[3]={}
dit[3]['ty']=-3432
dit[3]['t2y']=333
dit[3]['ty3']=1
print dit[3]['ty']
print sorted(dit[3],key=lambda x:dit[3][x])[-1]