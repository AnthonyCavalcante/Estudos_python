import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd

pres_df = pd.read_csv('datas/president_heights_party.csv')


def exercise1():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    fig = plt.figure()
    ax = plt.axes()
    ax.plot(x, y)
    ax.plot(x, np.cos(x))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('teste gráfico')
    plt.legend()
    plt.show()

def exercise2():
    '''pres_df.plot(kind = 'scatter',
        x = 'height',
        y = 'age',
        title = 'U.S Presidents'
    
    )'''
    age_pres = pres_df['age'].value_counts()
    plt.style.use('ggplot')
    age_pres.plot(kind = 'bar')
    plt.show()

def miss():
    lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]
    lst_df = pd.Series(lst)
    abdullah = lst_df.fillna(lst_df.mean()).round(1)
    print(abdullah)

def main():
    miss()
    

if __name__ == '__main__':
    main()
    