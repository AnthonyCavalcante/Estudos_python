import time
class Response:
    def __init__(self, resp, name, email):
        self.name = name 
        self.email = email
        self.resp = resp
        
    def data_user(self):
        user_dic = {
            'name':self.name,
            'email':self.email
            }
        return "seu nome é "+user_dic.get('name')+ \
         "\nseu email é o "+user_dic.get('email') \

    def verify(self):
        return " resposta nao econtrada\n======================="


class Verify_Calendar(Response):
    def verify(self):
        self.resp_return = 1
        return 'verificando calendário'

class Schedule_Calendar(Response):
    def verify(self):
        self.resp_return = 2
        return 'agendando horário'

option={"1":Verify_Calendar, "2":Schedule_Calendar}

def data_user(name, email):
    user_dic = {
    'name':name.split()[0],
    'email':email
    }
    return "seu nome é "+user_dic.get('name')+ \
         "\nseu email é o "+user_dic.get('email') \




def main ():
    #apresentação
    print('Opa, tudo bem? Sou o CalenBot')
    name = input(f'Qual seu nome?\n')
    email = input(f'informe seu email:\n')
    time.sleep(3)
    print(data_user(name,email))
    fname = name.split()[0]

    #opções 
      
    print('Maravilha, '+ fname + '! \nVamos acessar o calendário de cláudio e trazer'+ 
            ' algumas opções\n===================')
    time.sleep(5)

    resp = input('Certo, temos as seguintes opções:'+
                    '\n[1]-Verificar calendário'+ '\n[2]-agendar horario'+
                        '\nO que você quer fazer?\n')
    
    while option.get(resp) == None:
        print('Opção não encontrada\n=======================')
        resp = input('Escolha uma das seguintes opções:'+
                    '\n[1]-Verificar calendário'+ '\n[2]-agendar horario'+
                        '\nResponda com 1 ou 2:\n')

    start_operation= option.get(resp,Response)(resp,name,email)
    print(start_operation.verify())


#função para testar pequenas variações (excluir quando terminar)
def test():
    print('Opa, tudo bem? Sou o CalenBot')
    name = input('Qual seu nome?\n')
    email = input('informe seu email:\n')
    print(data_user(name,email))
    fname = name.split()[0]

        
    



if __name__ == '__main__':
    main()    

'''
Nota:
===
    O que o bot precisa executar:
        
        0- guardar informações do usuário para usar nas ações do bot (nome ; email)
        0.1 - integrar com o calandário
        1- apresentar opções de uso: 
            verificar calendário; 
            retornar horários disponíveis
            agendar horário;
        2- receber e tratar mensagem
        3- Retornar respostas com as seguintes ações;
            verificar calendário; 
                ► retornar horários disponíveis
            agendar horário;
                ► validar resposta com disponibilidade
                ► confirmar agendamento
===
  '''