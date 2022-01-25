import numpy as np 
import pandas as pd 

qd_age_df = pd.read_csv('quero-delivery/datas/Data-analysis-traffics-age291221.csv', 
encoding='unicode_escape')

#data manipulation
qd_age_df.drop(['Nível de veiculação', 'Tipo de resultado',
               'Término dos relatórios', 'Início dos relatórios', 
               'Nome da campanha.1','Status de veiculação' ], 
               inplace= True, axis= 1)

qd_age_df.insert(3, 'Weekday',pd.to_datetime(qd_age_df['Dia']).dt.strftime('%A'))

qd_age_df['Dia'] = qd_age_df['Dia'].str.replace('-', '')
qd_age_df['Dia'] = pd.to_datetime(qd_age_df['Dia']).dt.strftime('%d/%m/%y')

qd_age_df['Weekday'] = qd_age_df['Weekday'].map({'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'})

print(qd_age_df.info())

def nan_for_mean(col):
     data = qd_age_df[~qd_age_df[col].isna()][col]
     
     return qd_age_df[col].fillna(data.mean(), inplace= True)
     


print(qd_age_df[['Cliques (todos)','Custo por resultado',
               'Custo por ativação de aplicativo', 'Custo por ativação do aplicativo única']].head())     
for colunas in qd_age_df:
     if qd_age_df[colunas].dtypes != object:
          nan_for_mean(colunas)


print(qd_age_df[['Cliques (todos)','Custo por resultado',
               'Custo por ativação de aplicativo', 'Custo por ativação do aplicativo única']].head())      