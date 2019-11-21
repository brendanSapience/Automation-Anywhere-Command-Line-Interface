import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils



def Process_Create_Response(res):

    result = json.loads(res.text)
    #print(result)
    try:
        if result['code'] == "UM1111":
            print("You were logged out, please login again.")
            return True
        else:
            if result['message']:
                print(result['message'])
                if result['details']:
                    print(result['details'])
                return True
            else:
                print("unknown error.")
                return True
    except:
        pass

    if(res.status_code < 400):
        #print(result)
        print("user created with ID:"+str(result['id']))
        return False

    else:
        if result['message']:
            print("Error Code: "+res.status_code+" | Error Message: "+result['message'])
            return True
        else:
            print("Error Code: "+res.status_code)
            return True
