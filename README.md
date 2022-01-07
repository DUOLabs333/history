history: MITM proxy your browsing history, and search for it later

How to use:
1. Clone the repository
1. Make a `history` script:
```
#!/bin/bash
cd index
./recollindex -m -w 0 -D -c . &

cd ../search
pdm run --site-packages python ./webui-standalone.py -p 2012 -c ../index &

cd ../proxy
LANG=en_US.UTF-8 pdm run mitmdump --listen-host 127.0.0.1 -p 2011  -s history.py --ssl-insecure --set stream_large_bodies="1m" --no-http2 
```
1. Make a `logs` directory
1. Change `index/recoll.conf` to the absolute path of `logs`.
1. Change the ports in `history` to match the ports for the proxy and webui you want.
1. Install pdm with `pip install pdm`
1. Go into `proxy` and do `pdm sync -r`
1. Go to `index/search` and do `pdm sync -r`
1. Go to `index` and replace `recollindex` with one from your distribution or with one manually compiled (you do not need it to be compiled with inotify, but if you do, you must change `history` to index with a cron job)
1. Run `history`
1. Point your browser to your proxy
1. Go to your webui
1. Profit!

This tool uses two other tools -- mitmproxy and recoll. Credit goes to the developers of both.

