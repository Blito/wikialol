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