import pandas as pd
import os

# Directory where your CSV files are stored
folder_path = 'C:\\Repos\\Project2\\WeatherMachine\\Data cleaning\\cloud_cover'

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
    
    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Optionally, sort by the relevant columns (e.g., Year, Month, Day, and Time)
combined_df['Date'] = pd.to_datetime(combined_df[['Year', 'Month', 'Day']])

# Drop the 'Year', 'Month', 'Day', and 'Time [Local time]' columns
combined_df = combined_df.drop(columns=['Year', 'Month', 'Day', 'Time [Local time]'])

cloud_cover=  {
    'Clear (0/8)': 0,
    'Clear (1/8)': 1,
    'Mostly clear (2/8)': 2,
    'Mostly clear (3/8)': 3,
    'Partly cloudy (4/8)': 4,
    'Partly cloudy (5/8)': 5,
    'Mostly cloudy (6/8)': 6,
    'Mostly cloudy (7/8)': 7,
    'Cloudy (8/8)': 8,
    'Cloudiness cannot be determined (9/8)': 9,
    '-': 9}
combined_df['cloud_cover_code']= combined_df['Cloud cover [1/8]'].map(cloud_cover)

# Sort by the 'Date' column
combined_df = combined_df.sort_values(by='Date')

# Save the combined DataFrame to a new CSV file
output_file_path = os.path.join(folder_path, 'combined_cloud_data.csv')
combined_df.to_csv(output_file_path, index=False)

print("CSV files combined successfully with specified columns removed and missing values handled!")
