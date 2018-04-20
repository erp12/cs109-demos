import csv


##with open('iris.csv', 'r') as csv_file:
##    csv_reader = csv.reader(csv_file)
##    for row in csv_reader:
##        print(row)


# Find the average petal length
petal_lengths = []
with open('iris.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first_row = True
    for row in csv_reader:
        if first_row:
            first_row = False
        else:
            petal_lengths.append(float(row[2]))

avg_petal_length = sum(petal_lengths) / len(petal_lengths)
print("Mean petal length: " + str(avg_petal_length))
print()


# Average petal length for each species
petal_lengths = {}
with open('iris.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first_row = True
    for row in csv_reader:
        if first_row:
            first_row = False
        else:
            species = row[-1]
            if species not in petal_lengths.keys():
                petal_lengths[species] = []
            petal_lengths[species].append(float(row[2]))
                
                
for k, v in petal_lengths.items():
    avg_petal_length = sum(v) / len(v)
    print("Mean " + k + " petal length: " + str(avg_petal_length))

