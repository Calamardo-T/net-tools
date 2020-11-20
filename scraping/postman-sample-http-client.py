import http.client
import mimetypes
conn = http.client.HTTPSConnection("https://198.18.1.199/web_api")
payload = "{\r\n  \"limit\" : 50,\r\n  \"offset\" : 0,\r\n  \"details-level\" : \"full\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'X-chkp-sid': 'TzM_5O8pE7gLoyKxqi1zBiIU6bjlhzVD3E4L4yOnD9Y'
}
conn.request("POST", "/show-packages", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))