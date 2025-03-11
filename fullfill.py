import pandas as pd

df = pd.read_csv('Direct_solar_radiation_copy_test.csv', parse_dates=['Date'])


df_2013 = df[df['Date'].dt.year == 2013]

for i in range(len(df_2013)):
    prev_year_date = df_2013.iloc[i]['Date'] - pd.DateOffset(years=1)
    prev_year_data = df[df['Date'] == prev_year_date]
    df_2013.iloc[i, df_2013.columns.get_loc('Direct solar radiation mean [W/m2]')] = prev_year_data['Direct solar radiation mean [W/m2]'].values[0]


df.update(df_2013)

df.to_csv('Direct_solar_radiation_copy_test_final.csv')