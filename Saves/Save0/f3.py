def plant_carrots():
	world_size = get_world_size()
	while True:
		for i in range(world_size):
			if can_harvest():
				harvest()
				# till()
			else:
				trade(Items.Carrot_Seed)
				plant(Entities.Carrots)
				move(North)
		move(East)
plant_carrots()