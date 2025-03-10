import pandas as pd
import os

# Directory where your CSV files are stored
folder_path = 'C:\\Repos\\Project2\\WeatherMachine\\Data cleaning'

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# List to hold dataframes
dfs = []

# Loop over all CSV files and read them into a list
for file in csv_files:
    # Full path to the CSV file
    file_path = os.path.join(folder_path, file)
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Optionally, you can add a 'location' column if it isn't already in the file
    df['Location'] = file.split('.')[0]  # Assuming the file name is the location
    
    # Append the DataFrame to the list
    dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Optionally, you can sort by a date column if your data has one
combined_df['Date'] = pd.to_datetime(combined_df['Date'])  # Adjust column name as necessary
combined_df = combined_df.sort_values(by='Date')

# Save the combined DataFrame to a new CSV
combined_df.to_csv('combined_weather_data.csv', index=False)

print("CSV files combined successfully!")
