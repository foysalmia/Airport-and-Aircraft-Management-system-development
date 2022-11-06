import csv

with open("./data/curancyrates.csv", 'r') as CurFile:
    lines = csv.reader(CurFile)
    for line in lines:
        if 'Bangladesh' in line[0]:
            print(line)
