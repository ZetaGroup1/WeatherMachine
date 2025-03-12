input_file = r"Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\Levi_06.csv" 
output_file = r"Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\Levi_06_cleaned.csv"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = [line.replace('""', '"') for line in lines]

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)