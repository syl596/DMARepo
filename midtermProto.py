import time
import board
import busio
import digitalio
import audioio
import audiomp3
from rainbowio import colorwheel
import neopixel

NUM_PIXELS = 12  # NeoPixel Ring Length
BRIGHTNESS = 0.07 # Set Brightness

# Enable Button Input
button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

num_sample = 2 # Amount of mp3 Files
sample_number = 0 # Starting File
hit_count = 0 #Set Hit/Coin Counter

# Enable Pins to Set Up Speaker
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True
speaker = audioio.AudioOut(board.A0)

#Set Up NeoPixel
strip = neopixel.NeoPixel(board.D5, NUM_PIXELS, brightness=BRIGHTNESS)

#Main Loop
while True:
    #Play coin sfx if 9 coins or under, yellow LED
    if hit_count < 9:
        strip.fill((colorwheel(40)))
        sample = "/protoSamp/0.mp3"
        mp3stream = audiomp3.MP3Decoder(open(sample, "rb"))
        speaker.play(mp3stream)
        print("Playing", sample)
        while speaker.playing:
            pass
        while button.value:
            pass
        #Add 1 to Hit/Coin Counter
        hit_count = hit_count + 1
    #Play 1up sfx if 10 coins, green LED
    else:
        strip.fill((colorwheel(80)))
        sample = "/protoSamp/1.mp3"
        mp3stream = audiomp3.MP3Decoder(open(sample, "rb"))
        speaker.play(mp3stream)
        print("Playing", sample)
        while speaker.playing:
            pass
        while button.value:
            pass
        #Reset Hit/Coin Counter
        hit_count = 0
