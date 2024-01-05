import requests

url = "https://text-you.ru/search.html"

payload=f'do=search&subaction=search&story={message.text}'
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
  'Accept-Language': 'en-GB,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://text-you.ru/search.html',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Origin': 'https://text-you.ru',
  'Connection': 'keep-alive',
  'Cookie': 'PHPSESSID=pbiv2qgcfhuglbdsf1intt5tkd',
  'Upgrade-Insecure-Requests': '1',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'TE': 'trailers'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
data = response