import templates
from riotwatcher.riotwatcher import RiotWatcher

with open('key.txt') as f:
    key = f.read()
 
w = RiotWatcher(key)

# Get all champion statistics
#static_champ_list = w.static_get_champion_list(champ_data='stats')
#datos_champions = static_champ_list['data']
#for champ in datos_champions:
#    print(champ + ':')
#    for stat in datos_champions[champ]['stats']:
#        print(stat + ': ' + str(datos_champions[champ]['stats'][stat]))

# Get free champion rotation
free_champ_rotation = w.get_all_champions(None, True)
champions = w.static_get_champion_list(data_by_id=True);
free_champions = []
for champ in free_champ_rotation['champions']:
   free_champions.append(champions['data'][str(champ['id'])]['name'])

# This should match es.leagueoflegends.wikia.com/wiki/Plantilla:Rotación_de_Campeones?action=raw
print(templates.free_champion_rotation(free_champions))