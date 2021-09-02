import random
import json
import time
with open('game\categories.json') as f:
    ler = f.read()

categ = json.loads(ler)

resp_select = {'1':'animal', '2':'carro', '3':'pais', '4':'personagem'}

def select_group(ent):

    list = resp_select.get(ent)
    group = categ.get(list)
    return random.choice(group)

def start_game(key,categ):
    keyword =  key
    list = resp_select.get(categ)
    hide_keyword = "_ "*len(keyword)
    list_keyword = []
    for letters in keyword:
        list_keyword.append(letters)


    select_hide = hide_keyword.split(' ')
    select_word = []
    index_select_word = []
    print(hide_keyword)
    print ( 'É um {} com '.format(list) +str(len(keyword))+ ' letras\n')
    print('Você tem 3 chances!')
    
    for x,y in enumerate(list_keyword):
        select_word.append(y)
        index_select_word.append(x)    

    life = 0
    while len(index_select_word)>0 and life < 3:
        letter = input('insira uma letra:\n')
        

        if select_word.count(letter) >=1:
            
   
            while select_word.count(letter) >=1:
                time.sleep(0.5)
                w= select_word.index(letter)
                
                select_word.remove(letter)
                select_word.insert(w, '*')
                select_hide.pop(w)
                select_hide.insert(w, letter)
                index_select_word.pop(0)

                print(''.join(select_hide))
                
        elif select_hide.count(letter) >=1:
            print('já tem')
            print(''.join(select_hide))
        else:
            print('não tem')
            life += 1
            print('quantidade de erros:  ' +str(life))
            print(''.join(select_hide)) 
        
        
    if len(index_select_word) == 0 :
        print('Parabéens! Você conseguiu!!! Você é bala!!')
        
    else:
        print ('Que pena! Suas vidas acabaram.\nA palavra era: ' +  keyword)

'''resp = input('escolha uma categoria:\n1- animal\n2- carro\n3- pais\n4-disney\nEscolhe um número:\n')
list = resp_select.get(resp)
group_selected = select_group(resp)
x = random.choice(categ.get(list))
print(list)
print(group_selected)
print(len(group_selected))
print(start_game(group_selected,resp))
'''