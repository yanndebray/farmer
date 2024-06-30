def plant_only_bush():
	while True:
		for i in range(3):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(North)
		move(East)
plant_only_bush()