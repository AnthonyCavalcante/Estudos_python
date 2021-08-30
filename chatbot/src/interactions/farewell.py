#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 23:14:23 2021
@author ccavalcante
"""

from view.animations.cursor import CursorAnimation
from utils.configuration import Configuration

class Farewell:

    def __init__(self):
        self.__conf = Configuration.get_instance() 

    def interact(self):

        CursorAnimation.typing('\nAté logo!\n')
        



