import pygame
from pygame import mixer
import serial
import time
import random


# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
mixer.init()

# Define a dictionary to map keys to sounds
key_to_sound = {
    'a': mixer.Sound('notes/D1.wav'),
    's': mixer.Sound('notes/D2.wav'),
    'd': mixer.Sound('notes/D3.wav'),
    'f': mixer.Sound('notes/D4.wav'),
    'g': mixer.Sound('notes/D5.wav'),
    'h': mixer.Sound('notes/D6.wav'),
    'j': mixer.Sound('notes/D7.wav'),
}

# Define the tempo sound
tempo_sound = mixer.Sound('notes/metronome.wav')

# Create a Pygame screen of width 500 and height 500
screen = pygame.display.set_mode((500, 500))

# Connect to the micro:bit
ser = serial.Serial('COM26', 115200, timeout=0)

start_time = time.time()

while True:
    tempo = 60  # Default tempo is 60 BPM
    data = ser.readline().strip()
    if data and b':' in data:
        name, value = data.decode().split(':')
        if value:  # Check that value is not an empty string
            try:
                if name == 'pressure':
                    pressure = int(value)
                    print('Pressure:', pressure)
                elif name == 'heart':
                    heart = int(value)
                    print('Heart:', heart)
                    tempo = heart  # Update the tempo based on the heart rate
                    break
            except ValueError:
                print('Invalid value:', value)
                continue  # Skip to the next iteration

    time.sleep(0.1)

    if time.time() - start_time >= 10:  # 20 seconds have passed
        tempo = random.randint(50, 85)  # Select a random tempo between 60 and 85
        break

    if (tempo < 50) or (tempo > 85):
        print('Invalid tempo:', tempo)
        tempo = random.randint(50, 85)  # Select a random tempo between 60 and 85

print('Initial tempo:', tempo)
interval = (60 / tempo) * 1000  # Convert tempo to milliseconds

# Create a custom event for the tempo
TEMPO_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TEMPO_EVENT, int(interval))

# Run until the user asks to quit
running = True
start_ticks = pygame.time.get_ticks() # starter tick
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TEMPO_EVENT:
            # Play the tempo sound
            tempo_sound.play()
    

   # Read the pressure sensor value from the micro:bit
    data = ser.readline().strip()
    if data and b':' in data:
        name, value = data.decode().split(':')
        if name == 'pressure' and value.strip():
            try:
                pressure = int(value)
            except ValueError:
                print(f"Invalid value for pressure: {value}")
                continue

            # Play a different note depending on the pressure
            if pressure <= 100:
                pass
            elif pressure < 200:
                key_to_sound['a'].play()
            elif pressure < 300:
                key_to_sound['s'].play()
            elif pressure < 450:
                key_to_sound['d'].play()
            elif pressure < 600:
                key_to_sound['f'].play()
            elif pressure < 850:
                key_to_sound['g'].play()
            elif pressure < 950:
                key_to_sound['h'].play()
            else:
                key_to_sound['j'].play()
    time.sleep(0.1)
    # Flip the display
    pygame.display.flip()

    # check if 30 sec are up
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 # calculate how many seconds
    if seconds > 15: # if more than 30 seconds close the game
        running = False

# Done! Time to quit.
pygame.quit()