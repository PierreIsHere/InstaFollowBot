import json
import os.path
from Login import api
from time import sleep


def getFollowers(user_id,rank_token):
    followers = []
    results = api.user_followers(user_id, rank_token)
    followers.extend(results.get('users', []))

    next_max_id = results.get('next_max_id')
    while next_max_id:
        results = api.user_followers(user_id, rank_token, max_id=next_max_id)
        followers.extend(results.get('users', []))
        if len(followers) >= 21:
            break
        next_max_id = results.get('next_max_id')

    followers.sort(key=lambda x: x['pk'])
    followers = json.dumps([u['pk'] for u in followers])
    followers = followers.replace("[", "")
    followers = followers.replace("]", "")
    followers = followers.split(", ")
    return followers[:21]


try:
    from instagram_private_api import (
        Client, __version__ as client_version)

except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from instagram_private_api import (
        Client, __version__ as client_version)

rank_token = Client.generate_uuid()
userId = '6042899418'
toFollow = getFollowers(userId, rank_token)
print(toFollow)
tempFollows = []
x = 0
while True:
    for user_id in toFollow:
        sleep(1)
        x = x+1
        print(str(x)+"-------"+user_id)
        api.friendships_create(user_id)
        temp = getFollowers(user_id, rank_token)
        if "" not in temp:
            tempFollows = tempFollows + temp
        print(tempFollows)
    toFollow = tempFollows
    tempFollows = []
