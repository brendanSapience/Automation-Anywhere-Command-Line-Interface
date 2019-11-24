import requests
import json
import sys
import os

sys.path.insert(1, './libs')
import DataUtils
import StdResponses

# {"code":"UM1114","details":"To be safe, we logged you off here.  Please log in again.","message":"You are logged in twice"}
def Process_Auth_Token_Response(res):

    if(res.status_code >= 400):
        print("Error Code: "+str(res.status_code))
        try:
            result = json.loads(res.text)
            if result['message']:
                print("Error Message: "+result['details'])
                return True
        except:
            return True

        return True

    else:
        try:
            result = json.loads(res.text)
            print("Token is valid, corresponding username: "+result['user']['username'])
            return False
        except:
            print("Unknown Error.")
            return True

def Process_Auth_Login_Response(res,url,sessionname):

    if(res.status_code >= 400):
        print("Error Code: "+str(res.status_code))
        try:
            result = json.loads(res.text)
            if result['message']:
                print("Error Message: "+result['message'])
                return True
        except:
            return True

        return True

    else:
        try:
            result = json.loads(res.text)
            #print(result['token'])
            token = result['token']
            #print("Token:["+token+"]")
            print("Token Stored in session: "+sessionname)
            DataUtils.StoreAuthToken(token,sessionname)
            DataUtils.StoreUrl(url,sessionname)
            return False
        except:
            print("Unknown Error.")
            return True


def Process_Auth_Logout_Response(res,sessionname):

    if(res.status_code >= 400):
        print("Error Code: "+str(res.status_code))
        return True
    else:
        print("Success: logged out of session: "+sessionname)
        return False
