import json
import sys
conocimiento = False

with open("base.json") as read_file:
	data=json.load(read_file)
conocimiento=data["conocimiento"]
	
def inicio(A,C):
	i=0
	NL=list()
	T=len(C)
	while i<T:
		D=C[i]
		if D[0]==A:
			NL.append(D)
		i+=1
	return NL

def verifica(A,B):
	for x in B:
		if A[0]==x[0] and A[1]==x[1]:
			return False
	return True

def b_profundidad(B,C,NL,N,T):
	i=0
	F=[]
	Fn=""
	L=0
	for x in NL:
		D=x
		if not D in N:
			print(D)
			N.append(D)
			if D[1]==B:
				T=True
				Fn=D
				print(main())
			else:
				NL=inicio(D[1],C)
				F= b_profundidad(B,C,NL,N,T)

		else:
			N.pop()


def profundidad(A,B):
	N=[["inicio","inicio"]]
	NL=inicio(A,conocimiento)
	b_profundidad(B,conocimiento,NL,N,False)

def main():
	print('Puedes consultar escribiendo: profundidad("<Twiter1>","<Twiter2>")')
	print("Para salir escribe 'q'")
	Terminar=False
	while not Terminar:
		Leer = input("> ")
		if Leer == 'q':
			exit()
		Imprimir = eval(Leer)
		print(Imprimir)
		
if __name__ == "__main__":
	main()



