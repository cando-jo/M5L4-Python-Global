#pgzero

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Uzaylı Koşusu" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayı

# Nesneler
uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("arkaplan")
kutu = Actor('kutu', (550, 265))
yeni_resim = 'uzaylı' # Anlık Görüntüyü Takip Eder
ari = Actor('arı', (850, 175))
ob = Actor("OB")
oyun_sonu = 0
puan = 0

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
    ari.draw()
    screen.draw.text(puan, pos=(10, 10), color="white", fontsize = 24)
    if oyun_sonu == 1:
        ob.draw()
        screen.draw.text("Enter'a Basınız", pos=(170, 250), color= "red", fontsize = 36)

def update(dt):
    global yeni_resim
    global oyun_sonu
    global puan

    arilar()
    kutular()
        
    # Kontroller
    if keyboard.left or keyboard.a and uzayli.x > 20:
        uzayli.x = uzayli.x - 5
        if yeni_resim != 'sol':
            uzayli.image = 'sol'
            yeni_resim = 'sol'
    elif keyboard.right or keyboard.d and uzayli.x < 580:
        uzayli.x = uzayli.x + 5
        if yeni_resim != 'sağ':
            uzayli.image = 'sağ'
            yeni_resim = 'sağ'
    elif keyboard.down or keyboard.s:
        if yeni_resim != 'eğilme':
            uzayli.image = 'eğilme'
            yeni_resim = 'eğilme'
            uzayli.y = 250
    else:
        if uzayli.y > 240 and yeni_resim == 'eğilme':
            uzayli.image = 'uzaylı'
            yeni_resim = 'uzaylı'
            uzayli.y = 240
    
    if oyun_sonu == 1 and keyboard.enter:
        oyun_sonu = 0 
        puan = 0
        uzayli.pos = (50, 240)
        kutu.pos = (550, 265)
        ari.pos = (850, 175)
    
    # Çarpışma
    if uzayli.colliderect(kutu) or uzayli.colliderect(ari):
        oyun_sonu = 1
        
def on_key_down(key):
    # Zıplama
    if keyboard.space or keyboard.up or keyboard.w:
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)

def kutular():
    global puan
    if kutu.x > -20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else:
        kutu.x = WIDTH + 20
        puan = puan + 1
        
def arilar():
    global puan
    if ari.x > -20:
        ari.x = ari.x - 5
    else:
        ari.x = WIDTH + 20
        puan = puan + 1
