import pandas as pd
import glob
 
# Load all weather files
file_paths = glob.glob("C:\Code\miniproject_2\WeatherMachine\Data cleaning\Final_merge\Final\*.csv")  # Adjust path
dfs = {file.split("/")[-1]: pd.read_csv(file) for file in file_paths}
 
# Quick inspection
for name, df in dfs.items():
    print(f"{name}: {df.shape}, Missing: {df.isnull().sum().sum()}")


import matplotlib.pyplot as plt
 
# Plot snow depth trends

for name, df in dfs.items():
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    df["Snow depth [cm]"].plot(label=name, alpha=0.7)
plt.legend()
plt.title("Snow Depth Over Time")
plt.show()

 