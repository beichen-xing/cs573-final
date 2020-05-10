import pandas as pd

data = pd.read_csv('Pedestrian_Counting_System___2009_to_Present__counts_per_hour_.csv', usecols=['Sensor_ID', 'Hourly_Counts', 'Year', 'Month', 'Mdate'], index_col=False)
select = data.loc[(data['Year'] == 2020) & ((data['Month'] == 'March') | (data['Month'] == 'April'))]
print(select)
select.to_csv('twoMonthsData.csv', index=False)