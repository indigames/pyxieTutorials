# indi game engine

## Tutorial10 - IGE Profiler

### Capture the game profiling scope (using the tutorial01 graphic)

#### root.py
- program entry point
- ige apprications have to start root.py

#### ship.png
- asset image
- get from https://opengameart.org/content/modular-ships
- cc0 License

#### connecting to profiler tool
- run Tracy.exe from `tools` folder
- connect
#### profiling scope
- enable profiler
	```
	profiler = core.profiler(True)
	```

- capturing
	```
	profiler = core.profiler('camera.shoot')
    camera.shoot(showcase)
    del profiler
	```