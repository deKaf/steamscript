import os
import imp

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
		url = ('https://steamcommunity.com/id/{0}/').format(profileName)
		return self.fromURL(url)

	def fromURL( self, url ):
		return steam.steamid.steam64_from_url(url)

	def fromID( self, id ):
		return id

############

class getProfileInfo():
	
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

getSteamID = getSteamID()
userID = getSteamID.fromName('kaf')

getProfileInfo = getProfileInfo(userID)



####getting owned games list info
# for games in getProfileInfo.getOwnedGames():
# 	print (games['name'].encode('utf-8')), games['playtime_forever']

### getting recently played games
for games in getProfileInfo.getRecentlyPlayedGames(5):
	print (games['name'].encode('utf-8'))


#### getting friends info
# friends =  getProfileInfo.friends()
# for friend in friends:
# 	friendID = friend['steamid']
# 	friend = api.ISteamUser.GetPlayerSummaries(steamids = friendID)
# 	friend = friend['response']['players'][0]

# 	print friend['personaname'], friend['steamid']

	
#####
