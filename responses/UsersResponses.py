import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import UsersTransformers

def Process_List_Response(res,CsvOutput):

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
            print(UsersTransformers.GetUserListAsCsv(result))
            return False
        else:
            print(result)
            return False

    else:
            if result['message']:
                print("Error Code: "+str(res.status_code)+" | Error Message: "+result['message'])
                return True
            else:
                print("Error Code: "+str(res.status_code))
                return True


def Process_Set_Login_Response(res):
    #"Credentials updated for test1"
    result = json.loads(res.text)
    if(res.status_code < 400):
        print(res.text)
        return False

    else:
            if result['message']:
                print("Error Code: "+str(res.status_code)+" | Error Message: "+result['message'])
                return True
            else:
                print("Error Code: "+str(res.status_code))
                return True


def Process_Delete_Response(res):
    #"Credentials updated for test1"
    result = json.loads(res.text)
    if(res.status_code < 400):
        print("user deleted: ["+result['username'] + " | "+str(result['id'])+ "]")
        return False

    else:
            if result['message']:
                print("Error Code: "+str(res.status_code)+" | Error Message: "+result['message'])
                return True
            else:
                print("Error Code: "+str(res.status_code))
                return True

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
            print("Error Code: "+str(res.status_code)+" | Error Message: "+result['message'])
            return True
        else:
            print("Error Code: "+str(res.status_code))
            return True
