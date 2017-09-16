import os   
from neurones import *
from numpy import mean

from string import ascii_lowercase


os.chdir("/home/moubarak/Documents/IA/DetectLangue")

naze="false"

while naze:


    text=input("Write your text :")
    frequAct={}

    for c in ascii_lowercase:
	       frequAct[c]=0


    i=0
    while(i<len(text)):
  	     if text[i]!= ' ':
	           frequAct[text[i].lower()]=frequAct[text[i].lower()]+(1/len(text))
  	
  	     i=i+1

    for b in ascii_lowercase:
	       print("Frequence ",b,frequAct[b])
    

    stock=0
    r=0





    with open("frequences","a") as fich:
        poss=reseau(frequAct)
        print("The language used is : ")
        if poss==0.25:
            print("English")
        if poss==0.5:
    	       print("French")
        if poss==1: 
    	       print("Spanish")

        stock=poss

        correct=input("True ?")
        if correct.lower()=="yes":
    	       print("Well done !")

        else:
            answer=input("so what was the language ?")
            if answer.lower()=="english":
                stock=0.25
            if answer.lower()=="french":
                stock=0.5
            if answer.lower()=="spanish":
                stock=1
    
        if stock==0.25:
            dom="english"
        if stock==1:
            dom="spanish"  
        if stock==0.5:
            dom="french"
        fich.write(dom)
        fich.write("\n")
        for a in frequAct:
            fich.write(str(frequAct[a]))
            fich.write("\n")
        fich.close()