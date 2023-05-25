# Get Mesh Name
# V1.0.0 01/02/2023
# 5@xes
#

from UM.Message import Message
from cura.CuraApplication import CuraApplication
from UM.Mesh.ReadMeshJob import ReadMeshJob
from UM.Scene.Iterator.DepthFirstIterator import DepthFirstIterator

Id = 0
Me = CuraApplication.getInstance()
for node in DepthFirstIterator(Me.getController().getScene().getRoot()):
      if node.callDecoration("isSliceable"):
            mesh_data = node.getMeshData()
            Id +=1
            if mesh_data:
                file_name = mesh_data.getFileName()
                name = node.getName()
                print("{} -> : {}".format(name,file_name))
            model = dict()
            print("WorldTransformation {}".format((node.getWorldTransformation().getData())))
            print("WorldTransformation 3x3 {}".format((node.getWorldTransformation().getData()[0:3, 0:3])))
            print("Transposed {}".format((node.getWorldTransformation().getTransposed().getData())))
            print("LocalTransformation {}".format((node.getLocalTransformation().getData())))


