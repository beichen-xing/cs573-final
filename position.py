import csv
import pandas as pd

data = pd.read_csv('Pedestrian_Counting_System_-_Sensor_Locations.csv', usecols=['sensor_id', 'latitude', 'longitude'], index_col=False)
print(data)
data.to_csv('location.csv', index=False)