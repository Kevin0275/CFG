# Half Carrot and half for hay and bush
clear()
while True:
	for i in range(get_world_size()/2):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)
				move(North)
			else:
				move(North)
		move(East)
	for j in range(get_world_size()/2):
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(North)
			else:
				move(North)
		move(East)