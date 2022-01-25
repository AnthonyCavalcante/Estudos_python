import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=LAPTOP-M55B3J1F;"
    "Database=Qd_data_analysis;"
    "UID=sa;"
    "PWD=16maju11;"

)

conexao = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-M55B3J1F;Database=Qd_data_analysis; UID=sa;PWD=16maju11;")
print('deu certo')