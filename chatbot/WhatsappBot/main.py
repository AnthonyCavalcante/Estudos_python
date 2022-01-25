from functions.interactions import find_command,send_msg, read_first_contacts,end_bot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import json
#creating bot intelligent and responses training

botleandor = ChatBot('Leandor')
trainer = ListTrainer(botleandor)

# read responses 
with open ('docs\\botresponses.json',  encoding='utf-8') as f:
        read_j= f.read()

with open ('docs\\responsechatterbot.json', encoding='utf-8') as j:
    read_response = j.read()
     
def main ():
       
    dic_resp = json.loads(read_j)
    cond = ''
    while cond != 'finalizar' :
        
        for rotate in range(5,11):
            
            time.sleep(0.5)
            read_first_contacts(rotate)

            com = find_command()
            resp = dic_resp.get(com)
            
            if resp != None: 
                send_msg(resp)
            
            if resp == 'bot finalizado': 
                time.sleep(2)
                cond = 'finalizar'
                break
    end_bot()

def test ():
       
    dic_resp = json.loads(read_response).get('dialog') 
    trainer.train(dic_resp)
   
    cond = ''
    while cond != 'finalizar' :
        
        for rotate in range(8,11):
            
            time.sleep(0.5)
            read_first_contacts(rotate)

            com = find_command()
            resp = botleandor.get_response(com)
            
            if float(resp.confidence) > 1: 
              #corrigir a resposta para enviar ao whatsapp 
                send_msg(str(resp))
            
            if com == 'finalizar': 
                time.sleep(2)
                cond = 'finalizar'
                break

            else:
                cond = ''
    end_bot()


if __name__ == '__main__':
    main()
    