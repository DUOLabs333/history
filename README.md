history: MITM proxy your browsing history, and search for it later

How to use:
1. Clone the repository
1. Make a `logs` directory
1. Change `index/recoll.conf` to the absolute path of `logs`.
1. Change the ports in `history` to match the ports for the proxy and webui you want.
1. Install pdm with `pip install pdm`
1. Go into `proxy` and do `pdm reinstall`
1. Go to `index/search` and do `pdm reinstall`
1. Go to `index` and replace `recollindex` with one from your distribution or with one manually compiled (you do not need it to be compiled with inotify, but if you do, you must change `history` to index with a cron job)
1. Run `history`
1. Point your browser to your proxy
1. Go to your webui
1. Profit!

This tool uses two other tools -- mitmproxy and recoll. Credit goes to the developers of both.

