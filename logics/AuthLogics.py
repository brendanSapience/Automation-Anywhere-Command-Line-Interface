import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import AuthResponses

AUTH_LOGIN_URI = "/v1/authentication"
AUTH_LOGIN_REQ_TYPE = "POST"

AUTH_TOKEN_URI = "/v1/authentication/token"
AUTH_TOKEN_REQ_TYPE = "POST"

AUTH_LOGOUT_URI = "/v1/authentication/logout"
AUTH_LOGOUT_REQ_TYPE = "POST"

def GET_AUTH_TOKEN_BODY(token):
    b = json.dumps(
        {
            'token': token
        }
    )
    return b

def GET_AUTH_LOGIN_BODY(login, password):
    b = json.dumps(
        {
            'username': login,
            'password':password
        }
    )
    return b

def checktoken(token,sessionname):

    URL = DataUtils.GetUrl(sessionname)+AUTH_TOKEN_URI

    payload = GET_AUTH_TOKEN_BODY(token)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'X-Authorization': DataUtils.GetAuthToken(sessionname)
    }

    response = requests.request(AUTH_TOKEN_REQ_TYPE, URL, data=payload, headers=headers)
    isInError = AuthResponses.Process_Auth_Token_Response(response)

def login(url,login,password,sessionname):

    URL = url+AUTH_LOGIN_URI

    #print(URL)
    payload = GET_AUTH_LOGIN_BODY(login,password)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    response = requests.request(AUTH_LOGIN_REQ_TYPE, URL, data=payload, headers=headers)
    isInError = AuthResponses.Process_Auth_Login_Response(response,url,sessionname)

def logout(sessionname):

    URL = DataUtils.GetUrl(sessionname)+AUTH_LOGOUT_URI
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'X-Authorization': DataUtils.GetAuthToken(sessionname)
    }

    response = requests.request(AUTH_LOGOUT_REQ_TYPE, URL, data=None, headers=headers)
    isInError = AuthResponses.Process_Auth_Logout_Response(response,sessionname)
    if(not isInError):
        DataUtils.DeleteSessionFiles(sessionname)
