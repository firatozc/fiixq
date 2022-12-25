# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:26:23 2022

@author: User
"""

liste=["-","-","-"]
liste2=["-","-","-","-"]
templist=["-","-","-","-"]
liste3=[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
liste4=[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]


def corpus1(x):
    
    print(x)
    print()
    print("|",end=" ")
    for i in range(0,4):
        print(templist[i],end=" ")         
    print("\n")
    for y in range(0,7):
        print("|",end=" ")
        for a in range(0,4):
            print(liste3[y][a],end=" ")
        
        print()
        print()

def corpus2(y):
    
    print(y)
    print()
    print("|",end=" ")
    for i in range(0,4):
        print(templist[i],end=" ")         
    print("\n")
    for y in range(0,7):
        print("|",end=" ")
        for a in range(0,4):
            print(liste4[y][a],end=" ")
        
        print()
        print()        
    
        
#corpus1(liste)

counter=0
def calculationman():
    global counter
    while True: 
        
        if liste[0]+liste[1]+liste[2]=="man":
            print(liste,"\n"+"You Won")
            counter+=1
            break
        
        corpus1(liste)
        
        a=input("Please enter a character: ")
        if a=="m":
            if liste[0]=="m":
                print("You entered the character before, point -1")
                if liste3[5][2]=="/":
                    liste3[5][3]="  \\"
                
                elif liste3[3][3]=="| \\":
                    liste3[5][2]="/"
                
                elif liste3[3][2]=="/":
                    liste3[3][3]="| \\"
                
                elif liste3[4][3]=="|":
                    liste3[3][2]="/"
                
                elif liste3[3][3]=="|":
                    liste3[4][3]="|"
                
                elif liste3[2][3]=="O":
                    liste3[3][3]="|"
                
                elif liste3[1][3]=="|":
                    liste3[2][3]="O"
                
                elif liste3[0][3]=="|":
                    liste3[1][3]="|"
                liste3[0][3]="|"
                continue
            liste[0]="m"
        elif a=="a":
            if liste[1]=="a":
                print("You entered the character before, point -1")
                if liste3[5][2]=="/":
                    liste3[5][3]="  \\"
                
                elif liste3[3][3]=="| \\":
                    liste3[5][2]="/"
                
                elif liste3[3][2]=="/":
                    liste3[3][3]="| \\"
                
                elif liste3[4][3]=="|":
                    liste3[3][2]="/"
                
                elif liste3[3][3]=="|":
                    liste3[4][3]="|"
                
                elif liste3[2][3]=="O":
                    liste3[3][3]="|"
                
                elif liste3[1][3]=="|":
                    liste3[2][3]="O"
                
                elif liste3[0][3]=="|":
                    liste3[1][3]="|"
                liste3[0][3]="|"
                continue
            liste[1]="a"
        elif a=="n":
            if liste[2]=="n":
                print("You entered the character before, point -1")
                if liste3[5][2]=="/":
                    liste3[5][3]="  \\"
                
                elif liste3[3][3]=="| \\":
                    liste3[5][2]="/"
                
                elif liste3[3][2]=="/":
                    liste3[3][3]="| \\"
                
                elif liste3[4][3]=="|":
                    liste3[3][2]="/"
                
                elif liste3[3][3]=="|":
                    liste3[4][3]="|"
                
                elif liste3[2][3]=="O":
                    liste3[3][3]="|"
                
                elif liste3[1][3]=="|":
                    liste3[2][3]="O"
                
                elif liste3[0][3]=="|":
                    liste3[1][3]="|"
                liste3[0][3]="|"
                continue
            liste[2]="n"
        else:
            print("You guess is wrong, point -1")
            
            if liste3[5][2]=="/":
                liste3[5][3]="  \\"
            
            elif liste3[3][3]=="| \\":
                liste3[5][2]="/"
            
            elif liste3[3][2]=="/":
                liste3[3][3]="| \\"
            
            elif liste3[4][3]=="|":
                liste3[3][2]="/"
            
            elif liste3[3][3]=="|":
                liste3[4][3]="|"
            
            elif liste3[2][3]=="O":
                liste3[3][3]="|"
            
            elif liste3[1][3]=="|":
                liste3[2][3]="O"
            
            elif liste3[0][3]=="|":
                liste3[1][3]="|"
            liste3[0][3]="|"
            
            if liste3[0][3]+liste3[1][3]+liste3[2][3]+liste3[3][3]+liste3[4][3]+liste3[3][2]+liste3[5][2]+liste3[5][3]=="||O| \\|//  \\":
                print("You Lost")
                corpus1(liste)
                break

            



def calculationbent():
    global counter  
    while True: 
        
        if liste2[0]+liste2[1]+liste2[2]+liste2[3]=="bent":
            print(liste2,"\n"+"You Won")
            counter+=1
            print("Your total points are",counter)
            break
    
        
        corpus2(liste2)
        
        a=input("Please enter a character: ")
        if a=="b":
            if liste2[0]=="b":
                print("You entered the character before, point -1")
                if liste4[5][2]=="/":
                    liste4[5][3]="  \\"
                
                elif liste4[3][3]=="| \\":
                    liste4[5][2]="/"
                
                elif liste4[3][2]=="/":
                    liste4[3][3]="| \\"
                
                elif liste4[4][3]=="|":
                    liste4[3][2]="/"
                
                elif liste4[3][3]=="|":
                    liste4[4][3]="|"
                
                elif liste4[2][3]=="O":
                    liste4[3][3]="|"
                
                elif liste4[1][3]=="|":
                    liste4[2][3]="O"
                
                elif liste4[0][3]=="|":
                    liste4[1][3]="|"
                liste4[0][3]="|"
                continue
            liste2[0]="b"
        elif a=="e":
            if liste2[1]=="e":
                print("You entered the character before, point -1")
                if liste4[5][2]=="/":
                    liste4[5][3]="  \\"
                
                elif liste4[3][3]=="| \\":
                    liste4[5][2]="/"
                
                elif liste4[3][2]=="/":
                    liste4[3][3]="| \\"
                
                elif liste4[4][3]=="|":
                    liste4[3][2]="/"
                
                elif liste4[3][3]=="|":
                    liste4[4][3]="|"
                
                elif liste4[2][3]=="O":
                    liste4[3][3]="|"
                
                elif liste4[1][3]=="|":
                    liste4[2][3]="O"
                
                elif liste4[0][3]=="|":
                    liste4[1][3]="|"
                liste4[0][3]="|"
                continue
            liste2[1]="e"
        elif a=="n":
            if liste2[2]=="n":
                print("You entered the character before, point -1")
                if liste4[5][2]=="/":
                    liste4[5][3]="  \\"
                
                elif liste4[3][3]=="| \\":
                    liste4[5][2]="/"
                
                elif liste4[3][2]=="/":
                    liste4[3][3]="| \\"
                
                elif liste4[4][3]=="|":
                    liste4[3][2]="/"
                
                elif liste4[3][3]=="|":
                    liste4[4][3]="|"
                
                elif liste4[2][3]=="O":
                    liste4[3][3]="|"
                
                elif liste4[1][3]=="|":
                    liste4[2][3]="O"
                
                elif liste4[0][3]=="|":
                    liste4[1][3]="|"
                liste4[0][3]="|"
                continue
            liste2[2]="n"
        elif a=="t":
            if liste2[3]=="t":
                print("You entered the character before, point -1")
                if liste4[5][2]=="/":
                    liste4[5][3]="  \\"
                
                elif liste4[3][3]=="| \\":
                    liste4[5][2]="/"
                
                elif liste4[3][2]=="/":
                    liste4[3][3]="| \\"
                
                elif liste4[4][3]=="|":
                    liste4[3][2]="/"
                
                elif liste4[3][3]=="|":
                    liste4[4][3]="|"
                
                elif liste4[2][3]=="O":
                    liste4[3][3]="|"
                
                elif liste4[1][3]=="|":
                    liste4[2][3]="O"
                
                elif liste4[0][3]=="|":
                    liste4[1][3]="|"
                liste4[0][3]="|"
                continue
            liste2[3]="t"
            
        else:
            print("You guess is wrong, point -1")
            
            if liste4[5][2]=="/":
                liste4[5][3]="  \\"
            
            elif liste4[3][3]=="| \\":
                liste4[5][2]="/"
            
            elif liste4[3][2]=="/":
                liste4[3][3]="| \\"
            
            elif liste4[4][3]=="|":
                liste4[3][2]="/"
            
            elif liste4[3][3]=="|":
                liste4[4][3]="|"
            
            elif liste4[2][3]=="O":
                liste4[3][3]="|"
            
            elif liste4[1][3]=="|":
                liste4[2][3]="O"
            
            elif liste4[0][3]=="|":
                liste4[1][3]="|"
            liste4[0][3]="|"
            
            if liste4[0][3]+liste4[1][3]+liste4[2][3]+liste4[3][3]+liste4[4][3]+liste4[3][2]+liste4[5][2]+liste4[5][3]=="||O| \\|//  \\":
                print("You Lost")
                print("Your total points are",counter)
                corpus2(liste2)
                break
            
        
                            
calculationman()            
calculationbent()
            
            
            
            
            
            

                        
    

