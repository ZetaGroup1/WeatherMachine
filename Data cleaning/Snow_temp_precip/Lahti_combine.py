import pandas as pd
import os

# Directory where CSV files are stored
folder_path = "C:\\Repos\\Project2\\WeatherMachine\\Data cleaning\\Snow_temp_precip"

files = [f for f in os.listdir(folder_path) if f.startswith("Lahti_") and f.endswith(".csv")]

# List to hold dataframes
dfs = []

# Loop over all CSV files and read them into a list
for file in files:
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

# Sort by the 'Date' column
combined_df = combined_df.sort_values(by='Date')

# Save the combined DataFrame to a new CSV file
output_file_path = os.path.join(folder_path, 'Lahti_snow_temp_preci.csv')
combined_df.to_csv(output_file_path, index=False)

print("CSV files combined successfully!")
