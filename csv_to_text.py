import csv

with open('Custom Chaos Draft - Set Lists.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    first_line = next(csv_reader)
    num_of_cols = len(first_line)

    custom_sets = []
    # list of all the custom sets
    for n in range(0, num_of_cols):
        if (first_line[n] != ''):
            custom_sets.append(first_line[n])

    # skips lines 2 & 3 (on Google Sheets)
    next(csv_reader)
    next(csv_reader)

    matrix = []
    for row in csv_reader:
        matrix.append(row)


    for n in range (0, len(custom_sets)):
        common_setlist = []
        rare_setlist = []
        super_setlist = []
        ultra_setlist = []
        secret_setlist = []
        for m in range (0, len(matrix)): # len(matrix) is the number of rows; m is row number
            row = matrix[m]
            common_card = row[6*n + 0]
            rare_card = row[6*n + 1]
            super_card = row[6*n + 2]
            ultra_card = row[6*n + 3]
            secret_card = row[6 * n + 4]
            
            if common_card != '':
                common_setlist.append(common_card)
            if rare_card != '':
                rare_setlist.append(rare_card)
            if super_card != '':
                super_setlist.append(super_card)
            if ultra_card != '':
                ultra_setlist.append(ultra_card)
            if secret_card != '':
                secret_setlist.append(secret_card)
        with open("public/custom_packs_texts/" + custom_sets[n].replace(" ", "_").lower() + "/" + "01co.txt", "w") as outfile:
            for card in common_setlist:
                outfile.write(card)
                outfile.write('\n')
        with open("public/custom_packs_texts/" + custom_sets[n].replace(" ", "_").lower() + "/" + "02ra.txt", "w") as outfile:
            for card in rare_setlist:
                outfile.write(card)
                outfile.write('\n')
        with open("public/custom_packs_texts/" + custom_sets[n].replace(" ", "_").lower() + "/" + "03su.txt", "w") as outfile:
            for card in super_setlist:
                outfile.write(card)
                outfile.write('\n')
        with open("public/custom_packs_texts/" + custom_sets[n].replace(" ", "_").lower() + "/" + "04ul.txt", "w") as outfile:
            for card in ultra_setlist:
                outfile.write(card)
                outfile.write('\n')
        with open("public/custom_packs_texts/" + custom_sets[n].replace(" ", "_").lower() + "/" + "05se.txt", "w") as outfile:
            for card in secret_setlist:
                outfile.write(card)
                outfile.write('\n')
        #print(common_setlist)

    #print(custom_sets)
    #print(common_setlist)
    #print(rare_setlist)