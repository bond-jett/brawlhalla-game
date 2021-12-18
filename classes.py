import const
class GameObject:
    def __init__(self, image, x=0, y=0, speed=(0,0), w=None, h=None):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(x, y)

    def move(self):
        self.pos = self.pos.move(self.speed[0],self.speed[1])
        if self.pos.right > const.window_width:
            self.pos.left = 0
