# steamscript
Python project to read data from Steam

This python script provides a simpler and cleaner way to fetch and retrieve profile information from Steam's Web API and serves as a frontend for another module that can be found here: https://github.com/ValvePython/steam


The end goal is to do a bunch of things that will output to a dynamic website, such as:

  1. Accept a given steam profile URL
  2. List friends associated with this account
  3. List all recently played games of profile and friends
  4. Compare more played games amongs profiles and suggest new games based on hours played / frequency
  

Usage Information for the Python script:

```python
import steam
from steam import WebAPI

api = WebAPI( apiKey )`
[apiKey needs to be a string that points to an ASCII file with your Steam API Key]


`
getSteamID = getSteamID()
profileID = getSteamID.fromURL('http://steamcommunity.com/id/kaf/')
profileInfo = GetProfileInfo(profileID)

friends =  profileInfo.friends()
for friend in friends:
	friendID = friend['steamid']
	friend = api.ISteamUser.GetPlayerSummaries(steamids = friendID)
	friend = friend['response']['players'][0]

	print friend['personaname'], friend['steamid']
```