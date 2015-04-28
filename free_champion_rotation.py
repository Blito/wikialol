import templates
import riotwatcher.riotwatcher as RiotAPI
import pywikibot

with open('key.txt') as f:
    key = f.read()

print ("Validando usuario en RiotAPI...")
riotApi = RiotAPI.RiotWatcher(key)

print ("Calculando rotación de campeones...")
# Get free champion rotation
free_champ_rotation = riotApi.get_all_champions(None, True)
champions = riotApi.static_get_champion_list(data_by_id=True)
free_champions = []
for champ in free_champ_rotation['champions']:
   free_champions.append(champions['data'][str(champ['id'])]['name'])

new_wikia_code = templates.free_champion_rotation(free_champions)

print ("Subiendo cambios a es.leagueoflegends.wikia.com/wiki/Plantilla:Rotación_de_Campeones...")
# Get wiki content from Rotacion de Campeones page
site = pywikibot.Site()
page = pywikibot.Page(site, u"Plantilla:Rotación_de_Campeones")
page.text = new_wikia_code
page.save(u"Página editada automáticamente por [[Usuario:BleetohBot|BleetohBot]]!")

print ("Listo!")