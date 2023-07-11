import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

url = "https://testorchestrate.atlassian.net/rest/api/2/search"

auth = HTTPBasicAuth("jam414@yahoo.com", "ATATT3xFfGF0VxTQJECT1_4Lk4Y8CRqiDhf6o0AyyTaya1CipVHAgK-C6-NAMUszaSgk3UcV24qouHLFRWB5QYrcddkN6r0ElGxdZzuGfIvXKvCYDORETW8ACT7AfwVRyblOczSff32izhgvv_qr7gMqRey-yZOCR_9ApEGO3Vnd3bWAveYxYTw=8DB1D440")

headers = { "Accept": "application/json"}

query = { 'jql': 'project ="Equity Market - Defects"'}

response =requests.request(  "GET",  url,  headers=headers,  auth=auth,  params=query)

projectIssues = json.dumps(json.loads(response.text), sort_keys=True,indent=6,separators=(",", ": "))
print(projectIssues)

dictProjectIssues = json.loads(projectIssues)
listAllIssues = []
keyIssue, keySummary, keyReporter = "", "", ""

def iterateDictIssues(oIssues, listInner):

    for key, values in oIssues.items():
        if(key == "fields"):
            fieldsDict = dict(values)
            iterateDictIssues(fieldsDict, listInner)
        elif (key == "reporter"):
            reporterDict = dict(values)
            iterateDictIssues(reporterDict, listInner)
        elif(key == 'key'):
            keyIssue = values
            listInner.append(keyIssue)
        elif(key == 'summary'):
            keySummary = values
            listInner.append(keySummary)
        elif(key == "displayName"):
                    keyReporter = values
                    listInner.append(keyReporter)

        for key, value in dictProjectIssues.items():
    
            if(key == "issues"):
                totalIssues = len(value)
        
            
                for eachIssue in range(totalIssues):
                    listInner = []  
                    iterateDictIssues(value[eachIssue], listInner)  
                    listAllIssues.append(listInner)