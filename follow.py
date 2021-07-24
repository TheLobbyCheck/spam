import requests
import random
R = '\033[1;36m'
G = "\033[1;32m"
Y = "\033[1;33m"
print(R+'''
              رشق متابعين انستا 

         _  _ _    _     _   _  _
         `||` `||``||` [ __ ]  [  ][  ][  ]
          ||   ||  ||       ]  [  ][  ][  ]
          ||   ||  ||     __]  [ _][ _][ _]   
          
          Telegram : TTT9000 💜
          by : سوالف انستا كلشي بلاش 

----------------------------------------------------------
''')
def Folowers():
    username = input('[+]Username :')
    print("")
    list = 'qwertyuiopasdfghjklzxcvbnm'
    eml = ''.join(random.choice(list) for i in range(5))
    email = f'{eml}@gmail.com'
    url = 'https://core.poprey.com/api/create_test_order.php'
    headers = {
    'accept': 'application/json, text/plain, /',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-length': '105',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://poprey.com',
    'referer': 'https://poprey.com/',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'x-auth-token': 'null',
    'x-target-lang': 'en'
    }
    data = {
    'service': 'Followers',
    'email': email,
    'username': username,
    'system': 'Instagram',
    'plan': '10',
    'tariff': 'normal',
    'csrf':''
    }
    req = requests.post(url,headers=headers,data=data)
    print(G+'Request sent 💜. ')
    print(Y+"[!]In case you don't receive your followers, try it at a later time")
Folowers()