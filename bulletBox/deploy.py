import igeCore as core
from igeCore import devtool
from igeCore import apputil
from igeCore.apputil import launch_server
import igeVmath as vmath
import pickle
import glob
import os

def convertVoxelModel(filename, src, dest, platform,scale):

    efig = core.editableFigure('efig')
    devtool.loadCollada(os.path.join(src, filename+'.dae'), efig)

    boxinfo = []
    for i in range(efig.numMeshes):
        aabb = vmath.aabb()
        inverts = efig.getVertexElements(i, core.ATTRIBUTE_ID_POSITION)
        for pos in inverts:
            pos *= scale
            aabb.insert(pos)
        outverts = []
        for pos in inverts:
            pos *= scale
            outverts.append(pos - aabb.center)
        efig.setVertexElements(i, core.ATTRIBUTE_ID_POSITION, outverts)
        efig.setJoint(i, position=aabb.center)

        min, max = efig.getAABB(i)
        pos, rot, _ = efig.getJoint(i)
        data = ((pos.x, pos.y, pos.z), (rot.x, rot.y, rot.z, rot.w), (min.x, min.y, min.z), (max.x, max.z, max.z))
        boxinfo.append(data)

    filepath = os.path.join(dest, filename+'.pickle')
    with open(filepath, 'wb') as f:
        pickle.dump(boxinfo, f)

    src = efig.getTextureSource()
    for tex in src:
        texfilename = os.path.basename(tex['path'])
        name, _ = os.path.splitext(texfilename)
        newtex = tex.copy()
        newtex['path'] = name
        efig.replaceTextureSource(tex, newtex)
        filepath = glob.glob('**/'+texfilename, recursive=True)
        if len(filepath) is not 0:
            devtool.convertTextureToPlatform(filepath[0], os.path.join(dest, name), platform, tex['normal'], tex['wrap'])

    efig.mergeMesh()
    efig.saveFigure(os.path.join(dest, filename))

def deployPlatform(src, model, appName, userID, appVersion, platform):
    dest = '.tmp/stage/' + appName + '/' + apputil.platformName(platform)
    apputil.makeDirectories(dest)
    convertVoxelModel(model, src, dest, platform)
    #devtool.appendFileBehavior('.pickle','copy')
    devtool.compileAndCopy(src, dest)
    devtool.packFolders(dest)
    addr = '/' + userID + '/' + appName + '/' + str(appVersion) + '/' + apputil.platformName(platform)
    launch_server.upload_files(dest, addr)


