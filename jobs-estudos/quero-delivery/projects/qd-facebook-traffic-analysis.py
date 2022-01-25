import datetime
from matplotlib import colors
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec 
#pd.set_options('display.max_rows', 101)
print_line = '===='*5
#Load data:
qd_df = pd.read_csv('../datas/Data-analysis-traffics-facebook281221.csv', encoding= 'unicode_escape')

#Table manipulation:   
qd_df.drop(['Nível de veiculação', 'Tipo de resultado',
               'Término dos relatórios', 'Início dos relatórios'],
          axis=1, inplace=True)
qd_df.insert(4,'Weekday', pd.to_datetime(qd_df['Dia']).dt.strftime('%A'))



qd_df['Dia'] = qd_df['Dia'].str.replace('-','')
qd_df['Dia'] = pd.to_datetime(qd_df['Dia']).dt.strftime('%d/%m/%y')


best_date = qd_df.groupby('Dia').sum()
best_date_result = best_date[(best_date['Resultados'] == best_date['Resultados'].max())]


print(qd_df.info())


#Table Analyses:
qd_region = qd_df.groupby('Região')
qd_adgroup = qd_df.groupby('Nome do conjunto de anúncios')
qd_weekday = qd_df.groupby('Weekday')
qd_day = qd_df.groupby('Dia')


print(qd_weekday["Resultados"].sum())
     #Statistics metrics 'custo por resultado'
qdcost_mean = qd_df['Custo por resultado'].mean()
qdcost_std =  qd_df['Custo por resultado'].std()
qdcost_max = qd_df['Custo por resultado'].max()
inter_region_std = qd_df[(qd_df['Custo por resultado'] > (qdcost_mean - qdcost_std))
                         & (qd_df['Custo por resultado'] < (qdcost_std + qdcost_mean))     
                              
                         ][['Região','Custo por resultado']]

#print('Custo por resultado por região\n'+'--'*5)
#print(qd_region['Custo por resultado'].mean().round(2).sort_values(ascending=False))

     #Statistics metrics 'Resultado' 

qdresult_region = qd_region['Resultados'].sum()
qdresult_weekday = qd_weekday['Resultados'].sum()
qdresult_bestday = qd_day['Resultados'].sum()

     #Statistics metrics 'Ativações' 
qd_atvcost_region = qd_region['Custo por ativação do aplicativo única'].mean().round(2)
qd_atvcost_weekday = qd_weekday['Custo por ativação do aplicativo única'].mean().round(2)
qd_atvcost_day = qd_day['Custo por ativação do aplicativo única'].mean().round(2)

qdatv_region = qd_region['Ativações do aplicativo únicas'].sum()
qdatv_weekday = qd_weekday['Ativações do aplicativo únicas'].sum()
qdatv_day = qd_day['Ativações do aplicativo únicas'].sum()
#print(qd_df['Região'].unique())
#Data Visualization:
'''plt.style.use(['bmh'])
fig = plt.figure(figsize=(10,12))
gs = gridspec.GridSpec(3,2)

plt.ion()
while True:
     region = input('selecione a região\n')
     

     set_graph = qd_df[(qd_df['Região'] == region)] 
     plt.cla()
     plt.clf()
     ax1 = fig.add_subplot(221)
     ax1_graph = set_graph.groupby('Weekday') ['Resultados'].sum().plot(kind='barh', 
               width = 0.8, color = 'springgreen')
     for i in ax1_graph.patches:
          plt.annotate(i.get_width(),
                    ( i.get_width()+0.5, i.get_y()+i.get_height() /2),
                    fontsize = 8
                         )

     ax2 = fig.add_subplot(222)
     ax2_graph= set_graph.groupby('Weekday') ['Custo por resultado'].mean().plot(kind = 'bar', 
               width = 0.8, color = 'orangered')
     for i in ax2_graph.patches:
          plt.annotate(i.get_height().round(2),
                    (i.get_x() + i.get_width()/ 2, i.get_height()),
                    ha='center', va = 'baseline',
                    fontsize = 8, xytext = (0,1), textcoords = 'offset points' )


     ax3 = fig.add_subplot(gs[-1,:])
     xs = set_graph.groupby('Weekday') ['Frequência'].mean().plot( marker='o', ms=8,  mec='b',color = 'red')
     #xs.annotate('testando', (1, 1.17),(1,1.18) )
     
     plt.pause(2)
     resp = input('fechar plot?\n')
     
     if resp == 'sim':
          plt.ioff()
          break'''
print(qd_df['Nome do conjunto de anúncios'])

