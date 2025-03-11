import pandas as pd
import os

# Directory where CSV files are stored
folder_path = 'C:\Code\miniproject_2\WeatherMachine\Radiation Sodankylä Tähtelä'

'''# Create a new folder for combined files
combined_folder = os.path.join(folder_path, "combined")
os.makedirs(combined_folder, exist_ok=True)'''

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    
# List to hold dataframes 
dfs = []

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all DataFrames
combined_df = pd.concat(dfs, ignore_index=True)

# Create 'Date' column
combined_df['Date'] = pd.to_datetime(combined_df[['Year', 'Month', 'Day']])
        
# Drop unwanted columns
combined_df = combined_df.drop(columns=['Year', 'Month', 'Day', 'Time [Local time]'])

# Sort by the 'Date' column
combined_df = combined_df.sort_values(by='Date')

# Step 4: Save the combined DataFrame to a new CSV file
combined_df.to_csv('Direct_solar_radiation.csv', index=False)