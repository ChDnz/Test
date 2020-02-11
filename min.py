l=[3,7,2,1,10] #min  è 1

min=l[3]
for elem in l:
    if elem<min:
        min=elem

print(min)


l=[3,7,2,1,10,40,33,11,54]
ricerca=int(input('inserisci elemento da caricare: \n'))
cont=0
for elem in l:
    if elem==ricerca:
        print('ho trovato numero: \n'+str(cont+1))
        break

        cont+=1
