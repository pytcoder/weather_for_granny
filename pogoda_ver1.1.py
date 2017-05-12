import requests
r = requests.get('http://api.openweathermap.org/data/2.5/find?q=Sochi&type=like&APPID=9135c77df6fd7abd0e8c4b30c031854f')
result = r.json() if r.text else dict()
temp = int(result['list'][0]['main']['temp']) - 273.15
humidity = int(result['list'][0]['main']['humidity'])
wind = (result['list'][0]['wind']['speed'])
f = 'https://sms.ru/sms/send?api_id=1DBD9D25-3FCC-4446-E114-C402C107D795&to=79384000957&msg='+'В+сочи:+'+str(round(temp))+'+град.+Влажность:+'+str(humidity)+'%'+'+Ветер:+'+str(wind)+'+м/с'+'&json=1'
requests.get(f)

