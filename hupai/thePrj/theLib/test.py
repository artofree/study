import requests
import time, threading ,datetime

url = 'http://api.yundama.com/api.php?method=upload'
files = {'file': open(r'C:\Users\guo\Desktop\thePrj\51\1.png', 'rb')}
data = {'username': 'silentcraft', 'password': 'inwcwizard', 'codetype': '1004', 'appid': '1', 'appkey': '22cc5376925e9387a23cf797cb9ba745', 'timeout': '30'}
r = requests.post(url, files=files, data=data)
print(r.json()['text'])