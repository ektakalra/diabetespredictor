import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


df=pd.read_csv('F:\codes\diabetes predictor\diabetes.csv')
# print(df.isnull().sum())
X=df.drop(['Outcome'],axis=1)
y=df['Outcome']

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3)
model_logR=LogisticRegression()
model_logR.fit(X_train,y_train)
print(model_logR.score(X_test,y_test))

model_svm=svm.SVC(kernel='linear')
model_svm.fit(X_train,y_train)
print(model_svm.score(X_test,y_test))

model_rfc=RandomForestClassifier(n_estimators=5)
model_rfc.fit(X_train,y_train)
print(model_rfc.score(X_test,y_test))
