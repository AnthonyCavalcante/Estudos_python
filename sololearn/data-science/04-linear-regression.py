import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#formula linear regression: Y = b(interceptação)+m(coeficiente) * X
def exercise1():
    boston_dataset = load_boston()
    boston = pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
    boston['MEDV'] = boston_dataset.target

    X = boston[['RM']]
    Y = boston['MEDV']
    model = LinearRegression()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,  test_size=0.3, random_state=1)
    model.fit (X_train, Y_train)

    new_rm = np.array([6.5]).reshape([-1,1])
    Y_test_predicated = model.predict(X_test)
    '''print(model.predict(new_rm))
    print(model.intercept_ + model.coef_*6.5)'''

    X2 = boston[['RM', 'LSTAT']]
    Y = boston['MEDV']
    model2 = LinearRegression()
    X2_train, X2_test, Y_train, Y_test = train_test_split(X2, Y, test_size = 0.3, random_state = 1)
    model2.fit(X2_train, Y_train)
    print(model2.intercept_)
    print(model2.coef_)
    
    y_test_predicated2 = model2.predict(X2_test)
    print(y_test_predicated2)

def main():
    exercise1()
    
if __name__ == '__main__':
    main()
    