import requests

url = "https://198.18.1.199/web_api/show-packages"

payload = "{\r\n  \"limit\" : 50,\r\n  \"offset\" : 0,\r\n  \"details-level\" : \"full\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'X-chkp-sid': 'TzM_5O8pE7gLoyKxqi1zBiIU6bjlhzVD3E4L4yOnD9Y'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))