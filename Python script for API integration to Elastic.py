
import requests
import json
from requests.auth import HTTPBasicAuth
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'https://observability-deployment-fc8291.es.eastus2.azure.elastic-cloud.com', 'port': 9243}],http_auth=('elastic','J72xzdirrp2sKIKT7bGwM3Co'))

def iterateAllKeys(e):
    for key in e.iterkeys():
        print (key)
        for child in key.get(key):
            iterateAllKeys(child)

def iter_dict(dic):
    for key in dic:
        print(key)
        if isinstance(dic[key], dict):
            iter_dict(dic[key])


username = "krapanshu.sinha@genpact.com"
token ="bla1oz1brj7kndrkexgdon408a627yu9"
test_id="52386"
roundid="1621245900"
agent_id="30b04cf2-b67b-48c4-b0b8-80cff24d4ce7"
#https://api.thousandeyes.com/v6/endpoint-data/tests/net/path-vis/52333/16ea6cf1-ca62-4fce-bb6c-1771bccc93e5/1620887400.json?headers=1&certificates=1"

url = "https://api.thousandeyes.com/v6/endpoint-data/tests/net/path-vis/52386/30b04cf2-b67b-48c4-b0b8-80cff24d4ce7/1621245900.json?headers=1&certificates=1"

payload = {}
headers = {
  'Authorization: Basic a3JhcGFuc2h1LnNpbmhhQGdlbnBhY3QuY29tOmJsYTFvejFicmo3a25kcmtleGdkb240MDhhNjI3eXU5='
}

#response = requests.request("GET", url, headers=headers, data = payload)

response = requests.request("GET", url, verify=False, auth=HTTPBasicAuth('krapanshu.sinha@genpact.com', 'bla1oz1brj7kndrkexgdon408a627yu9'))
result = json.loads(str(response.text))
#print(result)
hops = result['endpointNet']['pathVis'][int(0)]['routes'][int(0)]['hops']

i = 1
j = 0

while i < len(hops): 
	es.index(index='te', doc_type='hop', id=i,body=hops[j])
	i=i+1
	j=j+1

#iterateAllKeys(result)
#iter_dict(result)
#response = requests.request("GET", url, headers=headers, data = payload)
#print(str(response.text))




#print(response.text.encode('utf8'))
