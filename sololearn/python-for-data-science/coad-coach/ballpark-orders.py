menu = {'Nachos': 6, 'Pizza': 6, 'Cheeseburger': 10, 'Water': 4, 'Coke': 5}
tax = 0.07


req = [ i for i in input().split(' ')]
req_valor = [menu.get(i, 5) for i in req]
total = sum(req_valor) + (sum(req_valor)*tax) 
print(total)
 
