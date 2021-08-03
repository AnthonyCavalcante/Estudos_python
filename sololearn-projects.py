n=input("insira um valor:")
lista=list(range(1,int(n)))
print("os valores são "+str(lista))
for valor in lista:
    if valor%2==0:
        continue
    elif valor%3==0 and valor%5==0:
        print("sololearn")
    elif valor%5==0:
        print("learn")
    elif valor%3==0:
        print("solo")
    else:
        print("rola")
