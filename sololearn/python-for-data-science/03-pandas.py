import pandas as pd

def extra_intro1():
    data = {
   'ages': [14, 18, 24, 42],
   'heights': [165, 180, 176, 184]
            }  
    dt = pd.DataFrame(data, index=['lucas', 'carlos', 'maria', 'julia'])
    print(dt[["ages", "heights"]]) 

def extra_intro2():
    df = pd.read_csv("datas/ca-covid.csv")
    df['month'] = pd.to_datetime(df['date'], format = '%d.%m.%y').dt.month_name()
    df['percent_death'] = (df['deaths'] / df['cases'])*100
    df.drop('state', axis = 1, inplace = True)
    
    df.set_index('date', inplace = True)
    print(df['cases'].describe())

def exercise1():     
    data = {
    'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
    'number': ['1234', '5678', '2222', '1111', '0909']
    }
    dt = pd.DataFrame(data, index=data['name'])
    find_name = input()
    print(dt.loc[find_name])

def exercise2():
    
    data = {
    'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom', 'Harry'],
    'rank': [4, 1, 3, 5, 2, 6]
    }
    dt = pd.DataFrame(data)
    ranking = int(input())
    #result = dt.loc[ranking] 
    #print(dt[dt['rank']==ranking]['name'])
    print(dt[(dt["rank"]>ranking) & (dt['rank']< 5)] ['name'] )

def exercise3():
    df = pd.read_csv('datas/ca-covid.csv')
    df.drop('state', axis = 1 , inplace = True)
    df['weekday'] = pd.to_datetime(df['date']).dt.strftime('%A')
    df ['month'] = pd.to_datetime(df['date']).dt.month_name()
    
    print(df[(df['weekday'] == 'Friday')]  ['cases'].sum())

def exercise4():
    df = pd.read_csv('datas/ca-covid.csv')
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    df.drop ('state', axis =1, inplace = True)
    df.set_index('date', inplace = True)
    
    month_select = input()
    df_month = df[(df['month'] == month_select)]
    
    print(df_month[(df_month['cases'] == df_month['cases'].max())])


def covid_data():
    df = pd.read_csv('datas/ca-covid.csv')
    df['weekday'] = pd.to_datetime(df['date']).dt.strftime('%A')
    df['ratio'] = (df['deaths']/df['cases'])
    df.drop('state', axis = 1, inplace = True)
    df.set_index('date', inplace = True)

    print(df[(df['ratio'] == df['ratio'].max())])

def main():
    covid_data()

if __name__ == '__main__':
    main()
    