def plant_trees():
    world_size = get_world_size()
    for x in range(world_size):
        for y in range(world_size):
            plant(Entities.Tree)
            if y < world_size - 1:  # Don't move north after the last row
                move(North)
        if x < world_size - 1:  # Don't move east after the last column
            move(East)
            for i in range(world_size - 1):  # Move back south to the first row
                move(South)
plant_trees()