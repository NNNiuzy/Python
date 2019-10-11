import csv

filename = 'data/sitka_weather_2018_full.csv'
with open(filename)as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)