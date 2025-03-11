import pandas as pd

df_Levi_01 = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Others\Levi_01.csv')
df_Levi_02 = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Others\Levi_02.csv')
df_Levi_03 = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Others\Levi_03.csv')
df_Levi_04 = pd.read_csv('Levi - Ylläs - Ruka - Himos\Levi_Others\Levi_04.csv')


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

combined_df.to_csv('Levi - Ylläs - Ruka - Himos\Levi_Combined\levi_intermediate.csv', index=False)