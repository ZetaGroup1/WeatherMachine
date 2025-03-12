with open('Levi - Ylläs - Ruka - Himos\Himos_Cloud_Coverage\Himos_03_3.csv', 'r') as infile, open('Levi - Ylläs - Ruka - Himos\Himos_Cloud_Coverage\Himos_03.csv', 'w') as outfile:
    for line in infile:
        if line.endswith('\n'):
            line = line.rstrip('\n') + '"\n'
        else:
            line = line + '"'
        outfile.write(line)