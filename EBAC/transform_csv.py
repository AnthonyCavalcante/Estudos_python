#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Dec 22 17:55:37 2021
@author ccavalcante
"""

CSV_PATH = './carros.csv'
DELIMITER = ','

def is_number(value: str) -> bool:

    try:
        
        int(value)

        return True

    except ValueError:

        return False

def convert_value(value: str):

    if is_number(value):
        return int(value)

    return value


def check_and_convert(value: str):
    try:
        
        return int(value)

    except ValueError:

        return value


result = []

with open(CSV_PATH, 'r') as csv_file:
    
    header = csv_file.readline()

    line = csv_file.readline()

    while line:

        #converted_line = [ check_and_convert(value) for value in line.split(DELIMITER) ]
        converted_line = map(check_and_convert, line.split(DELIMITER)) 

        result.append(converted_line)

        line = csv_file.readline()
    
    print('-'*10)
    print(header)
    print('-'*10)

    for row in result:
        print(list(row))
