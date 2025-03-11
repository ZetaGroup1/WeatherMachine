import pandas as pd

# Define input and output file names
input_file = r"Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\Levi_06.csv"  # Use raw string (r"") to handle backslashes in paths
output_file = r"Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\Levi_06_cleaned.csv"

# Read the CSV file as a raw text to remove unwanted quotes
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Remove extra double quotes manually
cleaned_lines = [line.replace('""', '"') for line in lines]

# Save the cleaned file
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)

print(f"Cleaned CSV saved as {output_file}")