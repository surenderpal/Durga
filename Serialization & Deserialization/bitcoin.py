import requests
response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
binfo=response.json()
# print(type(binfo))
# print(binfo)
print('bitcoin price as on:',binfo['time']['updateduk'])
# print(binfo['chartName'])i
print('1 Bitcoin price is $',binfo['bpi']['USD']['rate'])
