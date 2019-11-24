import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import IQBotGroupResponses


LI_GROUP_LIST_URI = "/IQBot/api/bots"
LI_GROOUP_LIST_REQ_TYPE = "GET"

def list_groups(sessionname,CsvOutput,ProcessOutput = True):
    URL = urllib.parse.urljoin(DataUtils.GetUrl(sessionname), LI_GROUP_LIST_URI)

    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'X-Authorization': DataUtils.GetAuthToken(sessionname)
    }

    response = requests.request(LI_GROOUP_LIST_REQ_TYPE, URL, headers=headers)

    if(ProcessOutput):
        isInError = IQBotGroupResponses.Process_List_Response(response,CsvOutput)

    else:
        return response
