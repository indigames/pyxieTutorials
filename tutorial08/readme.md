# indi game engine

## Tutorial08
### igeOpenAL tutorial


- root.py
	- program entry point
- sound folder
	- sound resource

### Before running this tutorial, you have to install igeOpenAL
	[pip install igeOpenAL]

### Features
- [ogg , wav] extension are supported
- Preload supported

### Functions
- **First, you need to import and init the sound system**
	```
	import pyxopenal

	sound = pyxopenal.sound()
	sound.init()
	```

- **Play the sound**
	```
	# (sound_name , loop)
	sound.play('sound/beep2.ogg', False)
	```
- **Release it when everything is done**
	```
	sound.release()
	```
- **3D sound optional**
	- Global
	```
	# (option)
	sound.setListenerPosition(0, 0, -10);
	sound.setListenerOrientation(0, 0, -10, 0, -1.0, 0);
	```
	- Local
	```
	# (sound_name , option)
	sound.setPositon('sound/beep2.ogg', 0, 0, -10);
	sound.setPitch('sound/beep2.ogg', 1.1);
	sound.setGain('sound/beep2.ogg', 1.1);
	sound.setRolloff('sound/beep2.ogg', 1.1);
	```

### Todo
- To support streaming
- Sound packing strucure

### Reference
- [OpenAL](https://www.openal.org/)
- [OpenAL Soft](https://github.com/kcat/openal-soft) - a software implementation of the OpenAL 3D audio API.
- [Xiph](https://xiph.org/) - Ogg loader

