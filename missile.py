#ANCHOR - Imports
import math
import pyglet
import random
import time
import threading

#ANCHOR - Constants
gravity = 1
missilespeed = 1

#ANCHOR - Variables

points = 0

#SECTION - Set up
#ANCHOR - Setup the window
window = pyglet.window.Window(1000, 750)
window.set_caption("Missile sim")

#ANCHOR - Setup batches
entity_batch = pyglet.graphics.Batch()
terrain_batch = pyglet.graphics.Batch()

#ANCHOR - Setup missile
missile = pyglet.sprite.Sprite(pyglet.image.load("assets/missile.png"), x=0, y=0, batch=entity_batch)
missile.rotation = 90

#ANCHOR - place missile
missile.x = window.width / 2
missile.y = window.height / 2


@window.event
def on_draw():
    window.clear()
    terrain_batch.draw()
    entity_batch.draw()

pyglet.app.run()