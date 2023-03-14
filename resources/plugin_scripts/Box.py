# ConvexHull
# Replace a model by his convex_hull
# V1.0.0 01/02/2023
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

# custom function
def toMeshData( tri_node: trimesh.base.Trimesh) -> MeshData:
    # Rotate the part to laydown on the build plate
    # Modification from 5@xes
    tri_node.apply_transform(trimesh.transformations.rotation_matrix(math.radians(90), [-1, 0, 0]))
    tri_faces = tri_node.faces
    tri_vertices = tri_node.vertices

    # Following Source code from  fieldOfView
    indices = []
    vertices = []

    index_count = 0
    face_count = 0
    for tri_face in tri_faces:
        face = []
        for tri_index in tri_face:
            vertices.append(tri_vertices[tri_index])
            face.append(index_count)
            index_count += 1
        indices.append(face)
        face_count += 1

    vertices = numpy.asarray(vertices, dtype=numpy.float32)
    indices = numpy.asarray(indices, dtype=numpy.int32)
    normals = calculateNormalsFromIndexedVertices(vertices, indices, face_count)

    mesh_data = MeshData(vertices=vertices, indices=indices, normals=normals)

    return mesh_data  

def toTriMesh(mesh_data: MeshData) -> trimesh.base.Trimesh:
    vertices = mesh_data.getVertices()
    indices = mesh_data.getIndices()
    if indices is None:
        indices = []
        for face_id in range(0, (int(len(vertices)/3))):
            base_index = face_id * 3
            v_a = base_index#verts[base_index]
            v_b = base_index + 1 #verts[base_index + 1]
            v_c = base_index + 2 #verts[base_index + 2]
            indices.append([v_a, v_b, v_c])

    return trimesh.base.Trimesh(vertices=vertices, faces=indices)

Id =0 
Me = CuraApplication.getInstance()
for node in DepthFirstIterator(Me.getController().getScene().getRoot()):
    if node.callDecoration("isSliceable"):
        mesh_data = node.getMeshData()
        Id +=1
        if mesh_data:
            file_name = mesh_data.getFileName()
            name = node.getName()
            print("{} -> : {}".format(name,file_name))
            toy_mesh = toTriMesh(mesh_data)
            
            node_bounds = node.getBoundingBox()
            exten = [node_bounds.width+10,node_bounds.depth,node_bounds.height+10]
            print("Extends {}".format(exten))
            # print("available_formats {}".format(trimesh.available_formats()))


            # x = trimesh.interfaces.gmsh.load_gmsh("C:/temp/Cube.igs")
            convex = trimesh.convex.convex_hull(toy_mesh)
            convex.apply_transform(trimesh.transformations.rotation_matrix(math.radians(90), [1,0,0]))
            cbox=trimesh.primitives.Box(extents=exten)
            cbox.apply_transform(trimesh.transformations.translation_matrix([0 ,node_bounds.depth*0.5, node_bounds.height*0.5]))
           
            # boolean_sub  = convex.difference(cbox)

            # trimesh.permutate.Permutator(convex)
            print(convex .is_watertight)
            parent = node
            local_transformation = node.getLocalTransformation()
            node = CuraSceneNode()
            node.setSelectable(True)
            node.setName("ConvexHull")
            zero_translation = Matrix(data=numpy.zeros(3, dtype=numpy.float64))
            rotation = Quaternion.fromAngleAxis(math.radians(90), Vector.Unit_X)

            leMesh = toMeshData(convex)
            node.setMeshData(leMesh)


            active_build_plate = Me.getMultiBuildPlateModel().activeBuildPlate
            node.addDecorator(BuildPlateDecorator(active_build_plate))
            node.addDecorator(SliceableObjectDecorator())

            op = GroupedOperation()
            op.addOperation(AddSceneNodeOperation(node, Me.getController().getScene().getRoot()))
            op.addOperation(SetParentOperation(node, parent))   
            Me.getController().getScene().sceneChanged.emit(node) 
            
            node.setTransformation(local_transformation)
           # node.rotate(rotation)
            op.push()            

    

       

      