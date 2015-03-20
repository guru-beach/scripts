import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

d = datetime.date
d2n = mdates.date2num

labor_data {
  'LNS14000000' : { 'name' : 'Seasonally Adjusted Unemployment: US',
                    'data' : []
                  }
  'LNU04000000' : { 'name' : 'Not Seasonally Adjusted Unemployment: US',
                    'data' : []
                  }
  'LAUMT534266000000006' : { 'name' : 'Not Seasonally Adjusted Unemployment: SEATAC'
                             'data' : []
                           }
}

def import_unemployment():
  
raise_pct_1938 = [
(d(1938, 10, 24), 100),
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
(d(1961, 9, 3), 100),
(d(1964, 9, 3), 15),
(d(1965, 9, 3), 9),
(d(1967, 2, 1), 15),
(d(1968, 2, 1), 14),
(d(1974, 5, 1), 25),
(d(1975, 1, 1), 5),
(d(1976, 1, 1), 9.5)
]

raise_pct_1966_nonfarm = [
(d(1967, 2, 1), 100),
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
(d(1967, 2, 1), 100),
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
