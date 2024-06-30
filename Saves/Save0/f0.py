def harvest_world():
    world_size = get_world_size()
    for x in range(world_size):
        for y in range(world_size):
            harvest()
            move(North)
        move(East)
harvest_world()