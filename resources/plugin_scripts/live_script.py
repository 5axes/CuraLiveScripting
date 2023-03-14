# Set quality
# V1.0.0 01/02/2023
# 5@xes
#


from UM.Message import Message
from cura.CuraApplication import CuraApplication
from cura.Machines.ContainerTree import ContainerTree
from cura.Settings.CuraStackBuilder import CuraStackBuilder
from cura.Settings.ExtruderManager import ExtruderManager
from cura.Settings.ExtruderStack import ExtruderStack
from cura.Settings.GlobalStack import GlobalStack
from cura.Settings.IntentManager import IntentManager
from cura.Settings.CuraContainerStack import _ContainerIndexes
from UM.Settings.ContainerRegistry import ContainerRegistry

Me = CuraApplication.getInstance()
# zero_translation = Matrix(data=numpy.zeros(3, dtype=numpy.float64))

machine_manager =Me.getMachineManager()
container_tree = ContainerTree.getInstance()
global_stack = Me.getGlobalContainerStack()
machine_id=global_stack.quality.getMetaData().get('definition', '') 
containers = ContainerRegistry.getInstance().findInstanceContainers(definition = machine_id, type='quality_changes')

# for container in containers :
#      print("container {}".format(container))

container = containers[2]
print("container {}".format(container))

global_stack = Me.getGlobalContainerStack()
activeQualityType = global_stack.quality.getMetaDataEntry("quality_type")
print("activeQualityType {}".format(activeQualityType))
aQT = ContainerTree.getInstance().getCurrentQualityGroups().get(activeQualityType)
print("activeQualityType {}".format(aQT))

# machine_manager.setQualityChangesGroup(aQT)