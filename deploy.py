import pyxie
from pyxie import devtool

#devtool.deploy('tutorial01', 'tutorial', 'tutorial01', '10')
#devtool.deploy('tutorial02', 'tutorial', 'tutorial02', '10')
#devtool.deploy('tutorial03', 'tutorial', 'tutorial03', '10')
#devtool.deploy('tutorial04', 'tutorial', 'tutorial04', '10')
#devtool.deploy('tutorial05', 'tutorial', 'tutorial05', '10')


import Tutorial06.deploy
Tutorial06.deploy.deployPlatform('Tutorial06', 'Castle_200', 'tutorial06', 'tutorial', '10', pyxie.TARGET_PLATFORM_PC)
Tutorial06.deploy.deployPlatform('Tutorial06', 'Castle_200', 'tutorial06', 'tutorial', '10', pyxie.TARGET_PLATFORM_IOS)
Tutorial06.deploy.deployPlatform('Tutorial06', 'Castle_200', 'tutorial06', 'tutorial', '10', pyxie.TARGET_PLATFORM_ANDROID)
