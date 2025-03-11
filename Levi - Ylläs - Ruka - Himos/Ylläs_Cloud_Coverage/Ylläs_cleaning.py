input_file = r"Levi - Ylläs - Ruka - Himos\Ylläs_Cloud_Coverage\Ylläs_04.csv"
output_file = r"Levi - Ylläs - Ruka - Himos\Ylläs_Cloud_Coverage\Ylläs_04_cleaned.csv"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = [line.replace('""', '"') for line in lines]

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)