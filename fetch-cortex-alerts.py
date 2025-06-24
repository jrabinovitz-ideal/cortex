import http.client

conn = http.client.HTTPSConnection("https://api-delco.xdr.us.paloaltonetworks.com")

payload = "{\"request_data\":{\"filters\":[{\"field\":\"severity\",\"operator\":\"in\",\"value\":[\"low\",\"medium\",\"high\"]}]}}"

headers = {
    'Authorization': "SdjQ862Lq7uj8LMDLeqRVYkgpZa10fmriN3xJ405IncyKoVbwz3P2AWj07wdhXSDamOcHAVrjFvOBGqGYdljH38UhljZnQIFfKwVRRo2JYhuipYmMo3oIRAp2fVWfN6o",
    'x-xdr-auth-id': "2",
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

