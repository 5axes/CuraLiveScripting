# Sample test_script
# GetProperty  and display the value in a message

from UM.Message import Message
from cura.CuraApplication import CuraApplication

global_container_stack = CuraApplication.getInstance().getGlobalContainerStack()
extruder = global_container_stack.extruderList[0]
retraction_hop_enabled = extruder.getProperty("retraction_hop_enabled", "value")
Message(text = "retraction_hop_enabled : {}".format(retraction_hop_enabled)).show()

