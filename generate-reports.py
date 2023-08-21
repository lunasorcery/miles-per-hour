#!/usr/bin/env python3

import csv
import calendar
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

name = 'Miles'
years = range(1880, 2023)
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

fig.subplots_adjust(left=0.05, right=0.85, top=0.9, bottom=0.125)

ax.yaxis.tick_right()
ax.yaxis.set_label_position('right')
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())

ax.set_xlabel('Year', labelpad=5, fontsize=12)
ax.set_ylabel(f"Birth Rate ({name}/Hour)", labelpad=15, fontsize=12)

plt.title(f"How Often People Called '{name}' Are Born In The U.S.")
plt.savefig('out.png', dpi=200)
plt.savefig('out.svg')
