import json
import requests

### PARAMETERS ###
stats = [ "B19001_{0:03d}E".format(x) for x in range(1,17)]
# Aggregate:Subaggregate.  This is the NAME Column
get_for = 'us:*'
# Used for the 'in' filter
get_in = None
# Used for API key
get_key = None
# Used for selecting the API year, this probably varies by API
year = 2013
acs_type = 'acs5'
### /PARAMETERS ###

base_url = 'http://api.census.gov/data'

def get_acs_stats(acs_type, acs_year, stats, get_for, get_in, get_key):

  """IN:
  acs_type : list in ['acs1', 'acs3', 'acs5']
  acs_year : The year to query the API for.
  stats    : list of ACS5 variables
  get_for  : Aggregation information in format <category>:<filter>
  get_in   : Aggregation filter
  get_key  : ACS5 connection key
  OUT:
  data_dict : { aggregate : [value1, value2] }
  The list of values will match the statistics list"""

  url = "{}/{}/{}".format(base_url, acs_year, acs_type)
  params = { 
   'get' : "NAME,{}".format(','.join(stats)),
   'for' : get_for,
   'in'  : get_in,
   'key' : get_key
  }
  
  data_dict = { }
  r = requests.get(url, params=params)
  # First row is the header
  head = r.json()[0]
  # All the rest of the JSON object is data
  data = r.json()[1:]
  
  # This is usually a fixed value (Name), but capture just in case
  head_name = head[0]
  # This is the tail column, typically an id
  # Now the header list should only have data columns
  head_id = head[-1]
  
  for row in data:
    # Take out the first and last column
    name = row[0]
    name_id = row[-1]
    # There should only ever be one of these values in a response, so it can be used as a row key
    data_dict[name] = row[1:-1] 
    # Extract the records and insert a map of name to value based on the 
    # header data
  print data_dict
  return data_dict


if __name__ == '__main__':
  get_acs_stats(acs_type, year, stats, get_for, get_in, get_key)
