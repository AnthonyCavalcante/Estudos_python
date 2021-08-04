'''1-Adicionar valores a uma lista vazia
    2- verificar se existe valores repetidos
    3- se houver valores repetidos, printar as posições'''

list= []
list.append(input("adicione um item a lista: "))
print(list)
resp=""
while True:
    resp=input("continuar adicionando? ")
    if resp !="não":
        list.append(input("adicione um item a lista: "))
        print(list)
    else:
        print("sua lista final é: "+str(list))
        print("finalizou")
        break
newlist=[]
valorRep=[]
for x,n in enumerate(list):
    while list.count(n)>1:
        newlist.append(x)
        valorRep.append(n)
        break 
if len(newlist)>1:
    print("existem")
    print("valores repetidos são: "+str(set(valorRep)).strip('{}'))
    print("a posição dos valores repetidos são: "+str(newlist).strip('[]'))
else:
    print("não existe valores repetidos")