import requests
import json
start_year = '1947'
end_year   = '2015'
headers = {'Content-type': 'application/json'}
rest_endpoint = 'http://api.bls.gov/publicAPI/v1/timeseries/data/'

series_dict = { 'LNS14000000' : { 'name': 'Unemployment, Season Adjusted : US',
                                  'data': []
                                },
                'LNU04000000' : { 'name': 'Unemployment, Season Unadjusted : US',
                                  'data': []
                                }
              }

series = series_dict.keys()


data = json.dumps({"seriesid": series,"startyear":start_year, "endyear":end_year})
p = requests.post(rest_endpoint, data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        month = period.replace('M','')
        value = item['value']
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
            x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    output = open(&quot;c:\\temp\\&quot; + seriesId + &quot;.txt&quot;,&quot;w&quot;)
    output.write (x.get_string())
    output.close()
    
