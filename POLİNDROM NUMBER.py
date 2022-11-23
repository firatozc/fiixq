# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:47:13 2022

@author: User
"""

Number=int(input("please enter the number: "))
temp=Number
reversenumber=0
Numbernew=Number
while Number>0:
    
     a=int(temp%10)
     temp=Number/10
     reversenumber=reversenumber*10+a
     Number=int(temp)
     
     
if Numbernew==reversenumber:
    print(Numbernew,"sayısı polindrom sayıdır")
    
else:
    print(Numbernew,"sayısı polindrom sayı değildir")

