# Python 3.8.2 Keylogger

### If you use this software, you agree to only use it for learning or white hat purposes.

>Don't be evil - Google

It's important to learn how bad actors think to protect your own software. This was a practice exercise to see if I could write a keylogger on MacOS. It works! However, due to MacOS security, it requires to be run as root and it must be white listed in the settings. Regardless, once the script was white listed, all keyboard input typed can be logged. Everything is saved to a file called `log.txt`. My main interest is the pure text the user types so non-relevant key presses are excluded. This can easily be changed for someone interested in all key presses.

For more information on Pynput limitations: https://pynput.readthedocs.io/en/latest/limitations.html
