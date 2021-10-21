import json
import ssl
import urllib3
import pathlib
watchlist_file = pathlib.Path(__file__).parent / 'watchlist.json'
def get_tool_information(toolName):
    watchlist = open(watchlist_file)
    data = json.load(watchlist)
    for tool in data["Tools"]:
        if toolName in tool["name"]:
            return tool
    raise Exception("{0} not found in the watchlist, please add it.".format(toolName))
def get_tool_url(toolName):
    toolinfo = get_tool_information(toolName)
    return toolinfo["url"]
def fetch_tool(url):
    https = urllib3.PoolManager(cert_reqs = ssl.CERT_NONE)
    urllib3.disable_warnings()
    req = https.request('GET',url)
    return req.data

