import uvage

camera = uvage.Camera(800, 600)

background_image = uvage.from_image(389, 260, 'bg1012.png')
background_image.scale_by(0.9)

wizard_images = uvage.load_sprite_sheet('wizwalk2.png', 1, 6)
wizard = uvage.from_image(590, 402, wizard_images[-1])
walking_frame = 0
wizard_right = False

wizard2_images = uvage.load_sprite_sheet('wizwalk3.png', 1, 7)
wizard2 = uvage.from_image(200, 402, wizard2_images[-1])
walking_frame2 = 0
wizard2_right = True
wizard2_healthbar = uvage.from_color(200, 500, "light grey", 200, 20)
wizard2_healthgone = uvage.from_color(200, 500, "black", 194, 14)
wizard2_health = uvage.from_color(200, 500, "#157741", 194, 14)

plat = uvage.from_color(400, 640, '#1D0F20', 1000, 350)
hider = uvage.from_color(0, 640, "#1D0F20", 200, 350)
p1_drawing = uvage.from_image(87,500,'p1.png')
p1_drawing.scale_by(0.15)
statue1_drawing = uvage.from_image(700,350,'statue1.png')
statue1_drawing.scale_by(0.5)

jack_attack = uvage.load_sprite_sheet('jackattackflip.png', 1, 4)

health_affected = False

def move_wizard():
    global walking_frame
    global wizard_right
    global health_affected
    is_walking = False

    if uvage.is_pressing('left arrow'):
        if wizard_right:
            wizard.flip()
            wizard_right = False
        wizard.x -= 5
        is_walking = True

    elif uvage.is_pressing('right arrow'):
        if not wizard_right:
            wizard.flip()
            wizard_right = True
        wizard.x += 5
        is_walking = True
    if is_walking:
        walking_frame += 0.3
        if walking_frame >= 5:
            walking_frame = 0
        wizard.image = wizard_images[int(walking_frame)]
    elif uvage.is_pressing('space'):
        for i in range(3, 0, -1):
            wizard.image = jack_attack[i]
        camera.draw(wizard)
        if wizard.touches(wizard2) and not health_affected:
            health_affected = True
            wizard2_health.x -= 5
    else:
        health_affected = False
        wizard.image = wizard_images[-1]
    camera.draw(wizard)

def move_wizard2():
    global walking_frame2
    global wizard2_right
    is_walking = False
    if uvage.is_pressing('a'):
        if wizard2_right:
            wizard2.flip()
            wizard2_right = False
        wizard2.x -= 5
        is_walking = True
    elif uvage.is_pressing('d'):
        if not wizard2_right:
            wizard2.flip()
            wizard2_right = True
        wizard2.x += 5
        is_walking = True
    if is_walking:
        walking_frame2 += 0.3
        if walking_frame2 >= 6:
            walking_frame2 = 0
        wizard2.image = wizard2_images[int(walking_frame2)]
    else:
        wizard2.image = wizard2_images[-1]
    camera.draw(wizard2)

def tick():
    camera.clear('black')
    camera.draw(background_image)
    camera.draw(statue1_drawing)
    camera.draw(plat)
    camera.draw(wizard2_healthbar)
    camera.draw(wizard2_healthgone)
    camera.draw(wizard2_health)
    camera.draw(hider)
    camera.draw(p1_drawing)
    move_wizard()
    move_wizard2()
    camera.display()

uvage.timer_loop(30, tick)