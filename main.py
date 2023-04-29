from pygame import*
init()


#перший рівень
level1 = [
    "r                                                                    .",
    "r                                                                    .",
    "r                                                                    .",
    "r                                                                    .",
    "rr    °  °      l                             r    °  °  °     l     .",
    "r  ------------                                ---------------       .",
    "rr / l                                       r / l         r / l     .",
    "rr   l                                       r   l         r   l     .",
    "rr     °  l                       r     °  °     l   r         l     .",
    "r  ------                           ------------       -------       .",
    "r     r / l                                          r / l           .",
    "r     r   l                                          r   l           .",
    "r     r       °  °   l                       r   °  °    l           .",
    "r       ------------                           ---------             .",
    "r                r / l                       r / l                   .",
    "r                r   l                       r   l                   .",
    "r                                                                    .",
    "----------------------------------------------------------------------"]

#розміри рівня
level1_width = len(level1[0]) * 40
level1_height = len(level1) * 40

#розміри вікна
W = 1280
H = 720


#створюємо вікно
window = display.set_mode(W, H)#вікно
back = transform.scale(image.load('image/bgr.png'), (W, H))#фон
display.set_caption('Blockada')#назва вікно
display.set_icon(image.load('image/portal.png'))#іконка вікна


'''КАРТИНКИ СПРАЙТІВ'''
hero_l = "images/sprite1.png"
hero_r = "images/sprite1_r.png"

enemy_l = "images/cyborg.png"
enemy_r = "images/cyborg_r.png"

coin_img = "images/coin.png"
door_img = "images/door.png"
key_img = "images/key.png"
chest_open = "images/cst_open.png"
chest_close = "images/cst_close.png"
stairs = "images/stair.png"
portal_img = "images/portal.png"
platform = "images/platform.png"
power = "images/mana.png"
nothing = "images/nothing.png"


'''ФУНКЦІОНАЛ'''
class Settings(sprite.Sprite):#загальний клас для інших класів
    
    def __init__(self, x, y, width, height, speed, img):#загальні властивості
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):#відображення об'єктів
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Settings):#клас головного героя

    def r_l(self):#влево вправо
        pass

    def u_d(self):#карапкання по драбині, спускання по драбині
        pass


class Enemy(Settings):#клас ворогів

    def __init__(self, x, y, width, height, speed, img):#властивості ворогів
        Settings.__init__(self, x, y, width, height, speed, img)
        self.side = side

    def update(self):#рух ворогів
        pass


class Camera(object):

    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
    
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_config(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + W / 2, -t + H / 2
    
    l = min(0, l)  # Не виходимо за ліву межу
    l = max(-(camera.width - W), l)  # Не виходимо за праву межу
    t = max(-(camera.height - H), t)  # Не виходимо за нижню межу
    t = min(0, t)  # Не виходимо за верхню межу
    
    return Rect(l, t, w, h)

def collides():#зіткнення
    pass

def menu():#меню
    pass

def rules():
    pass

def pause():#пауза
    pass

def restart():#спочатку
    pass

def start_pos():#стартова позиція

    global items
    global camera

    camera = Camera(camera_config, level1_width, level1_height)
    items = sprite.Group()


    block_r = []
    block_l = []
    plat = []
    coins = []
    stairs_lst = []

    x = 0
    y = 0

    for r in level1:
        for c in r:
            if c == '-':
                p1 = Settings(x, y, 40, 40, 0, platform)
                plat.append(p1)
                items.add(p1)
            if c = 'l':
                p2 = Settings(x, y, 40, 40, 0, nothing)
                block_l.append(p2)
                items.add(p2)
            if c = 'r':
                p3 = Settings(x, y, 40, 40, 0, nothing)
                block_r.append(p3)
                items.add(p3)
            if c = '°':
                p4 = Settings(x, y, 40, 40, 0, coin_img)
                coins.append(p4)
                items.add(p4)
            if c = '/':
                p5 = Settings(x, y - 40, 40, 180, 0, stairs)
                stairs_lst.append(p5)
                items.add(p5)
            x += 40
        y += 40
        x = 0

def lvl1():
    
    game = True

    while  game:
        time.delay(10)
        for e in event.get():
            if e.type == QUIT:
                game = False
            
    

    for i in items:
        window.blit(i.image, camera.apply(i))

    display.update()

def lvl1_end():#кінець першого рівня
    pass


start_pos()
lvl1()






