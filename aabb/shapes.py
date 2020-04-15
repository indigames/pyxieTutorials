import math
import igeVmath as vmath

###################################################################################################
# Plane
###################################################################################################
_spriteIndices=(0, 2, 1, 1, 2, 3)
def makePlane(width:float, height:float, uv_left_top:tuple=(0,0), uv_right_bottom:tuple=(1,1), normal=None):
	w = width / 2
	h = height / 2
	points = ((-w, h, 0.0), (w, h, 0.0), (-w, -h, 0.0), (w, -h, 0.0))

	if normal is not None:
		newpoints = []
		nom0 = (0, 0, 1)
		mat = vmath.mat33(vmath.quat_rotation(nom0, normal))
		for p in points:
			newpoints.append(mat * p)
		points = newpoints

	uvs = (uv_left_top[0], uv_right_bottom[1],
		   uv_right_bottom[0], uv_right_bottom[1],
		   uv_left_top[0], uv_left_top[1],
		   uv_right_bottom[1], uv_left_top[1])

	nom = (0,0,-1)
	if normal is not None:
		nom = normal
	norms = (nom, nom, nom, nom)

	return points, norms, uvs, _spriteIndices

###################################################################################################
# Box
###################################################################################################
cubeN = ((-1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 0.0, 0.0),
		 (0.0, -1.0, 0.0), (0.0, 0.0, 1.0), (0.0, 0.0, -1.0))
cubeF = ((0, 1, 5, 4), (4, 5, 6, 7), (7, 6, 2, 3),
		 ( 1, 0, 3, 2 ), ( 1, 2, 6, 5 ), ( 0, 4, 7, 3 ))
cubeV = ((-.5, -.5, -.5), (-.5, -.5,  .5), ( .5, -.5,  .5), ( .5, -.5, -.5),	# Lower tier (lower in y)
		 (-.5, .5, -.5), (-.5, .5,  .5), ( .5, .5, .5), ( .5, .5, -.5)) 		# Upper tier

cubeT = ((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0))

def makeBox(width:float, height:float, depth:float):
	poss = []
	noms = []
	uvs = []
	idxs = []

	nvrt = 0
	for i in range(6):
		for j in range(4):
			poss.append((cubeV[cubeF[i][j]][0] * width, cubeV[cubeF[i][j]][1] * height, cubeV[cubeF[i][j]][2] * depth))
			noms.append((cubeN[i][0], cubeN[i][1], cubeN[i][2]))
			uvs.append((cubeT[j][0], cubeT[j][1]))

		idxs.append(nvrt)
		idxs.append(nvrt + 1)
		idxs.append(nvrt + 2)
		idxs.append(nvrt + 2)
		idxs.append(nvrt + 3)
		idxs.append(nvrt)
		nvrt += 4

	return poss, noms, uvs, idxs

def makeBoxFromAABB(min , max):
	cubeV2 = ((min.x, min.y, min.z), (min.x, min.y,  max.z), (max.x, min.y, max.z), (max.x, min.y, min.z),
			  (min.x, max.y, min.z), (min.x, max.y,  max.z), (max.x, max.y, max.z), (max.x, max.y, min.z))
	poss = []
	noms = []
	uvs = []
	idxs = []

	nvrt = 0
	for i in range(6):
		for j in range(4):
			poss.append((cubeV2[cubeF[i][j]][0], cubeV2[cubeF[i][j]][1], cubeV2[cubeF[i][j]][2]))
			noms.append((cubeN[i][0], cubeN[i][1], cubeN[i][2]))
			uvs.append((cubeT[j][0], cubeT[j][1]))

		idxs.append(nvrt)
		idxs.append(nvrt + 1)
		idxs.append(nvrt + 2)
		idxs.append(nvrt + 2)
		idxs.append(nvrt + 3)
		idxs.append(nvrt)
		nvrt += 4

	return poss, noms, uvs, idxs




###################################################################################################
# Cylinder
###################################################################################################
def makeCylinder(radius1:float, radius2:float, length:float, slices:int, stacks:int):

	# Sin/Cos caches
	sinI = []
	cosI = []
	for i in slices:
		angle = 2.0 * math.pi * i / slices
		sinI.append(math.sin(angle))
		cosI.append(math.cos(angle))

	# Compute side normal angle
	deltaRadius = radius2 - radius1
	sideLength = math.sqrt( deltaRadius * deltaRadius + length * length )

	normalXY = 1.0
	if sideLength > 0.00001:
		normalXY =  length / sideLength

	normalZ = 0.0
	if sideLength > 0.00001:
		normalZ = deltaRadius / sideLength

	# Base cap (uSlices + 1)
	fZ = length * -0.5
	radius = radius1

	poss = []
	noms = []
	uvs = []
	idxs = []

	poss.append((0.0, 0.0, fZ))
	noms.append((0.0, 0.0, -1.0))
	uvs.append((0.0, 0.0))

	for i in range(slices):
		poss.append((radius * sinI[i], radius * cosI[i], fZ))
		noms.append((0.0, 0.0, -1.0))
		uvs.append((0.0, 0.0))

	# Stacks ((uStacks + 1)*uSlices)
	for j in range(stacks+1):
		f = j / stacks
		fZ = length * ( f - 0.5 )
		radius = radius1 + f * deltaRadius

		for i in range(slices):
			poss.append((radius * sinI[i], radius * cosI[i], fZ))
			noms.append((normalXY * sinI[i], normalXY * cosI[i], normalZ))
			uvs.append((0.0, 0.0))

	# Top cap (uSlices + 1)
	fZ = length * 0.5
	radius = radius2

	for i in range(slices):
		poss.append((radius * sinI[i], radius * cosI[i], fZ))
		noms.append((0.0, 0.0, 1.0))
		uvs.append((0.0, 0.0))
	poss.append((0.0, 0.0, fZ))
	noms.append((0.0, 0.0, 1.0))
	uvs.append((0.0, 0.0))


	# Generate indices

	# Z+ pole (uSlices)
	rowA = 0
	rowB = 1

	for i in range(slices - 1):
		idxs.append( rowA )
		idxs.append( rowB + i )
		idxs.append( rowB + i + 1 )

	idxs.append( rowA )
	idxs.append( rowB + slices - 1 )
	idxs.append( rowB )

	# Interior stacks (uStacks * uSlices * 2)
	for j in range(stacks):
		rowA = 1 + ( j + 1 ) * slices
		rowB = rowA + slices
		for i in range(slices - 1):
			idxs.append( rowA + i )
			idxs.append( rowB + i )
			idxs.append( rowA + i + 1 )
			idxs.append( rowA + i + 1 )
			idxs.append( rowB + i )
			idxs.append( rowB + i + 1 )

		idxs.append( rowA + slices - 1 )
		idxs.append( rowB + slices - 1 )
		idxs.append( rowA )

		idxs.append( rowA )
		idxs.append( rowB + slices - 1 )
		idxs.append( rowB )

	# Z- pole (uSlices)
	rowA = 1 + ( stacks + 2 ) * slices
	rowB = rowA + slices

	for i in range(slices - 1):
		idxs.append( rowA + i )
		idxs.append( rowB )
		idxs.append( rowA + i + 1 )

	idxs.append( rowA + slices - 1 )
	idxs.append( rowB )
	idxs.append( rowA )

	return poss, noms, uvs, idxs

###################################################################################################
# Sphere
###################################################################################################
def makeSphere(radius:float, slices:int, stacks:int ):

	# Sin/Cos caches
	sinI = []
	cosI = []
	sinJ = []
	cosJ = []

	for i in range(slices):
		angle = 2.0 * math.pi * i / slices
		sinI.append(math.sin(angle))
		cosI.append(math.sin(angle))

	for j in range(stacks):
		angle = math.pi * j / stacks
		sinI.append(math.sin(angle))
		cosI.append(math.sin(angle))

	poss = []
	noms = []
	uvs = []
	idxs = []

	# +Z pole
	poss.append((0.0, 0.0, radius))
	noms.append((0.0, 0.0, 1.0))
	uvs.append((0.0, 0.0))

	# Stacks
	for j in range(stacks):
		for i in range(slices):
			norm = (sinI[i] * sinJ[j], cosI[i] * sinJ[j], cosJ[j])
			poss.append((norm[0] * radius, norm[1] * radius, norm[2] * radius))
			noms.append(norm)
			uvs.append((0.0, 0.0))

	# Z- pole
	poss.append((0.0, 0.0, -radius))
	noms.append((0.0, 0.0, -1.0))
	uvs.append((0.0, 0.0))


	# Generate indices
	# Z+ pole
	rowA = 0
	rowB = 1

	for i in range(slices-1):
		idxs.append( rowA )
		idxs.append( rowB + i + 1 )
		idxs.append( rowB + i )
	idxs.append( rowA )
	idxs.append( rowB )
	idxs.append( rowB + slices-1 )

	# Interior stacks
	for j in range(stacks - 1):
		rowA = 1 + (j - 1) * slices
		rowB = rowA + slices
		for i in range(slices - 1):
			idxs.append(rowA + i)
			idxs.append(rowA + i + 1)
			idxs.append(rowB + i)

			idxs.append(rowA + i + 1)
			idxs.append(rowB + i + 1)
			idxs.append(rowB + i)

		idxs.append(rowA + slices - 1)
		idxs.append(rowA)
		idxs.append(rowB + slices - 1)

		idxs.append(rowA)
		idxs.append(rowB)
		idxs.append(rowB + slices - 1)

	# Z- pole
	rowA = 1 + (stacks - 2) * slices
	rowB = rowA + slices

	for i in range(slices - 1):
		idxs.append(rowA + i)
		idxs.append(rowA + i + 1)
		idxs.append(rowB)

	idxs.append(rowA + slices - 1)
	idxs.append(rowA)
	idxs.append(rowB)

	return poss, noms, uvs, idxs

###################################################################################################
# Torus
###################################################################################################
def makeTorus(innerRadius:float, outerRadius:float, sides:int, rings:int):

	poss = []
	noms = []
	uvs = []
	idxs = []

	# Compute the vertices
	for i in range(rings):
		theta = i * 2.0 * math.pi / rings
		st = math.sin(theta)
		ct = math.cos(theta)
		for j in range(sides):
			phi = j * 2.0 * math.pi / sides
			sp = math.sin(phi)
			cp = math.cos(phi)
			poss.append((ct * ( outerRadius + innerRadius * cp ), -st * ( outerRadius + innerRadius * cp ), sp * innerRadius))
			noms.append((ct * cp, -st * cp, sp))
			uvs.append((0.0, 0.0))

	for i in range(rings - 1):
		for j in range(sides - 1):
			# Tri 1 (Top-Left tri, CCW)
			idxs.append( i * sides + j )
			idxs.append( i * sides + j + 1 )
			idxs.append( ( i + 1 ) * sides + j )

			# Tri 2 (Bottom-Right tri, CCW)
			idxs.append( ( i + 1 ) * sides + j )
			idxs.append( i * sides + j + 1 )
			idxs.append( ( i + 1 ) * sides + j + 1 )

		# Tri 1 (Top-Left tri, CCW)
		idxs.append( i * sides + j )
		idxs.append( i * sides )
		idxs.append( ( i + 1 ) * sides + j )

		# Tri 2 (Bottom-Right tri, CCW)
		idxs.append( ( i + 1 ) * sides + j )
		idxs.append( i * sides + 0 )
		idxs.append( ( i + 1 ) * sides + 0 )

	# join the two ends of the tube
	for j in range(sides - 1):
		# Tri 1 (Top-Left tri, CCW)
		idxs.append( i * sides + j )
		idxs.append( i * sides + j + 1 )
		idxs.append( j )

		# Tri 2 (Bottom-Right tri, CCW)
		idxs.append( j )
		idxs.append( i * sides + j + 1 )
		idxs.append( j + 1 )

	# Tri 1 (Top-Left tri, CCW)
	idxs.append( i * sides + j )
	idxs.append( i * sides )
	idxs.append( j )

	# Tri 2 (Bottom-Right tri, CCW)
	idxs.append( j )
	idxs.append( i * sides )
	idxs.append( 0 )

	return poss, noms, uvs, idxs
