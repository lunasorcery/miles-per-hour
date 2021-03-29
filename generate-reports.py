#!/usr/local/bin/python3
import csv
import calendar
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

name = 'Miles'
years = range(1880, 2020)
milesPerHourAllYears = []

for year in years:
	miles = 0
	with open(f"names/yob{year}.txt") as csvfile:
		for row in csv.reader(csvfile):
			if (row[0] == name):
				miles += int(row[2])

	daysInYear = 366 if calendar.isleap(year) else 365
	milesPerHour = miles / (daysInYear * 24)
	milesPerHourAllYears.append(milesPerHour)
	print(f"Birth rate in {year}: {milesPerHour:.5f} mph")

fig, ax = plt.subplots()
plt.bar(years, milesPerHourAllYears)
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.xlabel('Year')
plt.ylabel(f"Birth Rate ({name}/Hour)")
plt.title(f"How Often People Called '{name}' Are Born In The U.S.")
plt.savefig('out.png', dpi=200)
plt.savefig('out.svg')

# wide version for twitter
# make the figure 16:8 so the overall image is ~16:9
ax.set_aspect(((max(years)-min(years))/max(milesPerHourAllYears))/(16/8))
plt.savefig('out-wide.png', dpi=200, bbox_inches='tight', pad_inches=0.3)
