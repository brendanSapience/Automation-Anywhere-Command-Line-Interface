import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import RolesResponses

ROLES_LIST_URI = "/v1/usermanagement/roles/list"
ROLES_LIST_REQ_TYPE = "POST"

def GET_LIST_BODY():
    b = json.dumps(
        {
            "sort":
                [
                    {
                    "field":"name",
                    "direction":"asc"
                    }
                ],
            "filter":{},
            "fields":[],
            "page":
            {
            "length":200,
            "offset":0
            }
        }
    )
    return b

def list(sessionname,CsvOutput):

    URL = DataUtils.GetUrl(sessionname)+ROLES_LIST_URI

    payload = GET_LIST_BODY()
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'X-Authorization': DataUtils.GetAuthToken(sessionname)
    }

    response = requests.request(ROLES_LIST_REQ_TYPE, URL, data=payload, headers=headers)
    isInError = RolesResponses.Process_list_Response(response,CsvOutput)
