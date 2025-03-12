import pandas as pd

df_Himos_01 = pd.read_csv('Levi - Ylläs - Ruka - Himos/Himos_Others/Himos_01.csv')
df_Himos_02 = pd.read_csv('Levi - Ylläs - Ruka - Himos/Himos_Others/Himos_02.csv')

df_Himos_01['Date'] = pd.to_datetime(df_Himos_01[['Year', 'Month', 'Day']])
df_Himos_01 = df_Himos_01[['Date', 'Precipitation amount [mm]', 'Snow depth [cm]', 'Average temperature [°C]']]

df_Himos_02['Date'] = pd.to_datetime(df_Himos_02[['Year', 'Month', 'Day']])
df_Himos_02 = df_Himos_02[['Date', 'Precipitation amount [mm]', 'Snow depth [cm]', 'Average temperature [°C]']]

combined_df = pd.concat([df_Himos_01, df_Himos_02])

df_Himos_CC = pd.read_csv('Levi - Ylläs - Ruka - Himos/Himos_Cloud_Coverage/combined/Himos_combined.csv')

df_Himos_CC = df_Himos_CC[['Date', 'cloud_cover_code']]

df_Himos_CC['Date'] = pd.to_datetime(df_Himos_CC['Date'])

final_df = pd.merge(combined_df, df_Himos_CC, on='Date')

final_df.to_csv('Levi - Ylläs - Ruka - Himos/Himos_Combined/himos_intermediate.csv', index=False)