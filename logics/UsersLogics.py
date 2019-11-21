import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import UsersResponses

USER_CREATE_URI = "/v1/usermanagement/users"
USER_CREATE_REQ_TYPE = "POST"

def GET_ID_AS_JSON(roles):
    try:
        allRoles = roles.split(",")
        allRolesJson = []
        for role in allRoles:
            e ={"id":int(role)}
            allRolesJson.append(e)
        return allRolesJson
    except:
        print("Error: list of roles isnt formatted correctly.")
        exit(1)

def GET_USER_CREATE_BODY(username,password,email,roles,description,firstname,lastname):
    b = json.dumps(
    #"roles":[{"id":10},{"id":11}],
    {
        "roles":GET_ID_AS_JSON(roles),
        "email":email,
        "enableAutoLogin":True,
        "username":username,
        "description":description,
        "firstName":firstname,
        "lastName":lastname,
        "disabled":False,
        "password":password,
        "licenseFeatures":["DEVELOPMENT"],
        "sysAssignedRoles":[]
    }
    )
    #print(b)
    return b

def create(username,password,email,roles,description,firstname,lastname):

    URL = DataUtils.GetUrl()+USER_CREATE_URI

    payload = GET_USER_CREATE_BODY(username,password,email,roles,description,firstname,lastname)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'X-Authorization': DataUtils.GetAuthToken()
    }

    response = requests.request(USER_CREATE_REQ_TYPE, URL, data=payload, headers=headers)
    isInError = UsersResponses.Process_Create_Response(response)
