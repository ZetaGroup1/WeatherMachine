import os
import pandas as pd

# Read the file
file_path = 'C:\\Repos\\Project2\\WeatherMachine\\Data cleaning\\Snow_temp_precip\\Tahko_daily.csv'
df = pd.read_csv(file_path)

# Create 'Date' column
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# Drop unwanted columns
df = df.drop(columns=['Year', 'Month', 'Day', 'Time [Local time]'])

# Convert 'Snow depth [cm]' to numeric, replacing '-' with NaN
df['Snow depth [cm]'] = pd.to_numeric(df['Snow depth [cm]'], errors='coerce')

# Fill NaN values with a 7-day rolling mean
df['Snow depth [cm]'] = df['Snow depth [cm]'].fillna(df['Snow depth [cm]'].rolling(7, min_periods=1).mean())

# Get the directory of the original file
directory = os.path.dirname(file_path)

# Create the output file path by combining the directory with the new file name
output_file = os.path.join(directory, 'Tahko_snow_temp_preci.csv')

# Save to the same directory
df.to_csv(output_file, index=False)