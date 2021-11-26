from mitmproxy import http
from datetime import datetime
from bs4 import BeautifulSoup

def response(flow: http.HTTPFlow):
    if flow.request.headers['accept'].startswith('text/html,application/xhtml+xml,application/xml'):
        soup=BeautifulSoup(flow.response.content)
        file=str(datetime.fromtimestamp(int(flow.response.timestamp_start))).split(' ')[0]
        with open('../logs/ '[:-1]+file,'a+') as f:
            f.write(str(datetime.fromtimestamp(int(flow.response.timestamp_start)))+ ' '+soup.title.string+' '+str(flow.request.url)+'\n\n')
