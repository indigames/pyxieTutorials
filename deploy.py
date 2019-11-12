import igeCore as core
from igeCore import devtool

devtool.deploy('tutorial01', 'tutorial', 'tutorial01', '10')
devtool.deploy('tutorial02', 'tutorial', 'tutorial02', '10')
devtool.deploy('tutorial03', 'tutorial', 'tutorial03', '10')
devtool.deploy('tutorial04', 'tutorial', 'tutorial04', '10')
devtool.deploy('tutorial05', 'tutorial', 'tutorial05', '10')
devtool.deploy('tutorial06', 'tutorial', 'tutorial06', '10')

import tutorial07.deploy
tutorial07.deploy.deployPlatform('tutorial07', 'Castle_200', 'tutorial07', 'tutorial', '10', core.TARGET_PLATFORM_PC)
tutorial07.deploy.deployPlatform('tutorial07', 'Castle_200', 'tutorial07', 'tutorial', '10', core.TARGET_PLATFORM_IOS)
tutorial07.deploy.deployPlatform('tutorial07', 'Castle_200', 'tutorial07', 'tutorial', '10', core.TARGET_PLATFORM_ANDROID)
