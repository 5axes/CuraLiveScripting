# Sample SetValue
# Get from PrintInformation the Job Name and display in a message
# Get the support_xy_distance  and display the value in a message

from UM.Message import Message
from UM.Settings.SettingInstance import SettingInstance
from cura.CuraApplication import CuraApplication
from UM.Settings.SettingInstance import SettingInstance
from UM.Resources import Resources


global_container_stack = CuraApplication.getInstance().getGlobalContainerStack()
extruder = global_container_stack.extruderList[0]
infill_angles = extruder.getProperty("infill_angles", "value")
Message(text = "infill_angles : {}".format(infill_angles)).show()

extruder.setProperty("infill_angles", "value","[45,0,50,60 ]")

infill_angles = extruder.getProperty("infill_angles", "value")
Message(text = "infill_angles : {}".format(infill_angles)).show()