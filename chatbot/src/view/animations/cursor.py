#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 22:42:53 2021
@author ccavalcante
"""

from time import sleep

class CursorAnimation:
    """
    Classe responsável pelas animações do cursor
    """

    @staticmethod
    def typing(text, typing_speed=0.03):
        """
        Printa na tela um texto como se uma pessoa estivesse escrevendo.

        Parameters
        ----------
            text: str
            typing_speed: int (Default: 0.05)

        Returns
        -------
            self
        """

        for c in text:

            print(c, end='', flush=True)

            sleep(typing_speed)

    @classmethod
    def typing_input(cls, text):
        """
        Printa na tela um texto como se uma pessoa estivesse escrevendo e retorna o input do usuário.

        Parameters
        ----------
            text: str

        Returns
        -------
            self
        """

        cls.typing(text)
        return input(' > ')
