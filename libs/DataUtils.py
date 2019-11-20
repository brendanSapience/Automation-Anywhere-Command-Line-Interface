import os

TOKENFILE = "./data/.token"
URLFILE = "./data/.url"

def StoreUrl(url):
    os.remove(URLFILE)
    text_file = open(URLFILE, "w+")
    text_file.write(url)
    text_file.close()

def GetUrl():

    text_file = open(URLFILE, "r")
    url = text_file.read()
    text_file.close()
    return url

def StoreAuthToken(token):
    os.remove(TOKENFILE)
    text_file = open(TOKENFILE, "w+")
    text_file.write(token)
    text_file.close()

def GetAuthToken():

    text_file = open(TOKENFILE, "r")
    token = text_file.read()
    text_file.close()
    return token
