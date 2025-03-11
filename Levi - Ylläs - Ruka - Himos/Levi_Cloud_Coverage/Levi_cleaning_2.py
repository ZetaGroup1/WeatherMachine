import pandas as pd

# Define input and output file names
input_file = r"Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\Levi_06_cleaned.csv"
output_file = r"Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\Levi_06_cleaned_2.csv"

# Read the CSV file as raw text
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Clean each line:
cleaned_lines = []
for line in lines:
    # Remove surrounding quotes from each line and ensure correct formatting
    line = line.strip().strip('"')  # Remove any starting or ending quotes
    line = line.replace('""', '"')  # Fix doubled-up quotes
    cleaned_lines.append(line + "\n")  # Keep correct newline format

# Save the cleaned file
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)

print(f"Cleaned CSV saved as {output_file}")