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
window = display.set_mode((W, H))#вікно
back = transform.scale(image.load('images/bgr.png'), (W, H))#фон
display.set_caption('Blockada')#назва вікно
display.set_icon(image.load('images/portal.png'))#іконка вікна


'''КАРТИНКИ СПРАЙТІВ'''
hero_r = "images/sprite1.png"
hero_l = "images/sprite1_r.png"

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
        key_pressed = key.get_pressed()

        if key_pressed[K_a]:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))

        if key_pressed[K_d]:
            self.rect.x += self.speed
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))

    def u_d(self):#карапкання по драбині, спускання по драбині        
        if key_pressed[K_w]:
            self.rect.y -= self.speed

        if key_pressed[K_s]:
            self.rect.y += self.speed


class Enemy(Settings):#клас ворогів

    def __init__(self, x, y, width, height, speed, img):#властивості ворогів
        Settings.__init__(self, x, y, width, height, speed, img)
        self.side = side

    def update(self):#рух ворогів
        pass


class Camera(object):#клас камера

    def __init__(self, camera_func, width, height):#властивості камери
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
    
    def apply(self, target):#рух камери
        return target.rect.move(self.state.topleft)
    
    def update(self, target):#позиція камери
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

    for s in stairs_lst:
        if sprite.collide_rect(hero, s):
            hero.u_d()

            if hero.rect.y < hero.rect.y - 40:
                hero.rect.y = hero.rect.y - 40
                
            if hero.rect.y > hero.rect.y + 130:
                hero.rect.y = hero.rect.y +130
            

def menu():#меню
    pass


def rules():
    pass


def pause():#пауза
    pass


def restart():#спочатку
    pass


def start_pos():#стартова позиція

    global items, camera, hero, block_r, block_l, plat, coins, stairs_lst
    
    hero = Player(300, 650, 50, 50, 5, hero_r)
    camera = Camera(camera_config, level1_width, level1_height)#створюємо камеру яка рухається за гравцем
    items = sprite.Group()


    block_r = []
    block_l = []
    plat = []
    coins = []
    stairs_lst = []

    x = 0
    y = 0

    for r in level1:#відмальовування першого рівня
        for c in r:
            if c == '-':
                p1 = Settings(x, y, 40, 40, 0, platform)#платформа
                plat.append(p1)
                items.add(p1)
            if c == 'l':
                p2 = Settings(x, y, 40, 40, 0, nothing)#невидимі блоки зліва
                block_l.append(p2)
                items.add(p2)
            if c == 'r':
                p3 = Settings(x, y, 40, 40, 0, nothing)#невидимі блоки зправа
                block_r.append(p3)
                items.add(p3)
            if c == '°':
                p4 = Settings(x, y, 40, 40, 0, coin_img)#монетка
                coins.append(p4)
                items.add(p4)
            if c == '/':
                p5 = Settings(x, y - 40, 40, 180, 0, stairs)#сходи
                stairs_lst.append(p5)
                items.add(p5)
            x += 40
        y += 40
        x = 0
    items.add(hero)


def lvl1():#робота першого рівня
    
    game = True

    while  game:#гра

        time.delay(5)
        window.blit(back, (0, 0))

        for e in event.get():
            if e.type == QUIT:
                game = False

        hero.r_l()
        collides()
        camera.update(hero)   

        for i in items:#відмальовуння об'єктів на екрані першого рівня
            window.blit(i.image, camera.apply(i))

        display.update()

def lvl1_end():#кінець першого рівня
    pass


start_pos()
lvl1()






