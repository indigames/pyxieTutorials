"""
"""
import pyxopenal
import time

sound = pyxopenal.sound()
sound.init()

# sound load cache
sound.load('sound/beep2.ogg');

# 3D sound handle
sound.setPositon('sound/beep2.ogg', 0, 0, -10);
sound.setPitch('sound/beep2.ogg', 1.1);
sound.setGain('sound/beep2.ogg', 1.1);
sound.setRolloff('sound/beep2.ogg', 1.1);
sound.setListenerPosition(0, 0, -10);
sound.setListenerOrientation(0, 0, -10, 0, -1.0, 0);

# play
sound.play('sound/beep2.ogg', False)

# Wait for 5 seconds
time.sleep(5)

# release
sound.release()