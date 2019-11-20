import requests
import json
import sys
import os

sys.path.insert(1, './libs')
import DataUtils


# {"code":"UM1114","details":"To be safe, we logged you off here.  Please log in again.","message":"You are logged in twice"}
def Process_Auth_Token_Response(res):
    #print(res)
    result = json.loads(res.text)
    #print(res.text)
    if(res.status_code < 400):
        print("Token is valid, corresponding username: "+result['user']['username'])
        return False
    else:
        if result['details']:
            print("Error Code: "+res.status_code+" | Error Message: "+result['details'])
            return True
        else:
            print("Error Code: "+res.status_code)
            return True

def Process_Auth_Login_Response(res,url):
    result = json.loads(res.text)
    #print(res.text)
    if(res.status_code < 400):
        #print(result['token'])
        token = result['token']
        print("Token:["+token+"]")
        DataUtils.StoreAuthToken(token)
        DataUtils.StoreUrl(url)
        return False

    else:
        if result['message']:
            print("Error Code: "+res.status_code+" | Error Message: "+result['message'])
            return True
        else:
            print("Error Code: "+res.status_code)
            return True

def Process_Auth_Logout_Response(res):

    if(res.status_code < 400):
        print("Success")
        return False

    else:
        print("Error Code: "+str(res.status_code))
        return True
