import http.client

conn = http.client.HTTPSConnection("api-idealintegrationsxdr.xdr.us.paloaltonetworks.com")

payload = "{\"request_data\":{\"filters\":[{\"field\":\"severity\",\"operator\":\"in\",\"value\":[\"low\",\"medium\",\"high\"]}]}}"

headers = {
    'Authorization': "NGXu6viwq12tsuJED8PYaw4cJmpD0tajIk87h0UT5WZh9fxbHRd85oU2mE6picTXfeV4l8WzgQgDFmrGfKFOmFSpxwKFGeyppxUAyPwXCHk4W2NROtsK2UBeX8qRUQuL",
    'x-xdr-auth-id': "3",
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

