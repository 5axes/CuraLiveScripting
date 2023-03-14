# Get info on machine_disallowed_areas
# V1.0.0 01/02/2023
# 5@xes
#

import numpy
import math

from UM.Message import Message
from cura.CuraApplication import CuraApplication
from UM.Math.Polygon import Polygon
from cura.Scene.CuraSceneNode import CuraSceneNode

application=CuraApplication.getInstance()
global_container_stack = application.getGlobalContainerStack()

Tab=global_container_stack.getProperty("machine_disallowed_areas", "value")

# Switch from 
machine_disallowed_areas =  '[]'
if len(Tab) == 0:
    machine_disallowed_areas =  '[[[-117.5, 117.5], [-117.5, 108], [117.5, 108], [117.5, 117.5]],[[-117.5, -108], [-117.5, -117.5], [117.5, -117.5], [117.5, -108]]]'

global_container_stack.setProperty("machine_disallowed_areas", "value", machine_disallowed_areas)

Tab=global_container_stack.getProperty("machine_disallowed_areas", "value")
for area in Tab:
    polygon = Polygon(numpy.array(area, numpy.float32))
    print("Area : {}".format(area))
    print("Polygon : {}".format(polygon))
    
# Need this to updade the scene ?
CuraSceneNode()
