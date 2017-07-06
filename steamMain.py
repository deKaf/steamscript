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
		self.rawData = api.ISteamUser.GetPlayerSummaries(steamids = userID)

	def rawProfile( self ):

		'''Get profile info cleanly from rawData'''
		self.rawProfile = self.rawData['response']['players'][0]
	 	return self.rawProfile
		
	
	def friends( self ):
		friendRaw = api.ISteamUser.GetFriendList(steamid= self.userID)
		for k,v in friendRaw.items():
			for x in v.items(): friendRaw = x[1]
		
		return friendRaw


##############

api = WebAPI( apiKey )

getSteamID = getSteamID()
userID = getSteamID.fromName('kaf')

getProfileInfo = getProfileInfo(userID)

# print getProfileInfo.rawProfile()
friends =  getProfileInfo.friends()

for friend in friends:

	friendID = friend['steamid']
	friend = api.ISteamUser.GetPlayerSummaries(steamids = friendID)
	friend = friend['response']['players'][0]

	print friend['personaname'], friend['steamid']

	
#####
