# Create 'Date' column
import pandas as pd

#read the file
df = pd.read_csv('WeatherMachine/Data for Sodankylä Tähtelä (pyhäntunturi)/Pyhätunturi_ 2000-2025_snow_temp_perci.csv')

#change to date
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# Drop unwanted columns
df = df.drop(columns=['Year', 'Month', 'Day', 'Time [Local time]'])

#add to a new csv-file
df.to_csv('Pyhäntunturi_snow_temp_preci.csv')