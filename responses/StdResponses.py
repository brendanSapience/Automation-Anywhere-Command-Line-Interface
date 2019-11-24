import requests
import json
import sys
import os

def ProcessBool(myBool):
    if(str(type(myBool)) == "<class 'str'>"):
        if(myBool in ['True','true','t','yes']):
            return True
        if(myBool in ['False','false','f','no']):
            return False
    else:
        return myBool

def ProcessStdResponse(res,CsvOutput):
    CsvOutput = ProcessBool(CsvOutput)

    if(res.status_code >= 400):
        print("Error Code: "+str(res.status_code))
        try:
            result = json.loads(res.text)
            if result['message']:
                print("Error Message: "+result['details'])
                return True,None
        except:
            return True,None

        return True,None

    else:
        try:
            return False,CsvOutput
        except:
            print("Unknown Error.")
            return True,None
