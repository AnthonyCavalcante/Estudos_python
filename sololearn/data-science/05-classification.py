import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import confusion_matrix, plot_confusion_matrix

iris_df = pd.read_csv('datas/iris.csv')
iris_df.drop('id',axis = 1, inplace = True)

x=iris_df[['petal_len', 'petal_wd']]
y = iris_df['species']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state = 1, stratify = y)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)

pred = knn.predict(x_test)

#probabilidade 

pred_prob = knn.predict_proba(x_test)
#print(pred_prob[10:12])
#print(pred[10:12])

#accuracy with confusion_matrix

acc = confusion_matrix(y_test, pred)
#print(acc)
#plot_confusion_matrix(knn,x_test, y_test)
#plt.show()

#k-fold
knn_cv = KNeighborsClassifier(n_neighbors=3)
cv_score = cross_val_score(knn_cv, x, y, cv=5)
#print(cv_score, cv_score.mean())

#grid-search for best knn

knn2 = KNeighborsClassifier()
param_grid = {'n_neighbors': np.arange(2,10)}
knn_gscv = GridSearchCV(knn2,param_grid, cv = 5)
knn_gscv.fit(x, y)
'''
print(knn_gscv.best_params_)
print(knn_gscv.best_score_)
'''

#label prediction
new_data = np.array( np.array([[3.76, 1.2], [5.25, 1.2], [1.58, 1.2]]))


knn_final = KNeighborsClassifier(n_neighbors=knn_gscv.best_params_['n_neighbors'])
knn_final.fit(x, y)
print(knn_final.predict(new_data))