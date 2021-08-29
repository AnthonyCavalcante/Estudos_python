#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 16:48:51 2021
@author ccavalcante
"""

from enum import Enum

class QuestionTypeEnum(str, Enum)

class Question:

    __text = None
    __type = None 
    __answer = None
