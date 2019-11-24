import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import IQBotGroupTransformers
import StdResponses

def Process_List_Response(res,CsvOutput):
    isError,isCsvOutput = StdResponses.ProcessStdResponse(res,CsvOutput)
    if(isError):
        exit(1)
    else:
        result = json.loads(res.text)
        if isCsvOutput:
            print(IQBotGroupTransformers.GetGroupListAsCsv(result))
            exit(0)
        else:
            print(result)
            exit(0)
