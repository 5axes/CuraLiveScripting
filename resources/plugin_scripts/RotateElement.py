# Rotate Element
# V1.0.0 01/02/2023
# 5@xes
#

import math
import numpy

from UM.Message import Message
from cura.CuraApplication import CuraApplication
from UM.Mesh.ReadMeshJob import ReadMeshJob
from UM.Scene.Iterator.DepthFirstIterator import DepthFirstIterator
from UM.Math.Matrix import Matrix  
from UM.Math.Vector import Vector  
from UM.Math.Quaternion import Quaternion  
from UM.Mesh.MeshReader import MeshReader  

Me = CuraApplication.getInstance()
# Rotate Around Y to rotate around Z in Cura !!!
rotation = Quaternion.fromAngleAxis(math.radians(90), Vector.Unit_Y)
zero_translation = Matrix(data=numpy.zeros(3, dtype=numpy.float64))

for node in DepthFirstIterator(Me.getController().getScene().getRoot()):
      
      if node.callDecoration("isSliceable"):
        # Rotate but not reset LocalTransformation
        transformation_matrix = node.getLocalTransformation()
        print("Transformation_matrix : \n {}".format(transformation_matrix))
        node.rotate(rotation)
        
        # Reset LocalTransformation
        mesh_data = node.getMeshData()
        transformation_matrix = node.getLocalTransformation()
        print("Transformation_matrix : \n {}".format(transformation_matrix))
        # Apply again the transformation_matrix
        transformation_matrix.setTranslation(zero_translation)
        transformed_mesh = mesh_data.getTransformed(transformation_matrix)
        node.setMeshData(transformed_mesh)

        center = transformed_mesh.getZeroPosition()
        # center = transformed_mesh.getCenterPosition()
        if center is not None:
            print("Center : {}".format(center))
        name = node.getName()
        print("Rotate : {}".format(name))


