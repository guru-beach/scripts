import requests
import json
import datetime
import numpy as np

headers = {'Content-type': 'application/json'}
rest_endpoint = 'http://api.bls.gov/publicAPI/v1/timeseries/data/'
start_year = 1948
stop_year = 2015
interval = 10
day = 1

series_dict = { 'LNS14000000' : { 'name': 'Unemployment, Season Adjusted : US',
                                  'data': []
                                },
                'LNU04000000' : { 'name': 'Unemployment, Season Unadjusted : US',
                                  'data': []
                                }
              }

def get_series_data(series_id, start_year, end_year):
  """Takes a series ID, start year, end year and returns a list of series
  tuples formatted as (datetime.date, float)"""
  data_list = []
  data = json.dumps({"seriesid": [series_id],"startyear": "{}".format(start_year), "endyear": "{}".format(end_year)})
  p = requests.post(rest_endpoint, data=data, headers=headers)
  json_data = json.loads(p.text)
  # print p.text
  for item in json_data['Results']['series'][0]['data']:
    period = item['period']
    year = int(item['year'])
    month = int(period.replace('M',''))
    value = float(item['value'])
    data_list.append((datetime.date(year, month, day), value))
  return data_list

def split_years(start_year, stop_year, interval):
  """Return a list of start/stop year doubles broken up into interval"""
  start_stop = []
  start_years = np.arange(start_year, stop_year, interval)
  for start in start_years:
    end = start + (interval - 1)
    if end > stop_year:
      end = stop_year
    start_stop.append((start,end))
  print start_stop
  return start_stop

 
for series_id in  series_dict.keys():
  for start, stop in split_years(start_year, stop_year, interval):
    #print "checking {} = {}".format(start, stop)
    series_data = get_series_data(series_id, start, stop)
    series_dict[series_id]['data'] += series_data

print series_dict


