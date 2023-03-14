# ResetMatrix
# V1.0.0 01/02/2023
# 5@xes
#

import math
import numpy

from UM.Message import Message
from cura.CuraApplication import CuraApplication
from UM.Scene.Iterator.DepthFirstIterator import DepthFirstIterator
from UM.Math.Matrix import Matrix  
from UM.Math.Vector import Vector  
from UM.Math.Quaternion import Quaternion  

Me = CuraApplication.getInstance()
# zero_translation = Matrix(data=numpy.zeros(3, dtype=numpy.float64))

zero_translation = Matrix()                   
                    
for node in DepthFirstIterator(Me.getController().getScene().getRoot()):
      
      if node.callDecoration("isSliceable"):
        # Rotate but not reset LocalTransformation
        transformation_matrix = node.getLocalTransformation()
        print("Transformation_matrix : \n {}".format(transformation_matrix))
        node.setTransformation(zero_translation)
        transformation_matrix = node.getLocalTransformation()
        print("Transformation_matrix : \n {}".format(transformation_matrix))


