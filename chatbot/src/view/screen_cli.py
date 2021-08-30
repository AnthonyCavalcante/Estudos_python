#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 20:22:50 2021
@author ccavalcante
"""

import os
import sys

from art import tprint


class ScreenCliView:
    """
    Classe responsável por desenhar a tela no terminal
    """

    __instance = None

    def __init__(self):

        if ScreenCliView.__instance is not None:

            raise Exception('Use a função get_instance pra iniciar essa classe')

        ScreenCliView.__instance = self

    def clean_screen(self):
        """
        Limpa toda a tela do terminal

        Returns
        -------
            self
        """
        os.system('clear')

        return self

    def get_screen_size(fallback=(80, 24)):
        try:
            size = os.get_terminal_size(sys.__stderr__.fileno())
        except (AttributeError, ValueError, OSError):
            size = os.terminal_size(fallback)
        return size

    def draw(self):

        x, y = self.get_screen_size() 

        print('-'*x)
        tprint('  Leandor')

        print('\n' + '-'*x)

        return self
    
    def build(self):

        self.clean_screen()

        self.draw()

        return self

    @staticmethod
    def get_instance():

        if ScreenCliView.__instance is None:
            ScreenCliView()

        return ScreenCliView.__instance

