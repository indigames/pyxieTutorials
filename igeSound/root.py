"""
"""
from igeSound import sound
import time

_sound = sound()
_sound.init()

# sound load cache
_sound.load('sound/beep2.ogg');

# play
_sound.play('sound/beep2.ogg', False, True)

# Wait for 5 seconds
time.sleep(5)

# release
_sound.release()