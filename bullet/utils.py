import igeCore as core
import igeVmath as vmath
import igeBullet


class Utils:
    _instance = None

    _texture = core.texture("checker", 512, 512, core.GL_RGB)
    _texture.setCheckeredImage(0, 1, 0)
    shader = core.shaderGenerator()
    shader.setColorTexture(True)
    shader.setNumDirLamp(1)
    shader.setBoneCondition(1, 100)
    _efig = core.editableFigure('bullet')
    _efig.addMaterial("mate", shader)

    def __init__(self):
        None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def AddShapeMesh(self, shape : igeBullet.shape):

        meshName = "mesh{}".format(self._efig.numMeshes)
        jointName = "joint{}".format(self._efig.numMeshes)

        pos, nom, uv, idx = shape.getMeshData()
        numElem = len(pos) // 3
        idces = ((self._efig.numMeshes, 0, 0, 0),) * numElem

        self._efig.addMesh(meshName, "mate")
        self._efig.setVertexElements(meshName, core.ATTRIBUTE_ID_POSITION, pos)
        self._efig.setVertexElements(meshName, core.ATTRIBUTE_ID_NORMAL, nom)
        self._efig.setVertexElements(meshName, core.ATTRIBUTE_ID_UV0, uv)
        self._efig.setVertexElements(meshName, core.ATTRIBUTE_ID_BLENDINDICES, idces)
        self._efig.setTriangles(meshName, idx)
        self._efig.setMaterialParam("mate", "DiffuseColor", (1.0, 1.0, 1.0, 1.0))
        self._efig.setMaterialParamTexture("mate", "ColorSampler", self._texture,
                                             wrap_s=core.SAMPLERSTATE_BORDER,wrap_t=core.SAMPLERSTATE_BORDER,
                                             minfilter=core.SAMPLERSTATE_LINEAR, magfilter=core.SAMPLERSTATE_LINEAR)
        self._efig.addJoint(jointName)

    def GetFigure(self):
        return self._efig


def getLay(cam:core.camera, x,y):
    iproj = vmath.inverse(cam.projectionMatrix)
    iview = cam.viewInverseMatrix

    w,h = core.viewSize()
    pos = vmath.vec4(x / w / 2, y / h / 2, 0.0, 1.0)

    nearPos = iproj * pos;
    nearPos = iview * nearPos;
    pos.z = 1.0
    farPos = iproj * pos;
    farPos = iview * farPos;

    return nearPos, farPos

