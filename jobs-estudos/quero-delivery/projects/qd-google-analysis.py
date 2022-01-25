import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Data load
qd_df = pd.read_csv('../datas/perfomance-download-analysis301121.csv')

#Data manipulation
    #changing columns type
qd_df['CPC médio']= qd_df['CPC médio'].str.replace(',', '.').astype(float)
qd_df['Taxa de conv.']= qd_df['Taxa de conv.'].str.replace(',', '.').astype(float)
qd_df['Custo / conv.']= qd_df['Custo / conv.'].str.replace(',', '.').astype(float)
qd_df['Custo']= qd_df['Custo'].str.replace(',', '.').astype(float)
qd_df['CTR']= qd_df['CTR'].str.replace(',', '.').astype(float)
  
   #creater, edit and remove columns 
mask_date= [['Domingo', 'Segunda-feira','Terça-feira', 'Quarta-feira'
            'Quinta-feira', 'Sábado']]
qd_df.insert(2,'Dia da semana', pd.to_datetime(qd_df['Dia']).dt.strftime('%A'))
qd_df['Dia da semana'] = qd_df['Dia da semana'].map({'Friday': 'Sexta-feira', 'Monday':'Segunda-feira',
                                                    'Saturday': 'Sábado', 'Sunday': 'Domingo',
                                                    'Thursday': 'Quinta-feira', 'Tuesday':'Terça-feira',
                                                    'Wednesday': 'Quarta-feira'    })

qd_df.rename(columns = {'Cidade (local geográfico)':'Cidade',
                        'Conversões': 'Downloads','Custo / conv.': 'Cust/down.'}, 
                                    inplace = True)
qd_df.drop(['Tipo de campanha', 'Código da moeda'], axis=1, inplace = True)


#Data analyses
print(qd_df.info())

x= qd_df[(qd_df['Campanha'] == '[download]Manutencao_Novembro')]

print(qd_df.groupby('Campanha').sum().sort_values(by = 'Downloads', ascending= False)['Downloads'].iloc[0])






