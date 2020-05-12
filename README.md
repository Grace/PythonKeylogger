# Python 3.8.2 Keylogger

#### Disclaimer: If you use this software, you agree to only use it for learning or white hat purposes.

>Don't be evil - Google

This was a practice exercise to see if I could write a keylogger on MacOS. It works! However, due to MacOS security, it requires to be run as root and it must be white listed in the settings. Regardless, once the script was white listed, all keyboard input typed can be logged. Everything is saved to a file called `log.txt`. My main interest is the pure text the user types so non-relevant key presses are excluded. This can easily be changed for someone interested in all key presses.

For more information on Pynput limitations: https://pynput.readthedocs.io/en/latest/limitations.html

### Future ideas:
- Quietly start the script when the installed machine starts
- Feature to send a daily log to a specified email or phone number
- Text or email alerts triggered by certain words
- Create a database. Store all key presses and their frequency. Store all words and their frequency. Flag text that looks like passwords.
- Make a dashboard that explores the data
- Turning this into an easily-installable app for users (it would still need root permission and to be whitelisted on Mac)
- A reminder message to users to not be evil and use their code for good.