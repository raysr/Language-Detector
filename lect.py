import os
import math
def lect(letter):
	ret={}
	lol=[]
	letter=letter.lower()
	if letter=="a":
		num=2
	if letter=="b":
		num=3

	if letter=="c":
		num=4

	if letter=="d":
		num=5

	if letter=="e":
		num=6

	if letter=="f":
		num=7

	if letter=="g":
		num=8

	if letter=="h":
		num=9

	if letter=="i":
		num=10

	if letter=="j":
		num=11

	if letter=="k":
		num=12

	if letter=="l":
		num=13

	if letter=="m":
		num=14

	if letter=="n":
		num=15

	if letter=="o":
		num=16

	if letter=="p":
		num=17

	if letter=="q":
		num=18

	if letter=="r":
		num=19

	if letter=="s":
		num=20

	if letter=="t":
		num=21

	if letter=="u":
		num=22

	if letter=="v":
		num=23

	if letter=="w":
		num=24

	if letter=="x":
		num=25

	if letter=="y":
		num=26

	if letter=="z":
		num=27


		ret["english"]=[0]
		ret["french"]=[0]
		ret["spanish"]=[0]

	f = open("frequences","r")
	lines = f.readlines()
	a = int(lines[2])
	if(os.stat("frequences").st_size)!=0:
		i=0
		b=0
		d=0
		while i<len(lines):
				b=b+1
				if b==(27*d)+1:
					lang=lines[i].rstrip()
					lol=list(ret[lang])
					d=d+1

				if b==(num+27*d):
					chiff=int(line)
					lol.append(chiff)
					ret[lang]=lol
			
			i=i+1
	
	f.close()
	return ret