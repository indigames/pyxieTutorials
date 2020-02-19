# igeSound

C++ extension Sound for 3D and 2D games.

You can install it using the PyPI:

	pip install igeSound
### Features
- (ogg , wav, mp3, flac) extension are supported
- Caching, preloading, streaming is supported
### Functions
# First, you need to import and init the sound system
```python
from igeSound import sound

_sound = sound()
_sound.init()
```

# Play the sound
```python
# (sound_name , stream = False, loop = False)
_sound.play('sound/background.ogg', False, False)

# I highly recommend to use streaming for ogg background music
```
# Release it when everything is done
```python
_sound.release()
```
# 3D sound optional
- Global

- Local


### Todo
- To support 3D sound
- Sound packing strucure

### Reference
- [soloud](http://sol.gfxile.net/soloud/)

