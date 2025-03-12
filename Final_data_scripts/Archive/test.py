import pandas as pd

df_serena = pd.read_csv('C:\Code\miniproject_2\WeatherMachine\Pyhätunturi - Mustavaara - Serena\Serena_snow_temp_preci.csv')

df_pyhätunturi = pd.read_csv('C:\Code\miniproject_2\WeatherMachine\Pyhätunturi - Mustavaara - Serena\Pyhäntunturi_snow_temp_preci.csv')

df_mustavaara = pd.read_csv('C:\Code\miniproject_2\WeatherMachine\Pyhätunturi - Mustavaara - Serena\Mustavaara_snow_temp_preci.csv')



value_to_check = '-'

count = (df_serena['Snow depth [cm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

count = (df_pyhätunturi['Snow depth [cm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

count = (df_mustavaara['Snow depth [cm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

count = (df_serena['Precipitation amount [mm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

count = (df_pyhätunturi['Precipitation amount [mm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

count = (df_mustavaara['Precipitation amount [mm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

count = (df_pyhätunturi['Average temperature [°C]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

count = (df_serena['Average temperature [°C]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

count = (df_mustavaara['Average temperature [°C]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

# Convert 'Snow depth [cm]' to numeric, replacing '-' with NaN
df_serena['Snow depth [cm]'] = pd.to_numeric(df_serena['Snow depth [cm]'], errors='coerce')
 
# Fill NaN values with a 7-day rolling mean
df_serena['Snow depth [cm]'] = df_serena['Snow depth [cm]'].fillna(df_serena['Snow depth [cm]'].rolling(7, min_periods=1).mean())

count = (df_serena['Snow depth [cm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

# Convert 'Snow depth [cm]' to numeric, replacing '-' with NaN
df_pyhätunturi['Snow depth [cm]'] = pd.to_numeric(df_pyhätunturi['Snow depth [cm]'], errors='coerce')
 
# Fill NaN values with a 7-day rolling mean
df_pyhätunturi['Snow depth [cm]'] = df_pyhätunturi['Snow depth [cm]'].fillna(df_pyhätunturi['Snow depth [cm]'].rolling(7, min_periods=1).mean())

count = (df_pyhätunturi['Snow depth [cm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

# Convert 'Snow depth [cm]' to numeric, replacing '-' with NaN
df_mustavaara['Snow depth [cm]'] = pd.to_numeric(df_mustavaara['Snow depth [cm]'], errors='coerce')
 
# Fill NaN values with a 7-day rolling mean
df_mustavaara['Snow depth [cm]'] = df_mustavaara['Snow depth [cm]'].fillna(df_mustavaara['Snow depth [cm]'].rolling(7, min_periods=1).mean())

count = (df_mustavaara['Snow depth [cm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

# Convert 'Snow depth [cm]' to numeric, replacing '-' with NaN
df_mustavaara['Average temperature [°C]'] = pd.to_numeric(df_mustavaara['Average temperature [°C]'], errors='coerce')
 
# Fill NaN values with a 7-day rolling mean
df_mustavaara['Average temperature [°C]'] = df_mustavaara['Average temperature [°C]'].fillna(df_mustavaara['Average temperature [°C]'].rolling(7, min_periods=1).mean())

count = (df_serena['Snow depth [cm]'] == value_to_check).sum()
print(f"{value_to_check} appears {count} times in the column.")

df_serena.to_csv('Serena_t_s_p.csv', index = False)
df_pyhätunturi.to_csv('Pyhätunturi_t_s_p.csv', index = False)
df_mustavaara.to_csv('Mustavaara_t_s_p.csv', index = False)