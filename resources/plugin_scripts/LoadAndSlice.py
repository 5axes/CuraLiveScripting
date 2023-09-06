# LoadAndSlice
# V1.0.0 01/02/2023
# 5@xes
#

import time
from typing import cast

from PyQt6.QtCore import  QTimer

from cura.CuraApplication import CuraApplication
from UM.PluginRegistry import PluginRegistry
from UM.Mesh.MeshWriter import MeshWriter 
from UM.Message import Message

FileName="C:/Temp/Tube.stl"
FileGcode="C:/Temp/Tube.gcode"
	
Me = CuraApplication.getInstance()

# Me.deleteAll()
Me._openFile(FileName)

time.sleep(1)
print("File loaded {}".format(FileName))

Me.backend.forceSlice()
Me.backend.slice()

i=0

_SYNC_INTERVAL = 2.0  # seconds
_update_timer = QTimer()
_update_timer.setInterval(int(_SYNC_INTERVAL * 1000))
_update_timer.setSingleShot(True)
print("_update_timer ! {} s".format(_update_timer.isActive()))
_update_timer.start()

while _update_timer.isActive():
    print("_update_timer ! {} s".format(_update_timer.isActive()))
    if Me.backend._slicing != False:
        _update_timer.stop()
    i+=1
    print("Wait ! {} s".format(i))

gcode_writer = cast(MeshWriter, PluginRegistry.getInstance().getPluginObject("GCodeWriter"))
# Wait for the time to display the result
time.sleep(i)

# open wt Write and text mode
with open(str(FileGcode), "wt") as stream:
    success = gcode_writer.write(stream, None)
print("Save Gcode Ok {} !".format(success))
time.sleep(1)

if success :
    # Don't need to deleteAll As Loading a gcode reset the Model
    Me.deleteAll()
    time.sleep(1)
    Me._openFile(FileGcode)
else:
    Message("Error Gcode generation")

