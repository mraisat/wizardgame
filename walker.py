import uvage
camera = uvage.Camera(800,600)


walker_images = uvage.load_sprite_sheet('walk_stand.png',1,6)
walker = uvage.from_image(100,400,walker_images[-1])
walking_frame = 0
walker_right = True

def move_walker():
	global walking_frame
	global walker_right
	is_walking = False
	if uvage.is_pressing('left arrow'):
		if walker_right:
			walker.flip()
			walker_right = False
		walker.x -= 2
		is_walking = True
	elif uvage.is_pressing('right arrow'):
		if not walker_right:
			walker.flip()
			walker_right = True
		walker.x += 2
		is_walking = True
	if is_walking:
		walking_frame += 0.3
		if walking_frame >= 5:
			walking_frame = 0
		walker.image = walker_images[int(walking_frame)] # 0,1,2,3,4,0,1,2,3,4,0,1
	else:
		walker.image = walker_images[-1]
	camera.draw(walker)

def tick():
	camera.clear('light blue')
	move_walker()
	camera.display()

uvage.timer_loop(30,tick)