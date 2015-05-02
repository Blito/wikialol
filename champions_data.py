import riotwatcher.riotwatcher as RiotAPI

with open('key,txt') as f:
    key = f.read()

riotApi = RiotAPI.RiotWatcher(key)

static_champ_list = riotApi.static_get_champion_list(champ_data='all')
champions_data = static_champ_list['data']

for champ_data in champions_data:
    champion = Champion(champ_data)
