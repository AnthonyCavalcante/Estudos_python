from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


bot = ChatBot(
    'tonyboy')

dialog = [
    'Oi', 'Opa!',
    'tudo bem?', 'tudo certinho, e vc?',
    'Vamos conversar?', 'claro! Diz ai',
    'Quero agendar uma reunião', 'certo, vou abrir a agenda'
        ]

bot.set_trainer(ListTrainer)
bot.train(dialog)

user_resp = input('User: ')
bot_resp = bot.get_response(dialog)

while user_resp != 'sair':
    if float(dialog.confidence) > 0.5:
        print('tonyboy: ', bot_resp)
    else:
        print('tonyboy: Ainda não sei responder isso')