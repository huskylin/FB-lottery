#-*- coding:big5 -*- 

#   change CMD to UTF-8
#   chcp 65001

import requests
import json
import random

#  Facebook API
url = 'https://graph.facebook.com/v2.12/'
FB_token = 'GET_FROM_Graph_API_Explorer'
fileds = '2104358166245473/comments?filter=stream&limit=1000&order=chronological'

response = requests.get(url + fileds + FB_token).json()

#   get username form response data
result = list()
for comments in response['data']:
    result.append({
        'name' : comments['from']['name']
    })

#   remove duplicates
seen = set()
new_l = []
for d in result:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)

#   random sort
random.shuffle(new_l)
bingo = new_l[:1]

#   print
print(bingo)