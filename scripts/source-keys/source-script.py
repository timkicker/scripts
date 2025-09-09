import keyboard
import time
import threading

# Flag to enable/disable the script
suspend = False

# Function to toggle the suspend mode
def toggle_suspend():
    global suspend
    suspend = not suspend
    print("Script enabled!" if not suspend else "Script disabled!")

# Bunnyhop loop for Space key
def bunnyhop_space():
    print("Bunnyhop mode (Space key) active!")
    while not suspend:
        if keyboard.is_pressed('space'):
            print("Jumping...", end='\r')
            while keyboard.is_pressed('space'):
                keyboard.send("space")
                time.sleep(0.001)
        else:
            break
    print("Bunnyhop mode (Space key) ended.")

# Bunnyhop and additional action for X key
def bunnyhop_x():
    print("Bunnyhop and action E (X key) active!")
    while not suspend:
        if keyboard.is_pressed('x'):
            print("Jumping and action E...", end='\r')
            while keyboard.is_pressed('x'):
                keyboard.send("space")
                keyboard.send("e")
                time.sleep(0.001)
        else:
            break
    print("Bunnyhop and action E (X key) ended.")

# Set up hotkeys
keyboard.add_hotkey('f3', toggle_suspend)

# Main loop
print("Script running... Press F3 to enable/disable.")
try:
    while True:
        if not suspend:
            if keyboard.is_pressed('space'):
                bunnyhop_space()
            elif keyboard.is_pressed('x'):
                bunnyhop_x()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nScript terminated.")

