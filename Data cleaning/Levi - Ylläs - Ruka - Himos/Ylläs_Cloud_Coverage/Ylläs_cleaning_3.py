with open('Levi - Ylläs - Ruka - Himos\Ylläs_Cloud_Coverage\Ylläs_04_3.csv', 'r') as infile, open('Levi - Ylläs - Ruka - Himos\Ylläs_Cloud_Coverage\Ylläs_04.csv', 'w') as outfile:
    for line in infile:
        if line.endswith('\n'):
            line = line.rstrip('\n') + '"\n'
        else:
            line = line + '"'
        outfile.write(line)