import uvage

camera = uvage.Camera(800, 600)

background_image = uvage.from_image(389, 260, 'bg1012.png')
background_image.scale_by(0.9)

wizard_images = uvage.load_sprite_sheet('wizwalk2.png', 1, 6)
wizard = uvage.from_image(590, 402, wizard_images[-1])
walking_frame = 0
wizard_right = False
attacking_frame = 0

wizard2_images = uvage.load_sprite_sheet('wizwalk3.png', 1, 7)
wizard2 = uvage.from_image(200, 402, wizard2_images[-1])
walking_frame2 = 0
wizard2_right = True
attacking2_frame = 0

wizard2_healthbar = uvage.from_color(200, 500, "light grey", 200, 20)
wizard2_healthgone = uvage.from_color(200, 500, "black", 194, 14)
wizard2_health = uvage.from_color(200, 500, "#157741", 194, 14)

wizard_healthbar = uvage.from_color(588, 500, "light grey", 200, 20)
wizard_healthgone = uvage.from_color(588, 500, "black", 194, 14)
wizard_health = uvage.from_color(588, 500, "#157741", 194, 14)

plat = uvage.from_color(400, 640, '#1D0F20', 1000, 350)

hider1 = uvage.from_color(0, 640, "#1D0F20", 200, 350)
hider2 = uvage.from_color(800, 640, "#1D0F20", 200, 350)

p1_drawing = uvage.from_image(87,500,'p1.png')
p1_drawing.scale_by(0.15)

p2_drawing = uvage.from_image(705,500,'p2.png')
p2_drawing.scale_by(0.15)

statue1_drawing = uvage.from_image(700,364,'statue1hd.png')
statue1_drawing.scale_by(0.5)

statue2_drawing = uvage.from_image(95,350,'statue2.png')
statue2_drawing.scale_by(0.48)

jack_attack = uvage.load_sprite_sheet('jackattackflip.png', 1, 4)
wizard2_attack = uvage.load_sprite_sheet('wizard2attack.png', 1, 10)

health_affected = False
health2_affected = False

def move_wizard():
    global walking_frame
    global wizard_right
    global health_affected
    global attacking_frame
    is_walking = False
    is_attacking = False

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
        if walking_frame >= 6:
            walking_frame = 0
        wizard.image = wizard_images[int(walking_frame)]
        camera.draw(wizard)
        print(walking_frame)

    elif uvage.is_pressing('keypad 0'):
        is_attacking = True

    if is_attacking:
        attacking_frame += 1
        if attacking_frame >= 3:
            attacking_frame = 0
        wizard.image = jack_attack[int(attacking_frame)]
        if wizard.touches(wizard2, -70, 10) and not health_affected:
            health_affected = True
            wizard2_health.x -= 2
    else:
        health_affected = False
        wizard.image = wizard_images[-1]
        is_walking = False
    camera.draw(wizard)


def move_wizard2():
    global walking_frame2
    global wizard2_right
    global health2_affected
    global attacking2_frame
    is_walking = False
    is_attacking = False
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
        camera.draw(wizard2)
    elif uvage.is_pressing('space'):
        is_attacking = True
    if is_attacking:
        attacking2_frame += 1
        if attacking2_frame >= 10:
            attacking2_frame = 0
        wizard2.image = wizard2_attack[int(attacking2_frame)]
        if wizard2.touches(wizard, -70, 10) and not health2_affected:
            health2_affected = True
            wizard_health.x += 2
    else:
        health2_affected = False
        wizard2.image = wizard2_images[-1]
    camera.draw(wizard2)

def tick():
    camera.clear('black')
    camera.draw(background_image)
    camera.draw(statue1_drawing)
    camera.draw(statue2_drawing)
    camera.draw(plat)
    camera.draw(wizard2_healthbar)
    camera.draw(wizard2_healthgone)
    camera.draw(wizard2_health)
    camera.draw(wizard_healthbar)
    camera.draw(wizard_healthgone)
    camera.draw(wizard_health)
    camera.draw(hider1)
    camera.draw(hider2)
    camera.draw(p2_drawing)
    camera.draw(p1_drawing)
    move_wizard()
    move_wizard2()
    camera.display()

uvage.timer_loop(30, tick)