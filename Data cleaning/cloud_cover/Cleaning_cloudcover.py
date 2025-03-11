import pandas as pd
import os

# Directory where CSV files are stored
folder_path = 'C:\\Repos\\Project2\\WeatherMachine\\Data cleaning\\cloud_cover'

# Create a new folder for combined files
combined_folder = os.path.join(folder_path, "combined")
os.makedirs(combined_folder, exist_ok=True)

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Identify unique venue names dynamically by extracting the part before the first underscore
venue_names = set([file.split('_')[0] for file in csv_files])

# Dictionary to store DataFrames for each venue
combined_dfs = {}

for venue in venue_names:
    # Filter files that start with the current venue name
    matching_files = [file for file in csv_files if file.startswith(venue + "_")]
    
    # List to hold dataframes for this venue
    dfs = []
    
    for file in matching_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        dfs.append(df)
    
    # Combine all DataFrames for this venue if any files exist
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        
        # Create 'Date' column
        combined_df['Date'] = pd.to_datetime(combined_df[['Year', 'Month', 'Day']])
        
        # Drop unwanted columns
        combined_df = combined_df.drop(columns=['Year', 'Month', 'Day', 'Time [Local time]'])
        
        # Cloud cover mapping
        cloud_cover = {
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
            '-': 9
        }
        combined_df['cloud_cover_code'] = combined_df['Cloud cover [1/8]'].map(cloud_cover)
        
        # Sort by the 'Date' column
        combined_df = combined_df.sort_values(by='Date')
        
        # Save to CSV in the combined folder
        output_file = os.path.join(combined_folder, f'{venue}_combined.csv')
        combined_df.to_csv(output_file, index=False)
        
        print(f"CSV files for {venue} combined successfully and saved in 'combined' folder!")

