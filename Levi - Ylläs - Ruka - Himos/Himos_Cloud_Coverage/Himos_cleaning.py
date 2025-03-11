input_file = r"Levi - Ylläs - Ruka - Himos\Himos_Cloud_Coverage\Himos_03.csv"
output_file = r"Levi - Ylläs - Ruka - Himos\Himos_Cloud_Coverage\Himos_03_cleaned.csv"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = [line.replace('""', '"') for line in lines]

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)