def judge():
	if can_harvest():
			harvest()
			plant(Entities.Bush)
	else:
			continue
def forward():
	for i in range(get_world_size()-1):
		judge()
		move(North)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
def backward():
	for j in range(get_world_size()-1):
		judge()
		move(South)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
clear()
while True:
	forward()
	move(East)
	backward()
	move(East)
	forward()
	move(West)
	backward()
	move(West)