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

def data_champion(champion) :
	return ('{{{{{1<noinclude>|show data</noinclude>}}}|'+disp_name+'|{{{2|}}}|{{{3|}}}|{{{4|}}}|{{{5|}}}|'
			'disp_name='+disp_name+'|'
			'ms='+ms+'|'
			'range='+range+'|'
			'attack_delay='+attack_delay+'|'
			'as_base='+as_base+'|'
			'dam_base='+dam_base+'|'
			'arm_base='+arm_base+'|'
			'mr_base='+mr_base+'|'
			'hp_base='+hp_base+'|'
			'mp_base='+mp_base+'|'
			'hp5_base='+hp5_base+'|'
			'mp5_base='+mp5_base+'|'
			'as_lvl='+as_lvl+'|'
			'dam_lvl='+dam_lvl+'|'
			'arm_lvl='+arm_lvl+'|'
			'mr_lvl='+mr_lvl+'|'
			'hp_lvl='+hp_lvl+'|'
			'mp_lvl='+mp_lvl+'|'
			'hp5_lvl='+hp5_lvl+'|'
			'mp5_lvl='+mp5_lvl+'|'
			'image='+image+'|'
			'title='+title+'|'
			'herotype='+herotype+'|'
			'alttype='+alttype+'|'
			'rangetype='+rangetype+'|'
			'date='+date+'|'
			'patch='+patch+'|'
			'health='+health+'|'
			'attack='+attack+'|'
			'spells='+spells+'|'
			'difficulty='+difficulty+'|'
			'ip='+ip+'|'
			'rp='+rp+'|'
			'}}'
			)