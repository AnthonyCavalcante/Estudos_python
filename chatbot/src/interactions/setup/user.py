#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 22:37:20 2021
@author ccavalcante
"""

from utils.configuration import Configuration
from view.animations.cursor import CursorAnimation

class UserSetup:
    """
    Classe responsável por criar a interação entre o primeiro acesso do usuário e o bot
    """

    def __init__(self):

        self.__conf = Configuration.get_instance()

    def interact(self):

        if self.__conf.get('user') is not None:

            name = self.__conf.get('user')['name']

            hello_text = f'Olá {name}! Seja bem vindo de volta!\n'

            CursorAnimation.typing(hello_text)

        else:

            CursorAnimation.typing('Opa, tudo bem? Sou o Leandor\n\n') 
            
            name = CursorAnimation.typing_input('Qual o seu nome?')
            email = CursorAnimation.typing_input('E o seu email?')

            self.__conf.set('user', {'name': name, 'email': email})
            self.__conf.save()

        return self
