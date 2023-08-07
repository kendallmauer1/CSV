import csv
from datetime import datetime
import matplotlib.pyplot as plt

#sitka, aslaska graph
infile_sak = open('sitka_weather_2018_simple.csv', 'r')
csv_file_sak = csv.reader(infile_sak)
header_row_sak = next(csv_file_sak)
print(header_row_sak)

for index, col_header in enumerate(header_row_sak):
    if col_header == 'TMIN':
        tmin_sak = index
    elif col_header == 'TMAX':
        tmax_sak = index
    elif col_header == 'DATE':
        date_sak = index
    elif col_header == 'NAME':
        name_sak = index

highs = []
dates = []
lows = []

some_date_sak = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(some_date_sak))

for row in csv_file_sak:
    try:
        name = row[name_sak]
        some_date_sak = datetime.strptime(row[date_sak], '%Y-%m-%d')
        high_sak = int(row[tmax_sak])
        low_sak = int(row[tmin_sak])
    except ValueError:
        print(f"Missing data for {some_date_sak}")
    else:
        highs.append(high_sak)
        lows.append(low_sak)
        dates.append(some_date_sak)

print(highs[:5])
print(dates[:5])

fig = plt.figure()

plt.subplot(2,1,1)

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title(name, fontsize=10)
plt.xlabel("Dates", fontsize=10)
plt.ylabel("Temps (F)", fontsize=10)
plt.tick_params(axis="both", which="major", labelsize=10)
fig.autofmt_xdate()


#death valley graph
infile_dv = open('death_valley_2018_simple.csv', 'r')
csv_file_dv = csv.reader(infile_dv)
header_row = next(csv_file_dv)

for index, col_header in enumerate(header_row):
    if col_header == 'TMIN':
        tmin_dv = index
    elif col_header == 'TMAX':
        tmax_dv = index
    elif col_header == 'DATE':
        date_dv = index
    elif col_header == 'NAME':
        name_dv = index

highs = []
dates = []
lows = []

some_date_dv = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(some_date_dv))

for row in csv_file_dv:
    try:
        name2 = row[name_dv]
        some_date_dv = datetime.strptime(row[date_dv], '%Y-%m-%d')
        high_dv = int(row[tmax_dv])
        low_dv = int(row[tmin_dv])
    except ValueError:
        print(f"Missing data for {some_date_dv}")
    else:
        highs.append(high_dv)
        lows.append(low_dv)
        dates.append(some_date_dv)

print(highs[:5])
print(dates[:5])

plt.subplot(2,1,2)

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title(name2, fontsize=10)
plt.xlabel("Dates", fontsize=10)
plt.ylabel("Temps (F)", fontsize=10)
plt.tick_params(axis="both", which="major", labelsize=10)
fig.autofmt_xdate()

plt.suptitle(f"Temperature comparison between {name} and {name2}")

plt.show()