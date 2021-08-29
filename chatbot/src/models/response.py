#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 16:43:35 2021
@author ccavalcante
"""

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


