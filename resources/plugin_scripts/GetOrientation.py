# GetOrientation
# V1.0.0 01/02/2023
# 5@xes
#

import math
import numpy
import trimesh

from UM.Message import Message
from cura.CuraApplication import CuraApplication
from UM.Mesh.ReadMeshJob import ReadMeshJob
from UM.Scene.Iterator.DepthFirstIterator import DepthFirstIterator
from UM.Math.Matrix import Matrix  
from UM.Math.Vector import Vector  
from UM.Math.Quaternion import Quaternion  
from UM.Mesh.MeshReader import MeshReader  

def _unit_vector(vector):
   """ Returns the unit vector of the vector.  """
   return vector / numpy.linalg.norm(vector)


Me = CuraApplication.getInstance()
# Rotate Around Y to rotate around Z in Cura !!!
rotation = Quaternion.fromAngleAxis(math.radians(90), Vector.Unit_Y)
zero_translation = Matrix(data=numpy.zeros(3, dtype=numpy.float64))

for node in DepthFirstIterator(Me.getController().getScene().getRoot()):
      
      if node.callDecoration("isSliceable"):
        hull_polygon = node.callDecoration("_compute2DConvexHull")
        points=hull_polygon.getPoints()
        # Get the Rotation Matrix     
        print("Points : \n{}".format(points))                  
        transform, rectangle = trimesh.bounds.oriented_bounds_2D(points)
        print("transform : \n{}".format(transform))     
       
        t = Matrix()
        Vect = transform[0]
        Vect[2] = 0
        t.setColumn(0,Vect)
        Vect = transform[1]
        Vect[2] = 0
        t.setColumn(1,Vect)
        #t.setColumn(2,Vect)

        t = Matrix()
        print("local_transformation : \n{}".format(node.getLocalTransformation())) 

        Vect = [transform[1][1],0,transform[0][1]]
        t.setColumn(0,Vect)
        Vect = [0,1,0]
        t.setColumn(1,Vect)
        Vect = [transform[1][0],0,transform[0][0]]
        t.setColumn(2,Vect)
        print("Result T : \n{}".format(t))  

        local_transformation = Matrix()
        local_transformation.multiply(t)
        print("local_transformation : \n{}".format(node.getLocalTransformation())) 
        local_transformation.multiply(node.getLocalTransformation())
        node.setTransformation(local_transformation) 

    

       

      