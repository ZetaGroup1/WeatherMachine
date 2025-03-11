with open('Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\Levi_06_3.csv', 'r') as infile, open('Levi - Ylläs - Ruka - Himos\Levi_Cloud_Coverage\Levi_06.csv', 'w') as outfile:
    for line in infile:
        if line.endswith('\n'):
            line = line.rstrip('\n') + '"\n'
        else:
            line = line + '"'
        outfile.write(line)