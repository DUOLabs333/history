import json
from datetime import datetime

with open('./firefox_history.json','r') as f:
    file=json.load(f)

for l in file:
    date=str(datetime.fromtimestamp(l['timestamp']/1000000)).split(' ')[0]
    with open ('./history/logs/ '[:-1]+date,'a+') as f:
        f.write(str(datetime.fromtimestamp(l['timestamp']/1000000))+ ' '+str(l['description'])+ ' '+l['href']+'\n\n')
