def plant_pumpkins():
    # Get the size of the farm
    size = get_world_size()

    # Ensure we have enough seeds
    # for i in range(size * size):
    #     trade(Items.Pumpkin_Seed)

    # Plant pumpkins on each tile
    for i in range(size):
        for j in range(size):
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Pumpkin)
            if j < size - 1:
                move(North)  # Move north except after the last column
        if i < size - 1:
            # Move to the next column
            move(East)
            for k in range(size):
                move(South)  # Move back to the starting row
while True:
    plant_pumpkins()