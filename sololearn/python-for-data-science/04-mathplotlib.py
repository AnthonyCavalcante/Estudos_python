import pandas as pd
import matplotlib.pyplot as plt

def exercise1():
    s = pd.Series([18, 42, 9, 32, 81, 64,60, 3])
    s.plot(kind = 'bar')
    plt.savefig('matplotlib-imgs/plot.png')

def exercise2():
    df = pd.read_csv('datas/ca-covid.csv')
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    df.drop('state', axis = 1, inplace = True)
    df.set_index('date', inplace = True)

    df[(df['month'] == 'February')] ['cases'].plot()
    plt.savefig('matplotlib-imgs/chart.png')
    
    df[(df['month'] == 'February')] [['cases', 'deaths']].plot()
    plt.savefig('matplotlib-imgs/cases_deaths.png') 
def exercise3():
    df = pd.read_csv('datas/ca-covid.csv')
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    df['weekday'] = pd.to_datetime(df['date']).dt.strftime('%A')
    df.drop('state', axis = 1, inplace=True)
    df.set_index('date', inplace = True)
    set_month = df[(df['month'] == 'February')]
    (set_month.groupby('weekday') [['cases', 'deaths']].sum()).plot(kind = 'barh')
     
    plt.savefig('matplotlib-imgs/bar-weekday.png')


def exercise4():
    df= pd.read_csv('datas/ca-covid.csv')
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    df.drop('state', axis = 1, inplace = True)
    df.set_index('date', inplace = True)

    (df.groupby('month')['deaths'].sum()).plot(kind='pie')
    plt.savefig('matplotlib-imgs/pie-deaths')

def exercise5():
    df= pd.read_csv('datas/ca-covid.csv')
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    df['weekday'] = pd.to_datetime(df['date']).dt.strftime('%A')
    df.drop('state', axis = 1, inplace = True)
    df.set_index('date', inplace = True)
    set_month = df[(df['month'] == 'June')]
    (set_month.groupby('weekday') [['cases', 'deaths']].sum()).plot()
    
    plt.xlabel('week in june')
    plt.ylabel('numbers')
    plt.suptitle('COVID in June/2020')
    plt.show()

    #plt.savefig('matplotlib-imgs/fomart.png')
def main():
    exercise5()

if __name__ == '__main__':
    main()
    