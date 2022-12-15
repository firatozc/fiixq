# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 12:22:31 2022

@author: User
"""

l=[["-","-","-"],["-","-","-"],["-","-","-"]]

def menu(liste):
    
    
    print("  " ,0,1,2)
    print("---------")
    
    for a in range(0,3):
        print(a,"|"+" ".join(l[a]))
        
menu(l)

while True:
  
    c1r=int(input("Player 1 - Please enter a row number: "))
    c1c=int(input("Player 1 - Please enter a column number: "))
    if c1r>2:
        print("it cannot be higher than 2")
        continue
    elif c1c>2:
        print("it cannot be higher than 2")
        continue
    
    if l[c1r][c1c]=="O":
        print("This space is filled with O")
        pass
        
    elif l[c1r][c1c]=="X":
        print("This space is filled with X")
        pass
    else:
        l[c1r][c1c]="O"
        menu(l)
    
    if l[0][0] + l[0][1] + l[0][2]=="OOO":
        print("player 1 wins")
        break

    elif l[1][0] + l[1][1] + l[1][2]=="OOO":
        print("player 1 wins")
        break

    elif l[2][0] + l[2][1] + l[2][2]=="OOO":
        print("player 1 wins")
        break

    elif l[0][0] + l[1][0] + l[2][0]=="OOO":
        print("player 1 wins")
        break

    elif l[0][1] + l[1][1] + l[2][1]=="OOO":
        print("player 1 wins")
        break

    elif l[0][2] + l[1][2] + l[2][2]=="OOO":
        print("player 1 wins")
        break

    elif l[0][0] + l[1][1] + l[2][2]=="OOO":
        print("player 1 wins")
        break

    counter=0
    for c in range(0,3):
        for d in range(0,3):
            if l[c][d]!="-":
                counter+=1
    if counter==9:
        print("The game finished draw")
        break
    
    
    c2r=int(input("Player 2 - Please enter a row number: "))
    if c2r>2:
       print("it cannot be higher than 2")
       continue
    c2c=int(input("Player 2 - Please enter a column number: "))       
    if c2c>2:
        print("it cannot be higher than 2")
        continue
        
    if l[c2r][c2c]=="O":
        print("This space is filled with O")
        pass
    elif l[c2r][c2c]=="X":
        print("This space is filled with X")
        pass
    else:
        l[c2r][c2c]="X"
        menu(l)
    
    
    if l[0][0] + l[0][1] + l[0][2]=="XXX":
        print("player 2 wins")
        break

    elif l[1][0] + l[1][1] + l[1][2]=="XXX":
        print("player 2 wins")
        break

    elif l[2][0] + l[2][1] + l[2][2]=="XXX":
        print("player 2 wins")
        break

    elif l[0][0] + l[1][0] + l[2][0]=="XXX":
        print("player 2 wins")
        break

    elif l[0][1] + l[1][1] + l[2][1]=="XXX":
        print("player 2 wins")
        break

    elif l[0][2] + l[1][2] + l[2][2]=="XXX":
        print("player 2 wins")
        break

    elif l[0][0] + l[1][1] + l[2][2]=="XXX":
        print("player 2 wins")
        break
    counter2=0
    for c in range(0,3):
        for d in range(0,3):
            if l[c][d]!="-":
                counter2+=1
    if counter2==9:
        print("The game finished draw")
        break
