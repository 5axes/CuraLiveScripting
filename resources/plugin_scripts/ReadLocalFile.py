# ReadLocalFile
# V1.0.0 01/02/2023
# 5@xes
#

import os

from UM.Message import Message
from cura.CuraApplication import CuraApplication

VERSION_QT5 = False
try:
    from PyQt6.QtCore import QUrl
except ImportError:
    from PyQt5.QtCore import QUrl
    VERSION_QT5 = True

Me = CuraApplication.getInstance()

load_Path = Me.getDefaultPath("dialog_load_path").toLocalFile()
print("Path {}".format(load_Path))

for Nb in range(0,5) :
    Me.readLocalFile(QUrl.fromLocalFile(os.path.join(load_Path,"Tube.stl")))

# Me.selectAll()
Me.arrangeAll()
