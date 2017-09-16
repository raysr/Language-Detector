from lect import lect
import statistics
from numpy import mean
from math import sqrt
def equa(carr,x):	# Droite des moindres carrés
 	y=0
 	ler=[]
 	for b in lect(carr)["english"]:
 		ler.append(b*0.25)
 	for b in lect(carr)["french"]:
 		ler.append(b*0.5)
 	for b in lect(carr)["spanish"]:
 		ler.append(b*1)

 	moyxy=mean(ler)
 	ber=[]
 	ber.append(mean(lect(carr)["english"]))
 	ber.append(mean(lect(carr)["french"]))
 	ber.append(mean(lect(carr)["spanish"]))
 	moyx=mean(ber)



 	der=[]
 	der.append(len(lect(carr)["english"])*0.25)
 	der.append(len(lect(carr)["french"])*0.5)
 	der.append(len(lect(carr)["spanish"])*1)
 	moyy=mean(der)
 	

 	ler=[]
 	for b in lect(carr)["english"]:
 		ler.append(b)
 	for b in lect(carr)["french"]:
 		ler.append(b)
 	for b in lect(carr)["spanish"]:
 		ler.append(b)

 	moycarrx=mean(ler)
 	moyxcarr=sqrt(moyx)



 	m=(moyxy-moyx*moyy)/(moycarrx-moyxcarr)
 	b=moyy-m*moyx
 	return (m*x)+b



def reseau(group):
	lu=[]
	lu.append(neurA(group['a']))
	lu.append(neurB(group['b']))
	lu.append(neurC(group['c']))
	lu.append(neurD(group['d']))
	lu.append(neurE(group['e']))
	lu.append(neurF(group['f']))
	lu.append(neurG(group['g']))
	lu.append(neurH(group['h']))
	lu.append(neurI(group['i']))
	lu.append(neurJ(group['j']))
	lu.append(neurK(group['k']))
	lu.append(neurL(group['l']))
	lu.append(neurM(group['m']))
	lu.append(neurN(group['n']))
	lu.append(neurO(group['o']))
	lu.append(neurP(group['p']))
	lu.append(neurQ(group['q']))
	lu.append(neurR(group['r']))
	lu.append(neurS(group['s']))
	lu.append(neurT(group['t']))
	lu.append(neurU(group['u']))
	lu.append(neurV(group['v']))
	lu.append(neurW(group['w']))
	lu.append(neurX(group['x']))
	lu.append(neurY(group['y']))
	lu.append(neurZ(group['z']))

	meh=mean(lu)
	if 0.25<meh:
		if 0.5<meh:
			if meh==1:
				return 1
			elif 1-meh<meh-0.5:
				return 1
			else:
				return 0.5

		elif meh==0.5:
			return 0.5

	elif 0.5-meh<meh-0.25:
			return 0.5
	else: 
			return 0.25



def neurA(x):

 	return equa('a',x)



def neurB(x):

 	return equa('b',x)

def neurC(x):
 	return equa('c',x)



def neurD(x):
 	return equa('d',x)



def neurE(x):
 	return equa('e',x)



def neurF(x):
 	return equa('f',x)



def neurG(x):
 	return equa('g',x)



def neurH(x):
 	return equa('h',x)



def neurI(x):
 	return equa('i',x)



def neurJ(x):
 	return equa('j',x)



def neurK(x):
 	return equa('k',x)



def neurL(x):
 	return equa('l',x)



def neurM(x):
 	return equa('m',x)



def neurN(x):
 	return equa('n',x)



def neurO(x):
 	return equa('o',x)



def neurP(x):
 	return equa('p',x)



def neurQ(x):
 	return equa('q',x)



def neurR(x):
 	return equa('r',x)



def neurS(x):
 	return equa('s',x)



def neurT(x):
 	return equa('t',x)



def neurU(x):
 	return equa('u',x)



def neurV(x):
 	return equa('v',x)



def neurW(x):
 	return equa('w',x)



def neurX(x):
 	return equa('x',x)



def neurY(x):
 	return equa('y',x)



def neurZ(x):
 	return equa('z',x)



