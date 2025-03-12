import pandas as pd

df_Ruka_01 = pd.read_csv('Levi - Ylläs - Ruka - Himos/Ruka_Others/Ruka_01.csv')

df_Ruka_01['Date'] = pd.to_datetime(df_Ruka_01[['Year', 'Month', 'Day']])
df_Ruka_01 = df_Ruka_01[['Date', 'Precipitation amount [mm]', 'Snow depth [cm]', 'Average temperature [°C]']]

df_Ruka_CC = pd.read_csv('Levi - Ylläs - Ruka - Himos/Ruka_Cloud_Coverage/combined/Ruka_combined.csv')

df_Ruka_CC = df_Ruka_CC[['Date', 'cloud_cover_code']]

df_Ruka_CC['Date'] = pd.to_datetime(df_Ruka_CC['Date'])

final_df = pd.merge(df_Ruka_01, df_Ruka_CC, on='Date')

final_df.to_csv('Levi - Ylläs - Ruka - Himos/Ruka_Combined/ruka_intermediate.csv', index=False)