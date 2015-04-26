def threes(lista):
	t=0
	for i in lista:
		i=float(i)
		if(i/3 == int(i/3)):
			t=t+i
	return int(t)
	
lista=[]
w=input("Número para la lista. Escribe 'ya' para terminar la lista ")
while(w!= "ya"):
	lista.append(w)
	w=input("dime el numero")
	
#lista= [0,6,9,3,12]
print("total: " ,threes(lista))
