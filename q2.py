def docproduct(lista,lista2):
    counter=0
    a=0
    if(len(lista)==len(lista2)):
        while(counter<len(lista)):
            c=int(lista[counter])*int(lista2[counter])
            a= a+c
            counter=counter+1
    else:
        a="error"
    return a



lista=[]
t=input("Número para la lista. Escribe 'ya' para terminar la lista ")
while (t != "ya"):
    lista.append(t)
    t=input("Siguiente número ")

lista2=[]
t=input("Número para la segunda lista. Escribe 'ya' para terminar la lista ")
while (t != "ya"):
    lista2.append(t)
    t=input("Siguiente número ")

print("total: ",docproduct(lista,lista2))