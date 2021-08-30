#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 22:21:13 2021
@author ccavalcante
"""

import json

SETTINGS_FILE_PATH = './resources/config/settings.json'

class Configuration:
    """
    Classe responsável por ler e salvar as configurações do sistema
    """

    __instance = None

    def __init__(self):

        if Configuration.__instance is not None:

            raise Exception('Essa classe já foi instanciada e é um Singleton,' 
                   'use a função "get_instance" para usar essa classe.')

        self.load_or_create()

        Configuration.__instance = self

    def set(self, attr, value):

        self.__data[attr] = value

        return self

    def get(self, attr):

        return self.__data.get(attr)

    def load(self):

        try:

            file = open(SETTINGS_FILE_PATH, 'r')

            self.__data = json.load(file)

            return self.__data

        except FileNotFoundError:

            return None


    def load_or_create(self):
        
        if self.load() is None:

            self.__data = {}

            self.save()

        return self

    def save(self):
        """
        Salva as configurações atuais no arquivo settings.json

        Returns
        -------
            self
        """

        with open(SETTINGS_FILE_PATH, 'w') as settings_file:
            json.dump(self.__data, settings_file, indent=2)

        return self

    @staticmethod
    def get_instance():

        if Configuration.__instance is None:
            Configuration()

        return Configuration.__instance
