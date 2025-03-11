input_file = r"Levi - Ylläs - Ruka - Himos\Ylläs_Cloud_Coverage\Ylläs_04_cleaned.csv"
output_file = r"Levi - Ylläs - Ruka - Himos\Ylläs_Cloud_Coverage\Ylläs_04_cleaned_2.csv"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    line = line.strip().strip('"') 
    line = line.replace('""', '"')
    cleaned_lines.append(line + "\n") 

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)