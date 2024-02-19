# Name: Mumtaheena Raisa
# Computing ID: wxv3me

# Game Idea Description:

# 2-players will fight each other simultaneously.
# Each player will mostly attack each other to drain the opponent's health.
# First to lose all of their health loses the game.
# Each player will have their own wolf that will attack their opponent and drain their health.

# 3 basic features:

# user input: two players will use the keyboard arrows and WASD keys and other special keys for power ups to fight each other.
# game over: game ends after one player loses all of their health. Game displays the winner at the game over screen.
# graphics/images: it has a background image for a fighting stage, the characters will have images too.

# 4 additional features:

# health bar: characters have a health bar while fighting that decreases every time the opponent hits them.
# enemies: wolves from each side of the players will appear with the press of a key and will drain the health of their opponent.
# two players simultaneously: two players will fight each other simultaneously.
# timer: each players have a timer that counts down until they can release their wolf. It restarts after they use their wolf.
# sprite animations: characters fighting style and wolf running is animated with a spritesheet.

# Controls to use (also displayed in game):
# Player 1: D to move right, A to move left. Space bar to attack. F to bring wolf.
# Player 2: Arrow keys to move left & right. Keypad 0 to attack. Keypad 2 to bring wolf.

# Some limitations to make the attacks harder to carry out:
# Players should be close to their opponent while attacking or else the opponent's health won't be affected.
# Players can't keep holding on their attack buttons to drain health. They have to press the button to initiate each attack.
# Players can't attack while walking. They must stop before they want to attack, making them vulnerable to their opponent.
# To escape the wolf's attack, you have to run further out of the box and come back to fight, but you gotta be quick because the wolf is faster.

import uvage

camera = uvage.Camera(800, 600)

# uploading images and making health bars and platform

background_image = uvage.from_image(389, 260, 'bg1012.png')
background_image.scale_by(0.9)

background_border = uvage.from_image(400, 301, 'border.png')
background_border.scale_by(1.39)

# loading spritesheets

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

# making the health bars

wizard2_healthbar = uvage.from_color(200, 500, "light grey", 200, 20)
wizard2_healthgone = uvage.from_color(200, 500, "black", 194, 14)
wizard2_health = uvage.from_color(200, 500, "#157741", 194, 14)

wizard_healthbar = uvage.from_color(588, 500, "light grey", 200, 20)
wizard_healthgone = uvage.from_color(588, 500, "black", 194, 14)
wizard_health = uvage.from_color(588, 500, "#157741", 194, 14)

# platform and other graphic details

plat = uvage.from_color(400, 640, '#1D0F20', 1000, 350)

name = uvage.from_image(390, 280, 'wolfcast.png')
name.scale_by(1)

tutorial1 = uvage.from_image(190, 630, 'right3.png')
tutorial1.scale_by(0.45)
tutorial2 = uvage.from_image(600, 630, 'right4.png')
tutorial2.scale_by(0.45)
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

jack_attack = uvage.load_sprite_sheet('wizardflameflip.png', 1, 14)
wizard2_attack = uvage.load_sprite_sheet('Light_charge_attack.png', 1, 13)

enemy1_images = uvage.load_sprite_sheet('Hyena_walk_flip_P.png', 1, 6)
enemy1 = uvage.from_image(-50, 444, enemy1_images[-1])
enemy1_frame = 0
enemy_walking = False

health_affected = False
health2_affected = False

# function for moving Player 2 and attacking Player 1
def move_wizard():
    global walking_frame
    global wizard_right
    global health_affected
    global attacking_frame
    is_walking = False
    is_attacking = False


# moves left with left arrow
    if uvage.is_pressing('left arrow'):
        if wizard_right:
            wizard.flip()
            wizard_right = False
        wizard.x -= 5
        is_walking = True
# moves right with right arrow
    elif uvage.is_pressing('right arrow'):
        if not wizard_right:
            wizard.flip()
            wizard_right = True
        wizard.x += 5
        is_walking = True
# animating with spritesheet
    if is_walking:
        walking_frame += 0.3
        if walking_frame >= 5:
            walking_frame = 0
        wizard.image = wizard_images[int(walking_frame)]
        camera.draw(wizard)
# attacking Player 1
    elif uvage.is_pressing('keypad 0'):
        is_attacking = True
    if is_attacking:
        attacking_frame += 1
        if attacking_frame >= 13:
            attacking_frame = 0
        wizard.image = jack_attack[int(attacking_frame)]
        if wizard.right_touches(wizard2, -80, 10) and not health_affected and wizard_right:
            health_affected = True
            wizard2_health.x -= 2
        if wizard.left_touches(wizard2, -80, 10) and not health_affected and not wizard_right:
            health_affected = True
            wizard2_health.x -= 2
    else:
        health_affected = False
        wizard.image = wizard_images[-1]
    camera.draw(wizard)

# function to make Player 1 move and attack Player2, almost similar to the previous function
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
        if attacking2_frame >= 11:
            attacking2_frame = 0
        wizard2.image = wizard2_attack[int(attacking2_frame)]
        if wizard2.right_touches(wizard, -80, 10) and not health2_affected and wizard2_right:
            health2_affected = True
            wizard_health.x += 2
        if wizard2.left_touches(wizard, -80, 10) and not health2_affected and not wizard2_right:
            health2_affected = True
            wizard_health.x += 2
    else:
        health2_affected = False
        wizard2.image = wizard2_images[-1]
    camera.draw(wizard2)


# timer to count the cooldown for using wolf attack, cooldown duration in frames
cooldown_timer = 0
cooldown_duration = 300

empty_text = uvage.from_text(10, 10, "", 20, 'white')  # Create an "empty" text object
health_affected_by_enemy_wizard1 = False

# updating the timer to keep track
def update_cooldown_timer():
    global cooldown_timer
    global health_affected_by_enemy_wizard1

    if cooldown_timer > 0:
        cooldown_timer -= 1
        if cooldown_timer == 0:
            health_affected_by_enemy_wizard1 = False

# displaying the timer on screen
def display_cooldown_timer():
    global cooldown_timer

    if cooldown_timer > 0:
        cooldown_display = "WOLF COOLDOWN: " + str(int(cooldown_timer / 30)) + "s"
        cooldown_text = uvage.from_text(190, 580, cooldown_display, 18, '#CFCBCB')
        camera.draw(cooldown_text)
    else:
        # Clear the cooldown display when not in cooldown
        camera.draw(empty_text)

# function to move the wolf of Player 1 and attack Player 2
def move_enemy1():
    global enemy1
    global enemy1_frame
    global enemy_walking
    global cooldown_timer
    global health_affected_by_enemy_wizard1
# making sure that they can only press after the timer has reset
    if uvage.is_pressing('f') and cooldown_timer <= 0:
        enemy_walking = True
        cooldown_timer = cooldown_duration

    if enemy_walking:
        enemy1.x += 10

# checking to see if the enemy has reached the right edge of the screen
        if enemy1.x > camera.width:
            enemy1.x = -enemy1.width
            enemy_walking = False

# checking to see if enemy1 touches Player 2 and affects health
        if enemy1.right_touches(wizard, -80, 10) and not health_affected_by_enemy_wizard1:
            health_affected_by_enemy_wizard1 = True
            wizard_health.x += 10

    enemy1_frame += 0.3
    if enemy1_frame >= 5:
        enemy1_frame = 0

    enemy1.image = enemy1_images[int(enemy1_frame)]
    camera.draw(enemy1)

enemy2_images = uvage.load_sprite_sheet('Hyena_walk_B.png', 1, 6)
enemy2 = uvage.from_image(camera.width + 50, 444, enemy2_images[-1])
enemy2_frame = 0
enemy2_walking = False

enemy2_cooldown_timer = 0
enemy2_cooldown_duration = 300

empty_text = uvage.from_text(10, 10, "", 20, 'white')  # Create an "empty" text object
health_affected_by_enemy2_wizard2 = False

# the rest of the functions are similar to previous ones for the next Player's wolf
def update_enemy2_cooldown_timer():
    global enemy2_cooldown_timer
    global health_affected_by_enemy2_wizard2

    if enemy2_cooldown_timer > 0:
        enemy2_cooldown_timer -= 1
        if enemy2_cooldown_timer == 0:
            health_affected_by_enemy2_wizard2 = False

def display_enemy2_cooldown_timer():
    global enemy2_cooldown_timer

    if enemy2_cooldown_timer > 0:
        cooldown_display = "WOLF COOLDOWN: " + str(int(enemy2_cooldown_timer / 30)) + "s"
        cooldown_text = uvage.from_text(600, 580, cooldown_display, 18, '#CFCBCB')
        camera.draw(cooldown_text)
    else:
        # Clear the cooldown display when not in cooldown
        camera.draw(empty_text)

#function to move the wolf of Player 2 and attack Player 1
def move_enemy2():
    global enemy2
    global enemy2_frame
    global enemy2_walking
    global enemy2_cooldown_timer
    global health_affected_by_enemy2_wizard2

    if uvage.is_pressing('keypad 2') and enemy2_cooldown_timer <= 0:
        enemy2_walking = True
        enemy2_cooldown_timer = enemy2_cooldown_duration

    if enemy2_walking:
        enemy2.x -= 10

# checking if the enemy has reached the left edge of the screen
        if enemy2.x < -enemy2.width:
            enemy2.x = camera.width + 50
            enemy2_walking = False

# checking if enemy2 touches wizard2
        if enemy2.right_touches(wizard2, -80, 10) and not health_affected_by_enemy2_wizard2:
            health_affected_by_enemy2_wizard2 = True
            wizard2_health.x -= 10

    enemy2_frame += 0.3
    if enemy2_frame >= 5:
        enemy2_frame = 0

    enemy2.image = enemy2_images[int(enemy2_frame)]
    camera.draw(enemy2)

# functions to check if health is over for any of the players and displaying which player won in the end
def health_over2():
    game_over1 = False
    if wizard2_health.x <= 5:
        game_over1 = True
    if game_over1 ==True:
        gameover1_image = uvage.from_image(400, 300, 'player2wins.png')
        camera.draw(gameover1_image)
    camera.display()
def health_over1():
    game_over2 = False
    if wizard_health.x >= 782:
        game_over2 = True
    if game_over2 ==True:
        gameover2_image = uvage.from_image(400, 300, 'player1wins.png')
        camera.draw(gameover2_image)
    camera.display()

# tick function

def tick():
    camera.clear('black')
    objects_to_draw = [background_image, background_border, statue1_drawing, statue2_drawing, plat, tutorial1, tutorial2,
                    wizard2_healthbar, wizard2_healthgone, wizard2_health, wizard_healthbar, wizard_healthgone,
                    wizard_health, hider1, hider2, p2_drawing, p1_drawing]

# iterating over the list and drawing each object
    for i in objects_to_draw:
        camera.draw(i)

    move_wizard()
    move_wizard2()
    move_enemy1()
    move_enemy2()
    update_cooldown_timer()
    display_cooldown_timer()
    update_enemy2_cooldown_timer()
    display_enemy2_cooldown_timer()
    camera.draw(name)
    health_over2()
    health_over1()
    camera.display()

uvage.timer_loop(30, tick)



