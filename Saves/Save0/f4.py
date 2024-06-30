def till_soil():
    world_size = get_world_size()
    while True:
        for i in range(world_size):
            if get_ground_type() == Grounds.Turf:
                till()
            move(North)
        move(East)
till_soil()