import pandas as pd

df_Ylläs_01 = pd.read_csv('Levi - Ylläs - Ruka - Himos/Ylläs_Others/Ylläs_01.csv')

df_Ylläs_01['Date'] = pd.to_datetime(df_Ylläs_01[['Year', 'Month', 'Day']])
df_Ylläs_01 = df_Ylläs_01[['Date', 'Precipitation amount [mm]', 'Snow depth [cm]', 'Average temperature [°C]']]

df_Ylläs_CC = pd.read_csv('Levi - Ylläs - Ruka - Himos/Ylläs_Cloud_Coverage/combined/Ylläs_combined.csv')

df_Ylläs_CC = df_Ylläs_CC[['Date', 'cloud_cover_code']]

df_Ylläs_CC['Date'] = pd.to_datetime(df_Ylläs_CC['Date'])

final_df = pd.merge(df_Ylläs_01, df_Ylläs_CC, on='Date')

final_df.to_csv('Levi - Ylläs - Ruka - Himos/Ylläs_Combined/ylläs_intermediate.csv', index=False)