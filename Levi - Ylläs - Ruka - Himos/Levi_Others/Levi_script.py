import pandas as pd


df_Levi_03 = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Others\Levi_03.csv')
df_Levi_04 = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Others\Levi_04.csv')
df_Levi_01 = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Others\Levi_01.csv')
df_Levi_02 = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Others\Levi_02.csv')


df_Levi_03['Date'] = pd.to_datetime(df_Levi_03[['Year', 'Month', 'Day']])
df_Levi_03 = df_Levi_03[['Date', 'Average temperature [°C]']]


df_Levi_04['Date'] = pd.to_datetime(df_Levi_04[['Year', 'Month', 'Day']])
df_Levi_04 = df_Levi_04[['Date', 'Snow depth [cm]', 'Precipitation amount [mm]']]


df_Levi_01['Date'] = pd.to_datetime(df_Levi_01[['Year', 'Month', 'Day']])
df_Levi_01 = df_Levi_01[['Date', 'Average temperature [°C]', 'Snow depth [cm]', 'Precipitation amount [mm]']]


df_Levi_02['Date'] = pd.to_datetime(df_Levi_02[['Year', 'Month', 'Day']])
df_Levi_02 = df_Levi_02[['Date', 'Average temperature [°C]', 'Snow depth [cm]', 'Precipitation amount [mm]']]


combined_df = pd.merge(df_Levi_03, df_Levi_04, on='Date', how='outer')
combined_df = pd.merge(combined_df, df_Levi_01, on='Date', how='outer')
combined_df = pd.merge(combined_df, df_Levi_02, on='Date', how='outer')

combined_df['Average temperature [°C]'] = combined_df['Average temperature [°C]_x'].fillna(combined_df['Average temperature [°C]_y']).fillna(combined_df['Average temperature [°C]'])
combined_df = combined_df.drop(columns=['Average temperature [°C]_x', 'Average temperature [°C]_y'])

combined_df['Snow depth [cm]'] = combined_df['Snow depth [cm]_x'].fillna(combined_df['Snow depth [cm]_y']).fillna(combined_df['Snow depth [cm]'])
combined_df = combined_df.drop(columns=['Snow depth [cm]_x', 'Snow depth [cm]_y'])

combined_df['Precipitation amount [mm]'] = combined_df['Precipitation amount [mm]_x'].fillna(combined_df['Precipitation amount [mm]_y']).fillna(combined_df['Precipitation amount [mm]'])
combined_df = combined_df.drop(columns=['Precipitation amount [mm]_x', 'Precipitation amount [mm]_y'])

combined_df.to_csv('Levi - Ylläs - Ruka - Himos\Levi_Combined\levi_intermediate.csv', index=False)

df_Levi_cc = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\combined\Levi_combined.csv')



combined_df = pd.merge(combined_df, df_Levi_02, on='Date', how='outer')