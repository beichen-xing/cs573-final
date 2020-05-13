import pandas as pd

data = pd.read_csv('twoMonthsData.csv', usecols=['Month', 'Mdate','Sensor_ID', 'Hourly_Counts'], index_col=False)
group = data.groupby(['Month', 'Mdate','Sensor_ID']).sum()
print(group)
group.to_csv('groupData.csv')