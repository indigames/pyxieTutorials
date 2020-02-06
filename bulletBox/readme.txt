-------------------------------------
indi game engine

bulletBox
-------------------------------------

Example of moving 3D model mesh included in figure using Bullet physics
Calling a draw call for each mesh is very inefficient, so multiple meshes are merged into one mesh during data conversion.

root.py
	program entry point
deploy.py
	convert dae to iyxf(ige 3d data)
uploadLauncher.py
	upload prgram to launcher server

Brick.png
	class of 2d rectangle rigid body object	

Castle_200.dae
	3D model data


	
befor running this tutorial, you have to install igeBullet

[pip install igeBullet]


Bullet physics を利用してFigureに含まれる３Dモデルメッシュを動かすサンプル
メッシュ単位でドローコールを呼ぶと非常に効率が悪いので、データコンバートの際に１つのメッシュに複数のメッシュをマージしている

