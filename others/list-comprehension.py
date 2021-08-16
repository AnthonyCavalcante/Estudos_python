'''1-Adicionar valores a uma lista vazia
    2- verificar se existe valores repetidos
    3- se houver valores repetidos, printar as posições'''

def main():
    """
    Nota :
    ------
        O nome da varável q vc usou aqui 'list' está fora dos padrões de boas práticas pra criar
    variáveis. list, dict, str ou qualquer tipo primitivo de qualquer linguagem é errado, então
    to atualizando pra 'my_list'
    """

    #list= []
    #list.append(input("adicione um item a lista: "))
    #print(list)

    my_list = []
    my_list.append(input("adicione um item a lista: "))
    print(my_list)
    resp=""
    while True:
        resp=input("continuar adicionando? ")
        if resp !="não":
            list.append(input("adicione um item a lista: "))
            print(list)
        else:
            print("sua lista final é: "+str(my_list))
            print("finalizou")
            break
    newlist=[]
    valorRep=[]
    for x,n in enumerate(my_list):
        while list.count(n)>1:
            newlist.append(x)
            valorRep.append(n)
            break 
    if len(newlist)>1:
        print("valores repetidos são: "+str(set(valorRep)).strip('{}'))
        print("a posição dos valores repetidos são: "+str(newlist).strip('[]'))
    else:
        print("não existe valores repetidos")


def while_using_resp_input():
    """
    Essa é uma outra forma de usar o 'resp' e evitar o 'while True' no código.

    Nota 1:
    -----
        Para executar essa função, basta substituir a função 'main()' no if abaixo por essa função
    aqui.

    Nota 2:
    -------
        Criei um outro exemplo de como contar os valores repetidos usando dicionário
    """

    my_list = []
    continuar = None
    repeticoes = {}
    index = 0

    while continuar != 'não':
        resp = input('Adicione um item a lista: ')

        my_list.append(resp)

        if repeticoes.get(resp) is None:
            repeticoes[resp] = []

        repeticoes[resp].append(index)
        index += 1

        continuar = input('Continuar adicionando?[sim/nâo]: ') 

    repetidos = [ (valor, indices) for valor, indices in repeticoes.items() if len(indices) > 1 ]

    print('Sua lista final é: ' + str(my_list))

    if len(repetidos) == 0:
        print('não existem valores repetidos!')

    else:
        print('Seus valores repetidos:')

        print('-'*80)
        print('Valor | Total | Indices')
        print('-'*80)
        for valor, indices in repetidos:
            print(valor + ' |  ' + str(len(indices)) + ' |  ' + str(indices)  )

    print('Finalizou')


if __name__ == '__main__':
    """
    Essa é a maneira mais correta de criar scripts que executam direto do terminal como vc está
    fazendo. O ideal é criar as funções do lado de fora do main, adicionar a função 'main()' e
    então chamar a função main aqui dentro.
    """

    #while_using_resp_input()

    main()
