import pandas as pd
import sqlite3

file_path = "data/raw/T_ONTIME_REPORTING.csv"
df = pd.read_csv(file_path)

df['FL_DATE'] = pd.to_datetime(df['FL_DATE'], errors='coerce') #Convert flight date to datetime
df = df.dropna(subset=['DEP_DELAY', 'ARR_DELAY'], how = 'all')  #Drop rows that have both missing departure delay and arrival delay

df.columns = df.columns.str.lower()

delay_cols = ['carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']
df[delay_cols] = df[delay_cols].fillna(0)

df[['dep_delay', 'arr_delay']] = df[['dep_delay', 'arr_delay']].fillna(0).round(decimals=1) #Filling in empty delays with 0 and rounding to 1 decimal point

numeric_cols = ['distance', 'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']
df[numeric_cols] = df[numeric_cols].round(0)

print(df.head())
print(df.info())
