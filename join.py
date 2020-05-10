import pandas as pd

location = pd.read_csv('location.csv', usecols=['sensor_id', 'latitude','longitude'], index_col=False)
count = pd.read_csv('groupData.csv', usecols=['Sensor_ID', 'Hourly_Counts','Month','Mdate'], index_col=False)

out = location.set_index('sensor_id').join(count.set_index('Sensor_ID'))
out.to_csv('joinData.csv', index=True)