#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 20:15:25 2021
@author ccavalcante
"""

from pydantic import BaseModel

class UserModel(BaseModel):
    """
    Model responsável por manter as informações de usuário
    """

    name: str = Field(description='Nome do usuário')
    email: str = Field(None, description='Email do usuário')

