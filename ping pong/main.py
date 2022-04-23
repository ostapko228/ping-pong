

back = (200, 255, 255)
win_wight = 600
win_height = 500
window = display.set_mode((win_wight, win_height))
window.fill(back)
display.set_caption('Ping pong')

game = True
clock = time.Clock()
FPS = 120

while gsme:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
