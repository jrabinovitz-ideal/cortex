import http.client

conn = http.client.HTTPSConnection("")

payload = "{\"request_data\":{\"filters\":[{\"field\":\"severity\",\"operator\":\"in\",\"value\":[\"low\",\"medium\",\"high\"]}]}}"

headers = {
    'Authorization': "",
    'x-xdr-auth-id': "",
    'Accept-Encoding': "yes",
    'content-type': "application/json"
    }

conn.request("POST", "/public_api/v2/alerts/get_alerts_multi_events", payload,headers)

res = conn.getresponse()
data = res.read()
data_pretty = data.decode("utf-8")
files = open('output.json','a')
files.write(data_pretty)
files.close()

