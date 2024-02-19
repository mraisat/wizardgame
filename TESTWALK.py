import uvage

camera = uvage.Camera(800, 600)

background_image = uvage.from_image(389, 260, 'bg1012.png')
background_image.scale_by(0.9)

plat = uvage.from_color(400, 640, "black", 1000, 350)

walker_images = uvage.load_sprite_sheet('wizwalk2.png', 1, 6)
walker = uvage.from_image(590, 402, walker_images[-1])
walking_frame = 0
walker_right = False

walker2_images = uvage.load_sprite_sheet('wizwalk3.png', 1, 7)
walker2 = uvage.from_image(200, 402, walker2_images[-1])
walking_frame2 = 0
walker2_right = True

jack_attack = uvage.load_sprite_sheet('jackattack.png', 1, 4)
jack_fight_frames = [uvage.from_image(walker.x, walker.y, frame) for frame in jack_attack]
current_fight_frame = 0
fighting_animation = False


def move_walker():
    global walking_frame
    global walker_right
    is_walking = False

    if fighting_animation:
        walker_right = True
        walker.flip()
        walker.x -= 5
        is_walking = True

        walking_frame += 0.3
        if walking_frame >= 3:
            walking_frame = 0
            walker.image = jack_fight_frames[current_fight_frame]

    if uvage.is_pressing('left arrow'):
        if walker_right:
            walker.flip()
            walker_right = False
        walker.x -= 5
        is_walking = True
    elif uvage.is_pressing('right arrow'):
        if not walker_right:
            walker.flip()
            walker_right = True
        walker.x += 5
        is_walking = True
    if is_walking:
        walking_frame += 0.3
        if walking_frame >= 5:
            walking_frame = 0
        walker.image = walker_images[int(walking_frame)]
    else:
        walker.image = walker_images[-1]
    camera.draw(walker)


def move_walker2(walker, walking_frame, walker_right, keys):
    global walking_frame2
    global walker2_right
    is_walking = False
    if uvage.is_pressing('a'):
        if walker2_right:
            walker2.flip()
            walker2_right = False
        walker2.x -= 5
        is_walking = True
    elif uvage.is_pressing('d'):
        if not walker2_right:
            walker2.flip()
            walker2_right = True
        walker2.x += 5
        is_walking = True
    if is_walking:
        walking_frame2 += 0.3
        if walking_frame2 >= 6:
            walking_frame2 = 0
        walker2.image = walker2_images[int(walking_frame2)]
    else:
        walker2.image = walker2_images[-1]
    camera.draw(walker2)


def jack_fighting():
    global current_fight_frame
    global fighting_animation
    if uvage.is_pressing('space'):
        fighting_animation = True
        current_fight_frame = 0


def tick():
    global fighting_animation
    global current_fight_frame

    camera.clear('black')
    camera.draw(background_image)
    camera.draw(plat)
    move_walker()
    move_walker2(walker2, walking_frame2, walker2_right, {'A': 'A', 'D': 'D'})

    if fighting_animation:
        walker.image = jack_fight_frames[current_fight_frame]
        current_fight_frame += 1
        if current_fight_frame >= len(jack_fight_frames):
            current_fight_frame = 0
            fighting_animation = False

    camera.display()


uvage.timer_loop(30, tick)

