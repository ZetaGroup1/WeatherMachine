import pandas as pd
import os

# Get list of files in the current folder that start with 'Vuokatti_'
folder_path = "C:\\Repos\\Project2\\WeatherMachine\\Data cleaning\\Snow_temp_precip"  # Change this if the files are in a different folder
files = [f for f in os.listdir(folder_path) if f.startswith("Vuokatti_") and f.endswith(".csv")]

if len(files) < 2:
    raise ValueError("At least two files starting with 'Vuokatti_' are needed.")

# Read the two files
df1 = pd.read_csv(os.path.join(folder_path, files[0]))
df2 = pd.read_csv(os.path.join(folder_path, files[1]))

# Function to create 'Date' column
def add_date_column(df):
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    return df.drop(columns=['Year', 'Month', 'Day', 'Time [Local time]'], errors='ignore')

# Add 'Date' column and drop unnecessary columns
df1 = add_date_column(df1)
df2 = add_date_column(df2)

# Ensure "Average temperature [°C]" exists in one of the files
if "Average temperature [°C]" in df1.columns:
    temp_df = df1[['Date', 'Average temperature [°C]']]
    main_df = df2
elif "Average temperature [°C]" in df2.columns:
    temp_df = df2[['Date', 'Average temperature [°C]']]
    main_df = df1
else:
    raise ValueError("No file contains 'Average temperature [°C]' column.")

# Merge temperature data based on 'Date'
merged_df = main_df.merge(temp_df, on="Date", how="left")

# Convert 'Snow depth [cm]' to numeric, replacing '-' with NaN
merged_df['Snow depth [cm]'] = pd.to_numeric(merged_df['Snow depth [cm]'], errors='coerce')

# Fill NaN values with a 7-day rolling mean
merged_df['Snow depth [cm]'] = merged_df['Snow depth [cm]'].fillna(merged_df['Snow depth [cm]'].rolling(7, min_periods=1).mean())

# Save the merged DataFrame to a new file
output_file = os.path.join(folder_path, "Vuokatti_snow_temp_preci.csv")
merged_df.to_csv(output_file, index=False)

print(f"Merged file saved as {output_file}")
