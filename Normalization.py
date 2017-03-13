import pandas
from pandas import Series
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from math import sqrt



# #cols = ['name', 'emotion']
# no_headers = pd.read_csv('/home/julie/PycharmProjects/EmotionRecog/englishcsv.csv', sep=',', names=cols, low_memory=False)
# no_headers.head()
# print(no_headers)

# load the dataset

ser = pandas.read_csv('/home/julie/PycharmProjects/EmotionRecog/englishcsv.csv')
stand = ser.std()
me = ser.mean()

print(stand)
print(me)

# series = Series.from_csv('/home/julie/PycharmProjects/EmotionRecog/englishcsv.csv', header=0)
# #series = pd.read_csv('/home/julie/PycharmProjects/EmotionRecog/englishcsv.csv', sep=',', low_memory=False)
# print(series.head())
# #prepare data for standardization
# values = series.values
# values = values.reshape((len(values), 1))
# #train the standardization
# scaler = StandardScaler()
# scaler = scaler.fit(values)
# print('Mean: %f, StandardDeviation: %f' % (scaler.mean_, sqrt(scaler.var_)))
# normalized = scaler.transform(values)
# for i in range(960):
# 	print(normalized[i])
