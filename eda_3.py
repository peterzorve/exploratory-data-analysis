

import streamlit as st
import seaborn as sb
import pandas as pd 


data = pd.read_csv('train.csv')
data

data['y'].unique()  

min(data['congestion'])


import matplotlib.pyplot as plt 

# plt.hist(data.congestion, bin=10) 


data = pd.read_csv('train.csv')



sb.heatmap(data.corr(), cmap='YlGnBu', annot=True)



congestion = data['congestion']


data.head(4)

congestion = data['congestion']
x = data['x']
y = data['y']


plt.scatter(x, congestion)

plt.scatter(y, congestion)


plt.scatter(x, y)
data.head(5)


data['month'] = data['time'].apply(lambda row: row.split('-')[1])
data['new_time'] = data['time'].apply(lambda row: row.split('-')[2][2:])
data['day'] = data['time'].apply(lambda row: row.split('-')[2][:2])

data_ED = data[data.direction == 'EB']

print(len(data_ED))
data_ED




days = ['01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
# plt.bar(data['x'], data['congestion']) 

days_of_month = []
mean_for_the_day = []

for day2 in days:
     april  = april.groupby(day) == day2
     mean2  = april['congestion'].mean()

     # mean2 = mean2.astype(int)




     days_of_month.append(day2)
     mean_for_the_day.append(mean2)

print(days_of_month)
print(mean_for_the_day)

# print(type(april['congestion']))

# plt.plot(days_of_month, mean_for_the_day)


# april_1st_direction = april_1st[april_1st.direction == 'EB']
# april_1st_direction_x0 = april_1st_direction[april_1st_direction.x == 0]
# len(april_1st_direction_x0)


# april_1st_direction_x0.congestion[:50].plot()














