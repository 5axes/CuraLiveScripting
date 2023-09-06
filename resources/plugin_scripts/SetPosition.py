# SetPosition
# Set Position 
# V1.0.0 01/09/2023
# 5@xes
#

import math
import numpy
import trimesh

from cura.CuraApplication import CuraApplication
from cura.Scene.CuraSceneNode import CuraSceneNode
from cura.Scene.SliceableObjectDecorator import SliceableObjectDecorator
from cura.Scene.BuildPlateDecorator import BuildPlateDecorator
from cura.Operations.SetParentOperation import SetParentOperation

from UM.Mesh.ReadMeshJob import ReadMeshJob
from UM.Scene.Iterator.DepthFirstIterator import DepthFirstIterator
from UM.Scene.Iterator.BreadthFirstIterator import BreadthFirstIterator
from UM.Scene.SceneNode import SceneNode
from UM.Scene.Selection import Selection
from UM.Operations.AddSceneNodeOperation import AddSceneNodeOperation
from UM.Operations.GroupedOperation import GroupedOperation
from UM.Operations.RemoveSceneNodeOperation import RemoveSceneNodeOperation
from UM.Math.Matrix import Matrix  
from UM.Math.Vector import Vector  
from UM.Math.Quaternion import Quaternion  
from UM.Mesh.MeshReader import MeshReader
from UM.Mesh.MeshData import MeshData, calculateNormalsFromIndexedVertices 
from UM.Message import Message 


Id =0 
Me = CuraApplication.getInstance()
for node in DepthFirstIterator(Me.getController().getScene().getRoot()):
     if not node.callDecoration("isSliceable"):
             Position = node.getWorldPosition()
             print("Position : {}".format(Position))
             print("name : {}".format(node))
             node.setPosition(Vector((Position.x-10), 0, 0), CuraSceneNode.TransformSpace.World)
