import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import ActivitiesTransformers
import StdResponses

def Process_list_Response(res,CsvOutput):
    isError,isCsvOutput = StdResponses.ProcessStdResponse(res,CsvOutput)
    if(isError):
        exit(1)
    else:
        result = json.loads(res.text)
        if isCsvOutput:
            print(ActivitiesTransformers.GetListAsCsv(result))
            exit(0)
        else:
            print(result)
            exit(0)
