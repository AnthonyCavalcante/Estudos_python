from functions.botwhatsapp import find_command,find_contact,send_msg
import time

contact = ['Meus links']
msg = 'Testando Bot '

def main ():
    for users in contact:
        find_contact(users)
        send_msg(msg)
        com = find_command()
   
    while com != "finalizar":
        com = find_command()
        time.sleep(2)
        if com == 'teste':
            send_msg('recebendo msg corretamente')
        if com == '\calendario':
            send_msg('abrindo calendário...')
        if com == 'opa':
            send_msg('olá')    
    send_msg('bot finalizado')
    

if __name__ == '__main__':
    main()
    