import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
os.chdir('C:\\Users\\Sarthak\\Desktop\\ML Project\\boston-housing\\')
boston=pd.read_csv('train.csv')
boston.head()
print(boston)
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(boston['MEDV'], bins=30)
plt.show()
