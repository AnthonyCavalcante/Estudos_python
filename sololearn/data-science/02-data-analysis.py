import pandas as pd 
import numpy as np

pres_df = pd.read_csv('datas/president_heights_party.csv')
pres_df.set_index('name', inplace = True)

def exercise1():
    age_heights_df = pres_df[['age', 'height']]
    print(age_heights_df)
    print(age_heights_df.shape)

def reshape():

    r = int(input()) 
    inp = input()
    lst = [float(x) for x in inp.split()]
    arr = np.array(lst)
    n = int(len(lst)/r)

    print (arr.reshape(r,n))
def main():
   exercise1()
   
    
if __name__ == '__main__':
    main()
    