from mitmproxy import http
from datetime import datetime
from bs4 import BeautifulSoup

def responseheaders(flow):
    if not flow.request.headers['accept'].startswith('text/html,application/xhtml+xml,application/xml'):
        flow.response.stream = True

def response(flow: http.HTTPFlow):
    if flow.request.headers['accept'].startswith('text/html,application/xhtml+xml,application/xml'):
        try:
            title=BeautifulSoup(flow.response.content).title.string
        except:
            return
        file=str(datetime.fromtimestamp(int(flow.response.timestamp_start))).split(' ')[0]
        with open('../logs/ '[:-1]+file,'a+') as f:
            f.write(str(datetime.fromtimestamp(int(flow.response.timestamp_start)))+ ' '+title+' '+str(flow.request.url)+'\n\n')
