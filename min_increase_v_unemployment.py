import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from unemployment_dict import unemployment_dict as labor_data

years = YearLocator()   # every year
months = MonthLocator()  # every month
yearsFmt = DateFormatter('%Y')

d = datetime.date
d2n = mdates.date2num

# Series can be found: http://download.bls.gov/pub/time.series/la/la.series
series_info = { 
'LNS14000000' : 'Seasonally Adjusted Unemployment: US',
'LNU04000000' : 'Not Seasonally Adjusted Unemployment: US',
'LASDV534264400000003' : 'Unemployment Rate: Seattle-Bellevue-Everett, WA Metropolitan Division',
}
  
raise_pct_1938 = [
(d(1938, 10, 24), 20),
(d(1939, 10, 24), 20),
(d(1945, 10, 24), 30),
(d(1950, 1, 25), 85),
(d(1956, 3, 1), 30),
(d(1961, 9, 3), 15),
(d(1967, 2, 1), 15),
(d(1968, 2, 1), 14), 
(d(1974, 5, 1), 25),
(d(1975, 1, 1), 5), 
(d(1976, 1, 1), 9.5)
]

raise_pct_1961 = [
(d(1961, 9, 3), 20),
(d(1964, 9, 3), 15),
(d(1965, 9, 3), 9),
(d(1967, 2, 1), 15),
(d(1968, 2, 1), 14),
(d(1974, 5, 1), 25),
(d(1975, 1, 1), 5),
(d(1976, 1, 1), 9.5)
]

raise_pct_1966_nonfarm = [
(d(1967, 2, 1), 20),
(d(1968, 2, 1), 15),
(d(1969, 2, 1), 13),
(d(1970, 2, 1), 11.5),
(d(1971, 2, 1), 10),
(d(1974, 5, 1), 18.75),
(d(1975, 1, 1), 5),
(d(1976, 1, 1), 10),
(d(1977, 1, 1), 4.5)
]

raise_pct_1966_farm = [
(d(1967, 2, 1), 20),
(d(1968, 2, 1), 15),
(d(1969, 2, 1), 13),
(d(1974, 5, 1), 23),
(d(1975, 1, 1), 5),
(d(1976, 1, 1), 10),
(d(1977, 1, 1), 4.5)
]

raise_pct_1977 = [
(d(1978, 1, 1), 15),
(d(1979, 1, 1), 13.2),
(d(1980, 1, 1), 6.9),
(d(1981, 1, 1), 8.1),
(d(1990, 4, 1), 13.4),
(d(1991, 4, 1), 11.8),
(d(1996, 4, 1), 11.8),
(d(1997, 9, 1), 8.4),
(d(2007, 9, 24), 13.6),
(d(2008, 9, 24), 12),
(d(2009, 9, 24), 10.7)
]


# These don't need different x's in the list comprehension, but 
# Making is easier for other people to understand what these are for
raise_1938_dates = [x1[0] for x1 in  raise_pct_1938]
raise_1938_pct = [y1[1] for y1 in  raise_pct_1938]

raise_1961_dates = [x2[0] for x2 in raise_pct_1961]
raise_1961_pct = [y2[1] for y2 in raise_pct_1961]

raise_1966_nonfarm_dates = [x3[0] for x3 in raise_pct_1966_nonfarm]
raise_1966_nonfarm_pct = [y3[1] for y3 in raise_pct_1966_nonfarm]

raise_1966_farm_dates = [x4[0] for x4 in raise_pct_1966_farm]
raise_1966_farm_pct = [y4[1] for y4 in raise_pct_1966_farm]

raise_1977_dates = [x5[0] for x5 in raise_pct_1977]
raise_1977_pct = [y5[1] for y5 in raise_pct_1977]

# Seasonally Adjust Unemployment
ue_sa = labor_data['LNS14000000']['data']
ue_sa.sort()
ue_sa_dates = [x6[0] for x6 in ue_sa]
ue_sa_pct = [y6[1] for y6 in ue_sa]

# Seasonally Adjust Unemployment
ue_nsa = labor_data['LNU04000000']['data']
ue_nsa.sort()
ue_nsa_dates = [x7[0] for x7 in ue_nsa]
ue_nsa_pct = [y7[1] for y7 in ue_nsa]

# Seasonally adjusted Unemployment Seattle area
#ue_sa_seattle = labor_data['LASDV534264400000003']['data']
#ue_sa_seattle.sort()
#ue_sa_seattle_dates = [x8[0] for x8 in ue_sa_seattle]
#ue_sa_seattle_pct = [y8[1] for y8 in ue_sa_seattle]



fig, ax1 = plt.subplots()
bar1 = ax1.bar(raise_1938_dates, raise_1938_pct, width=10, color='k', edgecolor='k', label='1938 Law')
bar2 = ax1.bar(raise_1961_dates, raise_1961_pct, width=10, color='m', edgecolor='m', label='1961 Law')
bar3 = ax1.bar(raise_1966_nonfarm_dates, raise_1966_nonfarm_pct, width=10, color='c', edgecolor='c', label='1966 Nonfarm Law')
bar4 = ax1.bar(raise_1966_farm_dates, raise_1966_farm_pct, width=10, color='y', edgecolor='y', label='1966 Farm Law')
bar5 = ax1.bar(raise_1977_dates, raise_1977_pct, width=10, color='b', edgecolor='b', label='1977 Law')
ax1.xaxis_date()
ax1.set_xlabel('Time')
ax1.set_ylabel('Minimum Wage Raise %', color='b')
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
ax1.xaxis.set_minor_locator(months)
for tl in ax1.get_yticklabels():
    tl.set_color('b')
ax1.grid(which='both', color='green')
ax1.autoscale_view()
ax1.legend(loc=2)

ax2 = ax1.twinx()
line1 = ax2.plot(ue_sa_dates, ue_sa_pct,  'r-', label='US Unemployment Rate: Seasonally Adjusted')
line2 = ax2.plot(ue_nsa_dates, ue_nsa_pct,  'g-', label='US Unemployment Rate: Non-Seasonally Adjusted')
#line3 = ax2.plot(ue_sa_seattle_dates, ue_sa_seattle_pct,  'g-')
ax2.set_ylabel('Unemployment %', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
ax2.legend(loc=1)

plt.show()
