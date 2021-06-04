import json
import random

with open("mapamario.json") as base:
	rutas=json.load(base)
conocimiento=rutas["camino"]
	
def nodo(I,N,C): #metodo 
	NL=[] #arreglo
	i=0
	t=len(C)
	while i<t:
		D=C[i]
		if D[0]==I:
			if not (D[0] in N or D[2] in N):
				NL.append(D)
		i+=1
	return NL

def recorri(F,C,NL,L):
	i=1
	leng=len(NL)
	D=NL[0]
	print(D[0])
	dF=D
	cF=D[1]
	c1=0
	c2=0
	while i<leng:
		D=NL[i]
		c1=D[1]
		if c1==cF:
			r=round(random.random())
			if r:
				cF=c1
				dF=D
		if F==D[2]:
			print(F)
			main()
		if c1<cF:
			cF=c1
			dF=D
		c2=c1
		i+=1
	L.append(dF[0])
	if F==dF[2]:
		print(F)
		main()
	else:
		NL=nodo(dF[2],L,C)
		recorri(F,C,NL,L)

def recorrido(I,F):
	N=[["",""]]
	print("Recorrido: \n")
	NL=nodo(I,N,conocimiento)
	recorri(F,conocimiento,NL,N)
	
unico=[]
def lugares(c):
	for lugar in c:
		if not lugar[0] in unico:
			unico.append(lugar[0])
	return unico

def main():
	print("Bienvenido a este programa")
	print("Lugares:\n",lugares(conocimiento),'\nPara realizar un recorrido escribe: recorrido("<Inicio>","<Fin>")')
	print("Para terminar el programa escribe 'q'")
	terminar=False
	while not terminar:
		entrada = input("> ")
		if entrada == 'q':
			exit()
		print(eval(entrada))
		
if __name__ == "__main__":
	main()
