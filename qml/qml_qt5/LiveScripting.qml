// Copyright (c) 2015 Ultimaker B.V.
// All Modification after 2023 5@xes
// LiveScripting is released under the terms of the AGPLv3 or higher.
// proterties values
//   "ScriptPath" : Path to script
//   "Script"	: Script Code
//   "Result"	: Log of the Run Script
//   "AutoRun"   : AutoRun

import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.11
import QtQuick.Dialogs 1.0

import UM 1.1 as UM
import Cura 1.0 as Cura

Item
{
	id: base

	function pathToUrl(path)
	{
		// Convert the path to a usable url
		var url = "file:///"
		url = url + path
		// Not sure of this last encode
		// url = encodeURIComponent(url)
		
		// Return the resulting url
		return url
	}
	
	function urlToStringPath(url)
	{
		// Convert the url to a usable string path
		var path = url.toString()
		path = path.replace(/^(file:\/{3})|(qrc:\/{2})|(http:\/{2})/, "")
		path = decodeURIComponent(path)

		// On Linux, a forward slash needs to be prepended to the resulting path
		// I'm guessing this is needed on Mac OS, as well, but can't test it
		if (Cura.os == "linux" || Cura.os == "darwin") path = "/" + path
		
		// Return the resulting path
		return path
	}
			
	property variant catalog: UM.I18nCatalog { name: "livescripting" }
	
	
	// TODO: these widths & heights are a bit too dependant on other objects in the qml...
	width: 600
	height: 600
	TextArea {
		id: inputfg
		width: parent.width
		anchors.top: parent.top
		anchors.bottom: runOptions.top

		font.family: "Courier New"
		wrapMode: TextEdit.NoWrap
		textFormat: TextEdit.PlainText
		text: UM.ActiveTool.properties.getValue("Script")
		onTextChanged: {
			UM.ActiveTool.setProperty("Script", text)
		}
		Keys.onPressed: {
			if (event.key == Qt.Key_Tab) {
				insert(cursorPosition, "	");
				event.accepted = true;
			}
		}
	}
	Row {
		id: runOptions
		width: childrenRect.width
		height: childrenRect.height
		anchors.bottom: result.top
		
		spacing: Math.round(UM.Theme.getSize("default_margin").width / 2)

		Button {
			text: catalog.i18nc("@label","Run")
			onClicked: {
				UM.ActiveTool.triggerAction("runScript")
			}
		}
		Button {
			text: catalog.i18nc("@label","Save")
			onClicked: {
				UM.ActiveTool.triggerAction("saveCode")
			}
		}	
		Button {
			text: catalog.i18nc("@label","Open File")
			onClicked: fileDialog.open()
		}

		FileDialog
		{
			id: fileDialog
			onAccepted: UM.ActiveTool.setProperty("ScriptPath", urlToStringPath(fileUrl))
			// fileUrl QT5 !
			nameFilters: "*.py"
			// folder: CuraApplication.getDefaultPath("dialog_load_path")
			folder: pathToUrl(UM.ActiveTool.properties.getValue("ScriptFolder"))
		}

		Button {
			text: catalog.i18nc("@label","Save As")
			onClicked: fileDialogSave.open()
		}

		FileDialog
		{
			id: fileDialogSave
			// fileUrl QT5 !
			onAccepted: UM.ActiveTool.setProperty("ScriptFolder", urlToStringPath(selectedFile))
			nameFilters: "*.py"
			selectExisting : false
			folder:pathToUrl(UM.ActiveTool.properties.getValue("ScriptFolder"))		
		}
		
		CheckBox {
			text: catalog.i18nc("@option:check","Auto run")
			checked: UM.ActiveTool.properties.getValue("AutoRun")
			onClicked: {
				UM.ActiveTool.setProperty("AutoRun", checked)
			}
		}		
	}
	TextArea {
		id: result
		anchors.bottom: parent.bottom
		width: parent.width
		height: 150
		readOnly: true
		wrapMode: TextEdit.NoWrap
		textFormat: TextEdit.PlainText
		font.family: "Courier New"
		text: UM.ActiveTool.properties.getValue("Result")
		Keys.onPressed: {
			if (event.key == Qt.Key_Delete) {
				UM.ActiveTool.setProperty("Result", "");
				event.accepted = true;
			}
		}
	}
}
