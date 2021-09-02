import random
import time
from game.change_word import select_group, start_game

def main():

    print(' Olá, vamos jogar o JUEGO DE LÁ FUERCA!!!\n')
    time.sleep(2)
    
    resp = input('escolha uma categoria:\n1- animal\n2- carro\n3- pais\n4-disney\nEscolhe um número:\n')
    
    
    time.sleep(0.4)
    try:
        key = select_group(resp)
        start_game(key,resp)
    except TypeError:
        print('escolha errada parça!')
    restart = input('Vamos Jogar novamente?[sim/não]\n')
    
    while restart!="não":
        resp2 = input('escolha uma categoria:\n1- animal\n2- carro\n'
        '3- pais\n4-personagem\nEscolhe um número:\n')
        try:
            key = select_group(resp)
            start_game(key,resp)
        except TypeError:
            print('escolha errada meu parceiro')
        restart = input('Vamos Jogar novamente?[sim/não]\n')
        
    print('Até a próxima!!')

#def test():
  
   
if __name__ == '__main__':
    main()
