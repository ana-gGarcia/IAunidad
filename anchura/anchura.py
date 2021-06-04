import json
import sys
conocimiento = False


with open("conocimiento.json") as read_file:
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

def check(A,B):
	for x in B:
		if A[0]==x[0] and A[1]==x[1]:
			return False
	return True

def b_anchura(B,C,NL,N,T):
	i=0
	F=[]
	Fn=""
	L=0
	for x in NL:
		D=x
		print (D)
		if D[1]==B:
			Fn=D
			print(main())
		i+=1
		#print(i)
	for y in NL:
		if not y in N:
			#print(D)
			N.append(y)
			NL=inicio(y[1],C)
			F= b_anchura(B,C,NL,N,T)
		else:
			N.pop()

def anchura(A,B):
	N=[["inicio","inicio"]]
	NL=inicio(A,conocimiento)
	b_anchura(B,conocimiento,NL,N,False)

def main():
	print('Puedes consultar escribiendo: anchura("<Twiter1>","<Twiter2>")')
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
