import logging
import pathlib
import azure.functions as func
from . import binproxy

watchlist_file = pathlib.Path(__file__).parent / 'watchlist.json'

def main(req: func.HttpRequest) -> func.HttpResponse:
    toolName = ""
    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        toolName = req_body.get('name')     
    if toolName:
        url = binproxy.get_tool_url(toolName)
        bin_data = binproxy.fetch_tool(url)
        return func.HttpResponse(bin_data) 
       