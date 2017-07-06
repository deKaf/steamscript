from steam import WebAPI
import steam

import os

#### get key from file ####

def getKey(path):
	key = ''
	if os.path.isfile(path):
		lines = [line.rstrip('\n') for line in open(path)]
		if len(lines) > 1 :
			raise Exception ("One line for key only")
		else:
			return lines[0]	
	else:
		raise Exception("Not valid file path")

apiKey = getKey( "C:\\personal\\steam.key" )
api = WebAPI( apiKey )

##########

# set profileURL
profileURL = "https://steamcommunity.com/id/kaf/"
myProfileID = steam.steamid.steam64_from_url(profileURL)

### get user profile info!
#works!
myInfo = api.ISteamUser.GetPlayerSummaries(steamids = myProfileID)
profileDict = myInfo['response']['players']

# for x in profileDict: 
# 	for k,v in x.items():
# 		print k,v
	

#### friends stuff ######

myFriendsInfo =  api.ISteamUser.GetFriendList(steamid= myProfileID)

for key,value in myFriendsInfo.items():
	for x in value.items(): 
		myFriendsInfo = x[1]

#myFriendsInfo just returns steamid, friends_since and relationship

for item in myFriendsInfo:	
	friendProfile = api.ISteamUser.GetPlayerSummaries(steamids = item['steamid'])
	friendProfile = friendProfile['response']['players'][0]
		print friendProfile['personaname'], friendProfile['steamid']

	
