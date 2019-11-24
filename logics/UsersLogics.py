import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import UsersResponses

USER_CREATE_URI = "/v1/usermanagement/users"
USER_CREATE_REQ_TYPE = "POST"

USER_SETLOGIN_URI = "/v2/credentialvault/loginsetting"
USER_SETLOGIN_REQ_TYPE = "PUT"

USER_LIST_URI = "/v1/usermanagement/users/list"
USER_LIST_REQ_TYPE = "POST"

USER_DELETE_URI = "/v1/usermanagement/users"
USER_DELETE_REQ_TYPE = "DELETE"

def ConvertUsernameToList(username):
    if("," in username):
        return username.split(",")
    else:
        return [username]

def ConvertUsernameToListOfIDs(username,sessionname):
    ListOfUsernames = username.split(",")
    Mappings = {}
    try:
        res = list(sessionname,False,False)
        JsonListOfUsers = json.loads(res.text)

        UserList = JsonListOfUsers['list']
        for item in UserList:
            ID = item['id']
            USERNAME = item['username']
            if(USERNAME in ListOfUsernames):
                Mappings[USERNAME] = ID
        #print(Mappings)
        return Mappings
    except:
        print("An error occured while retrieving the list of existing users.")
        exit(1)

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

def GET_USER_LIST_BODY():
    b = json.dumps(
    {
    "sort":[
        {"field":"username",
        "direction":"asc"}
    ],
    "filter":{},
    "fields":[],
    "page":{
        "offset":0,
        "total":12,
        "totalFilter":12,
        "length":200
        }
    }
    )
    #print(b)
    return b

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

def GET_USER_SET_LOGIN_BODY(username,loginuser,loginpassword):
    b = json.dumps(
    {
        "username":username,
        "loginUsername":loginuser,
        "loginPassword":loginpassword
    }
    )
    #print(b)
    return b


def list(sessionname,CsvOutput,ProcessOutput = True):

    URL = urllib.parse.urljoin(DataUtils.GetUrl(sessionname), USER_LIST_URI)
    payload = GET_USER_LIST_BODY()
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'X-Authorization': DataUtils.GetAuthToken(sessionname)
    }

    response = requests.request(USER_CREATE_REQ_TYPE, URL, data=payload, headers=headers)
    if(ProcessOutput):
        isInError = UsersResponses.Process_List_Response(response,CsvOutput)
    else:
        return response

def delete(sessionname,username):
    # delete API endpoint only takes the user id and not the user Name
    # all usernames passed need to be first converted to a list of user ids
    AllUsernames = ConvertUsernameToListOfIDs(username,sessionname)

    for username,userid in  AllUsernames.items():
        URL = urllib.parse.urljoin(DataUtils.GetUrl(sessionname), USERUSER_DELETE_URI,str(userid))
        USER_LIST_URI
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'X-Authorization': DataUtils.GetAuthToken(sessionname)
        }

        response = requests.request(USER_DELETE_REQ_TYPE, URL, headers=headers)
        isInError = UsersResponses.Process_Delete_Response(response)

def create(sessionname,username,password,email,roles,description,firstname,lastname):
    AllUsernames = ConvertUsernameToList(username)

    for aUser in  AllUsernames:

        URL = urllib.parse.urljoin(DataUtils.GetUrl(sessionname), USER_CREATE_URI)

        payload = GET_USER_CREATE_BODY(aUser,password,email,roles,description,firstname,lastname)
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'X-Authorization': DataUtils.GetAuthToken(sessionname)
        }

        response = requests.request(USER_CREATE_REQ_TYPE, URL, data=payload, headers=headers)
        isInError = UsersResponses.Process_Create_Response(response)


def setlogin(sessionname,username,loginuser,loginpassword):
    AllUsernames = ConvertUsernameToList(username)

    for aUser in AllUsernames:

        URL = urllib.parse.urljoin(DataUtils.GetUrl(sessionname), USER_SETLOGIN_URI)
        payload = GET_USER_SET_LOGIN_BODY(aUser,loginuser,loginpassword)
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'X-Authorization': DataUtils.GetAuthToken(sessionname)
        }
        #print(payload)
        response = requests.request(USER_SETLOGIN_REQ_TYPE, URL, data=payload, headers=headers)
        isInError = UsersResponses.Process_Set_Login_Response(response)
