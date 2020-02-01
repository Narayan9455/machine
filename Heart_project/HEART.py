
# coding: utf-8

# In[12]:


import sys 
from sklearn.ensemble import RandomForestRegressor 
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
x_arg=sys.argv[1::]
dic={}

# In[8]:


df=pd.read_csv(r"/home/amit/Desktop/heart.csv")
df.dropna(axis=0,how="all")
df.dropna(axis=0,how="any")
independent_variables=list(df.columns.values)
independent_variables.remove("target")
x= df[independent_variables]
y=df["target"]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.80,random_state=33)
ex= RandomForestRegressor ()

lm = ex.fit(x_train, y_train)
#print(lm)
#y_train_pred = lm.predict(x_train)
y_test_pred = (lm.predict(x_test))
y_test_pred[y_test_pred>0.5]=1
y_test_pred[y_test_pred<=.5]=0
print(len(independent_variables))

i=0
print(x_arg)
for index in independent_variables:
    dic[index]=x_arg[i]
    i+=1
print(dic)
for index in independent_variables:
    print(x_arg[0],x_arg[1],x_arg[2])
    i+=1
print(dic)

# In[13]:
'''
#df=pd.DataFrame(dic,index=[0])
#y_test_pred =lm.predict(df)
#print(np.round(y_test_pred[0]))'''

