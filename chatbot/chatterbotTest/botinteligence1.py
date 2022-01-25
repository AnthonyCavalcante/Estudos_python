from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('tonybot')

trainer = ListTrainer(chatbot)

import json
with open('responsetrain.json', encoding= 'utf-8') as f:
        read_json = f.read()

dialog = json.loads(read_json).get("dialogo")

trainer.train(dialog)



while True:
        resp = input ('você: ')
        response = chatbot.get_response(resp)
        
        if resp =='sair':
                break
        if float(response.confidence ) >0.5:
                print ('Tonybot: ', response)
        else: 
                print( 'não tenho resposta para isso')