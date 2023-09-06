import turtle
import random
import time

#ANCHOR -  variables

points: int = 0
oldpoints: int = 0
missilespeed: int = 5
enemyspeed: int = 3

#ANCHOR - lists
missiles = []
targets = []
enemies = []
obstacles = []
explosions = []
hits = []

# ANCHOR - Set Up Screen
screen = turtle.Screen()
screen.setup(1000, 750)
screen.bgcolor("black")
screen.title("")

#SECTION - functions

# ANCHOR - Set Up Pen
def setup(mis: int, tar: int, enmi: int, obs:int , trails: bool): #! mis = missiles, tar = targets, enmi = enemies, obs = obstacles
    """Set up the game with the given number of missiles, targets, enemies, and obstacles."""
    # create the missiles
    for i in range(mis):
        missile = turtle.Turtle()
        missile.speed(0)
        missile.shape("triangle")
        missile.shapesize(1,2)
        missile.color("red")
        missile.penup()
        missile.goto(0, 0)
        missile.setheading(random.randint(0, 360))
        missiles.append(missile)
    # create the targets
    for i in range(tar):
        target = turtle.Turtle()
        target.speed(0)
        target.shape("circle")
        target.color("green")
        target.penup()
        target.goto(0, 0)
        targets.append(target)
    # create the allies
    for i in range(enmi):
        enemy = turtle.Turtle()
        enemy.speed(0)
        enemy.shape("triangle")
        enemy.color("blue")
        enemy.penup()
        enemy.goto(0, 0)
        enemies.append(enemy)
    # create the obstacles
    for i in range(obs):
        obstacle = turtle.Turtle()
        obstacle.speed(0)
        obstacle.shape("square")
        obstacle.color("grey")
        obstacle.shapesize(2,2)
        obstacle.penup()
        obstacle.goto(0, 0)
        obstacles.append(obstacle)
    # set up explosion
    for i in range(1):
        explosion = turtle.Turtle()
        explosion.hideturtle()
        explosion.speed(0)
        explosion.shape("circle")
        explosion.color("orange")
        explosion.penup()
        explosion.goto(0, 0)
        explosions.append(explosion)
    # place around the screen
    for missile in missiles:
        missile.goto(random.randint(-400, 400), random.randint(-300, 300))
    for target in targets:
        target.goto(random.randint(-400, 400), random.randint(-300, 300))
    for enemy in enemies:
        enemy.goto(random.randint(-400, 400), random.randint(-300, 300))
    for obstacle in obstacles:
        obstacle.goto(random.randint(-400, 400), random.randint(-300, 300))

     # create the trails
    if trails == True:
        for missile in missiles:
            missile.pendown()
        for target in targets:
            target.pendown()
        for enemy in enemies:
            enemy.pendown()
        for obstacle in obstacles:
            obstacle.pendown()
    

# SECTION - missile guidance

#ANCHOR - Direct
# 1 - each missile aim for its closest target directly
def missile_guidance_direct():
    for missile in missiles:
        # get the closest target
        closest_target = targets[0]
        for target in targets:
            if missile.distance(target) < missile.distance(closest_target):
                closest_target = target
        # aim at the target
        missile.setheading(missile.towards(closest_target))
        # move forward
        missile.forward(missilespeed)

#TODO - missile guidance 2
# 2 - WIP

#!SECTION 

# SECTION - enemy guidance

# ANCHOR - Direct
# 1 - each enemy aim for the closest missile directly
def enemy_guidance_direct():
    for enemy in enemies:
        # get the closest missile
        closest_missile = missiles[0]
        for missile in missiles:
            if enemy.distance(missile) < enemy.distance(closest_missile):
                closest_missile = missile
        # aim at the missile
        enemy.setheading(enemy.towards(closest_missile))
        # move forward
        enemy.forward(enemyspeed)

#TODO -  - Predictive
# 2 - aim for where the missile is going to be when the enemy reaches it
def enemy_guidance_predictive():
    for enemy in enemies:
        # get the closest missile
        closest_missile = missiles[0]
        for missile in missiles:
            if enemy.distance(missile) < enemy.distance(closest_missile):
                closest_missile = missile
        # aim at the missile
        enemy.setheading(enemy.towards(closest_missile))
        # move forward
        enemy.forward(enemyspeed)

#!SECTION

# ANCHOR - Explode
# cool explosion effect
def explode():
    for explosion in explosions:
        for i in range(10):
            explosion.goto(hits[0].xcor(), hits[0].ycor())
            explosion.showturtle()
            explosion.setheading(random.randint(0, 360))
            explosion.forward(10)
            explosion.color(random.choice(["orange", "yellow", "red", "white"]))
            time.sleep(0.01)
            explosion.hideturtle()
    hits.clear()


#!SECTION
#SECTION - Setup

# ANCHOR - eternal pen
eternal_pen = turtle.Turtle()
eternal_pen.hideturtle()
eternal_pen.speed(0)
eternal_pen.color("white")
eternal_pen.penup()
eternal_pen.goto(0, 300)
eternal_pen.write("Points: {}".format(points),
                  align="center", font=("System", 24, "normal"))

# ANCHOR - Setup config
# run setup
setup(1, 1, 1, 0, True)



#!SECTION
# ANCHOR - Main loop

while True:
    # missile guidance
    missile_guidance_direct()

    # enemy guidance
    enemy_guidance_direct()

    # check if missile hit a target
    if len(targets) > 0:
        for missile in missiles:
            for target in targets:
                if missile.distance(target) < 30:
                    hits.append(missile)
                    missiles.remove(missile)
                    missile.hideturtle()
                    targets.remove(target)
                    target.hideturtle()
                    explode()
                    oldpoints = points
                    points += 1
                    print(points, "points!")
    # check if missile hit an obstacle\
    if len(obstacles) > 0:
        for missile in missiles:
            for obstacle in obstacles:
                if missile.distance(obstacle) < 30:
                    hits.append(missile)
                    missiles.remove(missile)
                    missile.hideturtle()
                    explode()
                    oldpoints = points
                    points -= 1
                    print(points, "points!")
    # check if an enemy hit a missile
    if len(enemies) > 0:
        for missile in missiles:
            for enemy in enemies:
                if missile.distance(enemy) < 30:
                    hits.append(missile)
                    missiles.remove(missile)
                    missile.hideturtle()
                    enemies.remove(enemy)
                    enemy.hideturtle()
                    explode()
                    oldpoints = points
                    points -= 1
                    print(points, "points!")
    # check if an enemy hit an obstacle
    if len(enemies) > 0:
        for obstacle in obstacles:
            for enemy in enemies:
                if obstacle.distance(enemy) < 30:
                    hits.append(obstacle)
                    obstacles.remove(obstacle)
                    obstacle.hideturtle()
                    explode()
                    oldpoints = points
                    points += 1
                    print(points, "points!")

    # update points if changed
    if points != oldpoints:
        eternal_pen.clear()
        eternal_pen.write("Points: {}".format(points),
                            align="center", font=("System", 24, "normal"))
    oldpoints = points
    # check if game over and have win or lose based on points
    if len(missiles) == 0:
        if points > 0:
            print("Missile win!")
            eternal_pen.clear()
            eternal_pen.write("Missile win!", align="center",
                              font=("System", 24, "normal"))
        else:
            print("Missile lose!")
            eternal_pen.clear()
            eternal_pen.write("Missile lose!", align="center",
                              font=("System", 24, "normal"))
        break

time.sleep(5)