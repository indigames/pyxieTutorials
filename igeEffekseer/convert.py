
import igeCore
from igeCore import devtool
import os

# devtool.convertAssets('.','.', igeCore.TARGET_PLATFORM_PC)
devtool.convertAssets('.','.', igeCore.TARGET_PLATFORM_MOBILE)

for root, dirs, files in os.walk("Effects"):
    for file in files:
        if file.endswith(".efkproj") or file.endswith(".efkefc"):
            file_input = os.path.join(root, file)
            file_output = os.path.splitext(file_input)[0] + ".efk"
            command = "Tool\Effekseer.exe -cui -in " + str(file_input) + " -e " + str(file_output)
            print('processing ' + file_input)
            os.system(command)