import pandas as pd

# Example dataframe with daily measurements
data = {'date': pd.date_range(start='2012-01-01', periods=730, freq='D'),
        'measurement': [i if i % 2 == 0 else float('nan') for i in range(730)]}

df = pd.DataFrame(data)

# Extract year and month/day for later use
df['year'] = df['date'].dt.year

# Step 1: Split the data into 2012 and 2013
df_2012 = df[df['year'] == 2012]
df_2013 = df[df['year'] == 2013]

# Step 2: Merge 2013 data with 2012 data on the date
df_merged = pd.merge(df_2013, df_2012[['date', 'measurement']], on='date', suffixes=('_2013', '_2012'))

# Step 3: Replace NaN values in 2013 with corresponding 2012 values
df_merged['measurement_2013'] = df_merged['measurement_2013'].fillna(df_merged['measurement_2012'])

print(df_merged)
# Step 4: Replace the 2013 data in the original dataframe with updated 2013 data
df_updated = pd.concat([df[df['year'] != 2013], df_merged[['date', 'measurement_2013']].rename(columns={'measurement_2013': 'measurement'})], ignore_index=True)

#print(df_updated)
'''# Step 5: Sort the dataframe by date
df_updated = df_updated.sort_values('date').reset_index(drop=True)

# Print the final dataframe
print(df_updated)'''