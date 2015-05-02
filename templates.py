import champion

def free_champion_rotation(champions : list) :
	return ('<div style="text-align: center;font-size:145%;font-weight:bold;'
			'margin: .9em 0 .3em 0; color:#70b8ff">Rotación de Campeones</div>\n'
			'<div class="ability_details" style="align:center;width:100%; '
			'border-bottom: 2px solid #082848; margin: 0 0 1em 0; padding: 0 0 0 0; '
			'position:relative; z-index: 100;"></div>\n'
			'{{Champion Rotation|' + '|'.join(champions) + '}}\n'
			'{{clear}}\n'
			'<noinclude>{{documentation}}\n'
			'[[Category:Plantillas|{{PAGENAME}}]]</noinclude>')

def data_champion(champion : Champion) :
	template_text = str('{{{{{1<noinclude>|show data</noinclude>}}}|'+champion.disp_name+'|{{{2|}}}|{{{3|}}}|{{{4|}}}|{{{5|}}}|'
						'disp_name='+champion.disp_name+'|\n'
						'ms='+champion.ms+'|\n'
						'range='+champion.range+'|\n'
						'attack_delay='+champion.attack_delay+'|\n'
						'as_base='+champion.as_base+'|\n'
						'dam_base='+champion.dam_base+'|\n'
						'arm_base='+champion.arm_base+'|\n'
						'mr_base='+champion.mr_base+'|\n'
						'hp_base='+champion.hp_base+'|\n'
						'mp_base='+champion.mp_base+'|\n'
						'hp5_base='+champion.hp5_base+'|\n'
						'mp5_base='+champion.mp5_base+'|\n'
						'as_lvl='+champion.as_lvl+'|\n'
						'dam_lvl='+champion.dam_lvl+'|\n'
						'arm_lvl='+champion.arm_lvl+'|\n'
						'mr_lvl='+champion.mr_lvl+'|\n'
						'hp_lvl='+champion.hp_lvl+'|\n'
						'mp_lvl='+champion.mp_lvl+'|\n'
						'hp5_lvl='+champion.hp5_lvl+'|\n'
						'mp5_lvl='+champion.mp5_lvl+'|\n'
						'image='+champion.image+'|\n'
						'title='+champion.title+'|\n'
						'herotype='+champion.herotype+'|\n'
						'alttype='+champion.alttype+'|\n'
						'rangetype='+champion.rangetype+'|\n'
						'date='+champion.date+'|\n'
						'patch='+champion.patch+'|\n'
						'health='+champion.health+'|\n'
						'attack='+champion.attack+'|\n'
						'spells='+champion.spells+'|\n'
						'difficulty='+champion.difficulty+'|\n'
						'ip='+champion.ip+'|\n'
						'rp='+champion.rp+'|\n')

	# Add passive name's translation
	template_text.append(champion.passive.name['la']+'='+champion.passive.name['na']+'|\n')
	# Check if we have to add EUW version too
	if champion.passive.name['la'] != champion.passive.name['eu']:
		template_text.append(champion.passive.name['eu']+'='+champion.passive.name['na']+'|\n')

	# Add spell names' translations
	for i in champion._spells:
		template_text.append(champion._spells[i].name['la']+'='+champion._spells[i].name['na']+'|\n')
		# Check if we have to add EUW version too
		if champion._spells[i].name['la'] != champion._spells[i].name['eu']:
			template_text.append(champion._spells[i].name['eu']+'='+champion._spells[i].name['na']+'|\n')

	template_text.append('}}')

	return template_text
	