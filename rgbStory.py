#RGB Story Assignment
#A Story of One's Life
import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.05

while True:
    #Nothing, 0s
    led[0] = (0, 0, 0)
    time.sleep(2)
    #And then, something
    led[0] = (30, 0, 0)
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    time.sleep(1)
    led[0] = (50, 0, 0)
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    #Gestation...something is beating
    time.sleep(0.7)
    led[0] = (70, 0, 0)
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    time.sleep(0.5)
    led[0] = (100, 0, 0)
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    time.sleep(0.3)
    led[0] = (150, 0, 0)
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    time.sleep(0.2)
    led[0] = (170, 0, 0)
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    time.sleep(0.1)
    for i in range(5):
        time.sleep(0.1)
        led[0] = (0, 0, 0)
        time.sleep(0.1)
        led[0] = (200, 0, 0)
    for i in range(10):
        time.sleep(0.05)
        led[0] = (0, 0, 0)
        time.sleep(0.05)
        led[0] = (200, 0, 0)
    #Born, Breathing (Yellow) - Hello World, 7s
    for i in range(2):
        led[0] = (255, 255, 0)
        time.sleep(1)
        #Alternates between color and light - simulates breathing and light gets dimmer as one ages
        led[0] = (255, 255, 255)
        time.sleep(1)
    #Youth, Adolescence (Orange) - In Between, 11s
    for i in range(2):
        led[0] = (235, 120, 0)
        time.sleep(1)
        led[0] = (240, 240, 240)
        time.sleep(1)
    #Young Adult - Fiery Passion, 15s
    for i in range(2):
        led[0] = (200, 0, 0)
        time.sleep(1)
        led[0] = (210, 210, 210)
        time.sleep(1)
    #Adulthood - Dreams into Action, 19s
    for i in range(2):
        led[0] = (175, 0, 175)
        time.sleep(1)
        led[0] = (170, 170, 170)
        time.sleep(1)
    #Middle Age - Settling Down, 23s
    for i in range(2):
        led[0] = (0, 100, 0)
        time.sleep(1)
        led[0] = (100, 100, 100)
        time.sleep(1)
    #Old Age - Sobering Calm, 27s
    for i in range(2):
        led[0] = (0, 0, 120)
        time.sleep(1)
        led[0] = (30, 30, 30)
        time.sleep(1)
    #They say that your life flashes before your eyes, 31s
    led[0] = (255, 255, 0)
    time.sleep(0.3)
    led[0] = (30, 30, 30)
    time.sleep(0.3)
    led[0] = (235, 120, 0)
    time.sleep(0.3)
    led[0] = (30, 30, 30)
    time.sleep(0.3)
    led[0] = (200, 0, 0)
    time.sleep(0.3)
    led[0] = (30, 30, 30)
    time.sleep(0.3)
    led[0] = (175, 0, 175)
    time.sleep(0.3)
    led[0] = (30, 30, 30)
    time.sleep(0.3)
    led[0] = (0, 100, 0)
    time.sleep(0.3)
    led[0] = (30, 30, 30)
    time.sleep(0.3)
    led[0] = (0, 0, 120)
    time.sleep(0.3)
    led[0] = (30, 30, 30)
    time.sleep(0.3)
    #A sudden parade of memories bygone
    for i in range(3):
        led[0] = (255, 255, 0)
        time.sleep(0.1)
        led[0] = (235, 120, 0)
        time.sleep(0.1)
        led[0] = (200, 0, 0)
        time.sleep(0.1)
        led[0] = (175, 0, 175)
        time.sleep(0.1)
        led[0] = (0, 100, 0)
        time.sleep(0.1)
        led[0] = (0, 0, 120)
        time.sleep(0.1)
    #All the colors slipping by
    for i in range(5):
        led[0] = (255, 255, 0)
        time.sleep(0.05)
        led[0] = (235, 120, 0)
        time.sleep(0.05)
        led[0] = (200, 0, 0)
        time.sleep(0.05)
        led[0] = (175, 0, 175)
        time.sleep(0.05)
        led[0] = (0, 100, 0)
        time.sleep(0.05)
        led[0] = (0, 0, 120)
        time.sleep(0.05)
    #Good night world
    led[0] = (0, 0, 0)
    time.sleep(5)
