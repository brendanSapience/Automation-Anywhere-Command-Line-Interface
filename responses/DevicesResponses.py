import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import DevicesTransformers


def Process_list_Response(res,CsvOutput):

    result = json.loads(res.text)

    try:
        if result['code'] == "UM1111":
            print("You were logged out, please login again.")
            return True
        else:
            print("unknown error.")
            return True
    except:
        pass

    if(res.status_code < 400):
        if CsvOutput:
            print(DevicesTransformers.GetDeviceListAsCsv(result))
            return False
        else:
            print(result)
            return False

    else:
            if result['message']:
                print("Error Code: "+res.status_code+" | Error Message: "+result['message'])
                return True
            else:
                print("Error Code: "+res.status_code)
                return True
