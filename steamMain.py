import os
import imp
import operator 
from collections import OrderedDict

try:
	import steam
	from steam import WebAPI
except:
	print ("Steam module not found, attempting to import")




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


##########

class getSteamID():
	""""Class to retrieve steam64 ID via name, URL"""
	def fromName( self, profileName ):
		
		profileName = api.call( 'ISteamUser.ResolveVanityURL', vanityurl = profileName )
		return profileName['response']['steamid']

	def fromURL( self, url ):
		
		strippedURL = filter(None,(url).split("/"))[-1]
		return self.fromName(strippedURL)

	def fromID( self, id ):
		return id

############

class GetProfileInfo():

	"""Fetch user profile info"""
	def __init__(self, userID):

		self.userID = userID
		self.friendIDs = []
		self.recentlyPlayedGames = {}
		self.ownedGames = {}

		self.rawData = api.ISteamUser.GetPlayerSummaries(steamids = self.userID)


	def rawProfile( self ):

		'''Get profile info cleanly from rawData'''
		self.rawProfile = self.rawData['response']['players'][0]
	 	return self.rawProfile
		
	
	def friends( self ):
		friendRaw = api.ISteamUser.GetFriendList(steamid= self.userID)
		for k,v in friendRaw.items():
			for x in v.items(): friendRaw = x[1]
		
		return friendRaw

	def getOwnedGames( self ):

		self.ownedGames = api.IPlayerService.GetOwnedGames(
        	steamid=self.userID, include_appinfo=True, include_played_free_games=True, appids_filter={''})['response']['games']
		return self.ownedGames

	def getRecentlyPlayedGames( self, numGames ):
		
		self.recentlyPlayedGames = api.IPlayerService.GetRecentlyPlayedGames(
	        steamid=self.userID, count=numGames)['response']['games']

		return self.recentlyPlayedGames



##############
api = WebAPI( apiKey )
##############

#### Testing ####

getSteamID = getSteamID()
corvoID = getSteamID.fromURL('http://steamcommunity.com/id/kohan/')
corvoProfileInfo = GetProfileInfo(corvoID)

### getting recently played games
print ("Corvo's most recently played games")
for games in corvoProfileInfo.getRecentlyPlayedGames(5):
	print (games['name'].encode('utf-8'))

tempDict = corvoProfileInfo.getOwnedGames()
newDict = {}
for game in tempDict:
	newDict[game['name'].encode('utf-8')] = game['playtime_forever']

for k,v in sorted(newDict.items(), key=operator.itemgetter(1), reverse=True):
	print k,v

print ('Corvo owns {0} games').format (len(tempDict))


#### getting friends info
# friends =  getProfileInfo.friends()
# for friend in friends:
# 	friendID = friend['steamid']
# 	friend = api.ISteamUser.GetPlayerSummaries(steamids = friendID)
# 	friend = friend['response']['players'][0]

# 	print friend['personaname'], friend['steamid']

	
#####
