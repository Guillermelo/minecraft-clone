
from sre_constants import JUMP
from turtle import speed
from ursina import *
from ursina.texture_importer import load_texture
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

grass_texture = load_texture('assets/grass.png')
dirt_texture = load_texture('dirt.png')
brick_texture = load_texture('brick')
stone_texture = load_texture('stone.png')
sky_texture = load_texture('skybox.png')
block_pick = 1
axe_texture = load_texture('axe.png')
put_block = Audio('assets/colocarwav', loop = False, autoplay = False, volume = 200)
punch_block = Audio('assets/quitarwav', loop = False, autoplay = False, volume = 200)
soundtrack = Audio('assets/cancion', loop = True, autoplay = True, volume = 200)

lable = Text(text='1            2          3           4           5', scale=1, x=-0.3,
             y=-0.45,visible=True ,color=color.white)

def active(self):
	self.position = Vec2(0.3,-0.5)

def passive(self):
		self.position = Vec2(0.4,-0.6)

def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4



class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            model = 'assets/block',
            position = position,
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            
            scale = 0.5
        )

    def input(self,key):
         if self.hovered:
            if key == 'right mouse down':
                put_block.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)


            if key == 'left mouse down':
                punch_block.play()
                destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/axe',
            scale = 1.5,
            texture = axe_texture,
            rotation = Vec3(90,-30,-100),
            position = Vec2(0.5, -0.3))
def active(self):
	self.position = Vec2(0.3,-0.5)

def passive(self):
	self.position = Vec2(0.4,-0.6)

			





for z in range(35):
    for x in range(35):
        voxel = Voxel(position = (x,0,z))



sky = Sky()
player = FirstPersonController(speed=7)

hand = Hand()

app.run()
