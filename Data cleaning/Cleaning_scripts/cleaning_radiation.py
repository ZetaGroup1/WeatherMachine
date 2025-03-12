import pandas as pd
import numpy as np

df = pd.read_csv('C:\Code\miniproject_2\Direct_solar_radiation.csv')

df.drop('Observation station', axis = 1, inplace=True)

df['Direct solar radiation mean [W/m2]'] = pd.to_numeric(df['Direct solar radiation mean [W/m2]'], errors='coerce')

df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month


'''df_2013 = df[df['Date'].dt.year == 2013]

for i in range(len(df_2013)):
    prev_year_date = df_2013.iloc[i]['Date'] - pd.DateOffset(years=1)
    prev_year_data = df[df['Date'] == prev_year_date]
    df_2013.iloc[i, df_2013.columns.get_loc('Direct solar radiation mean [W/m2]')] = prev_year_data['Direct solar radiation mean [W/m2]'].values[0]

df.update(df_2013)'''

#update the values in year 2013 with values from 2012 where there is missing values
df_2013 = df[df['Date'].dt.year == 2013]

for i in range(len(df_2013)):
    if pd.notna(df_2013.iloc[i]['Direct solar radiation mean [W/m2]']):
        continue
    else:
        prev_year_date = df_2013.iloc[i]['Date'] - pd.DateOffset(years=1)
        prev_year_data = df[df['Date'] == prev_year_date]
        
        df_2013.iloc[i, df_2013.columns.get_loc('Direct solar radiation mean [W/m2]')] = prev_year_data['Direct solar radiation mean [W/m2]'].values[0]
   
df.update(df_2013)

#update the values in year 2014 with values from 2013 where there is missing values
df_2014 = df[df['Date'].dt.year == 2014]

for i in range(len(df_2014)):
    if pd.notna(df_2014.iloc[i]['Direct solar radiation mean [W/m2]']):
        continue
    else:
        prev_year_date = df_2014.iloc[i]['Date'] - pd.DateOffset(years=1)
        prev_year_data = df[df['Date'] == prev_year_date]
        
        df_2014.iloc[i, df_2014.columns.get_loc('Direct solar radiation mean [W/m2]')] = prev_year_data['Direct solar radiation mean [W/m2]'].values[0]
   
df.update(df_2014)

#update the values in year 2015 with values from 2014 where there is missing values
df_2015 = df[df['Date'].dt.year == 2015]

for i in range(len(df_2015)):
    if pd.notna(df_2015.iloc[i]['Direct solar radiation mean [W/m2]']):
        continue
    else:
        prev_year_date = df_2015.iloc[i]['Date'] - pd.DateOffset(years=1)
        prev_year_data = df[df['Date'] == prev_year_date]
        
        df_2015.iloc[i, df_2015.columns.get_loc('Direct solar radiation mean [W/m2]')] = prev_year_data['Direct solar radiation mean [W/m2]'].values[0]
   
df.update(df_2015)

#calculating the mean

monthly_means = df.groupby(['year', 'month'])['Direct solar radiation mean [W/m2]'].mean().reset_index(name='monthly_mean')
df = pd.merge(df, monthly_means.round(2), on=['year', 'month'], how='left')
df = df.drop(columns=['year', 'month'])

df.to_csv('Direct_solar_radiation_mean.csv', index=False)