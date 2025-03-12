import os
import pandas as pd
import numpy as np
import re

def extract_venue_name(filename):
    """Extracts venue name dynamically from filename before first underscore."""
    return re.split(r'_', filename, maxsplit=1)[0]

def process_files(folder_path):
    """Merges files, processes data, and saves final results in 'Final' folder."""
    final_folder = os.path.join(folder_path, 'Final')
    os.makedirs(final_folder, exist_ok=True)
    
    # Load direct solar radiation file
    solar_file = os.path.join(folder_path, 'Direct_solar_radiation.csv')
    df_solar = pd.read_csv(solar_file, usecols=['Date', 'Direct solar radiation mean [W/m2]'])
    df_solar['Date'] = pd.to_datetime(df_solar['Date'], errors='coerce')
    
    # Dictionary to store dataframes for each venue
    venue_dfs = {}
    required_columns = ['Precipitation amount [mm]', 'Snow depth [cm]', 'Average temperature [°C]', 'cloud_cover_code']
    
    # Process each file in the folder
    for file in os.listdir(folder_path):
        if file.endswith('.csv') and file != 'Direct_solar_radiation.csv':
            venue_name = extract_venue_name(file)
            file_path = os.path.join(folder_path, file)
            
            df = pd.read_csv(file_path)
            
            # Ensure Date column is converted properly
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

            # Filter rows between 2005-01-01 and 2024-12-31
            df = df[(df['Date'] >= '2005-01-01') & (df['Date'] <= '2024-12-31')]
            
            # Convert all other columns to numeric
            for col in df.columns:
                if col not in {'Date'}:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # Keep only necessary columns that exist in the file
            available_columns = ['Date'] + [col for col in required_columns if col in df.columns]
            df = df[available_columns]
            
            # Merge venue data
            if venue_name in venue_dfs:
                venue_dfs[venue_name] = venue_dfs[venue_name].merge(df, on='Date', how='outer')
            else:
                venue_dfs[venue_name] = df
    
    # Process and save final files
    for i, (venue, df) in enumerate(venue_dfs.items()):
        
        # Ensure Date is properly formatted before merging
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df_solar['Date'] = pd.to_datetime(df_solar['Date'], errors='coerce')
        
        # Merge with solar radiation data
        df = df.merge(df_solar, on='Date', how='outer')
        
        # Ensure all required columns exist (fill missing ones with NaN)
        for col in required_columns:
            if col not in df:
                df[col] = np.nan
        
        # Count consecutive days with snow > 10 cm
        df['days_above_10cm'] = (df['Snow depth [cm]'] > 10).astype(int)
        df['days_above_10cm'] = df.groupby((df['Snow depth [cm]'] <= 10).cumsum())['days_above_10cm'].cumsum()
        
        # Count consecutive days with snow > 20 cm
        df['days_above_20cm'] = (df['Snow depth [cm]'] > 20).astype(int)
        df['days_above_20cm'] = df.groupby((df['Snow depth [cm]'] <= 20).cumsum())['days_above_20cm'].cumsum()
        
        # Save final file
        output_path = os.path.join(final_folder, f'{venue}_final.csv')
        df.to_csv(output_path, index=False)
        print(f'Saved: {output_path}')

if __name__ == "__main__":
    folder_path = 'C:\\Repos\\Project2\\WeatherMachine\\Data cleaning\\Final_merge'  # Change this to your actual folder path
    process_files(folder_path)
