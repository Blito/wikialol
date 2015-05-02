import riotwatcher.riotwatcher as RiotAPI
from champion import Champion

with open('key.txt') as f:
    key = f.read()

riotApi = RiotAPI.RiotWatcher(key)

static_champ_list_la = riotApi.static_get_champion_list(locale='es_MX', champ_data='all')
# static_champ_list_na = riotApi.static_get_champion_list(locale='en_US', champ_data='all')
# static_champ_list_eu = riotApi.static_get_champion_list(locale='es_ES', champ_data='all')
champions_data_la = static_champ_list_la['data']
# champions_data_na = static_champ_list_na['data']
# champions_data_eu = static_champ_list_eu['data']

champions = []
for champ in champions_data_la:
    champ_data_la = champions_data_la[champ]
    # champ_data_na = champions_data_na[champ]
    # champ_data_eu = champions_data_eu[champ]
    champion = Champion(champ_data_la)
    champions.append(champion)

for champion in champions:
    print(champion.image)
