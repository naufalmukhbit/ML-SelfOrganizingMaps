import csv

with open('Tugas 2 ML Genap 2018-2019 Dataset Tanpa Label.csv', mode='r') as csv_input:         # Input from DataTugas2.csv file
    bltData = csv.reader(csv_input)
    next(bltData)                                           # Skip the first row
    for row in bltData:
        income.append(float(row[1]))                        # Insert second column to 'income' array
        debt.append(float(row[2]))