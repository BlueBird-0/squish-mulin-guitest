# encoding: UTF-8

from objectmaphelper import *

recoveryDialog = {"name": "MvRecoverProjectDialog", "type": "MinervaD::MvRecoverProjectDialog", "visible": 1}
recoveryDialog_Close = {"name": "btnClose", "type": "QPushButton", "visible": 1, "window": recoveryDialog}

mainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "visible": 1, "windowTitle": "MuLiN Creator"}
menuBar = {"type": "QMenuBar", "unnamed": 1, "visible": 1, "window": mainWindow}
fileMenu = {"title": "파일", "type": "QMenu", "unnamed": 1, "visible": 1, "window": mainWindow}

openFileDialog = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
openFileDialog_splitter = {"name": "splitter", "type": "QSplitter", "visible": 1, "window": openFileDialog}
openFileDialog_frame = {"container": openFileDialog_splitter, "name": "frame", "type": "QFrame", "visible": 1}
openFileDialog_stack = {"container": openFileDialog_frame, "name": "stackedWidget", "type": "QStackedWidget", "visible": 1}
openFileDialog_treeView = {"container": openFileDialog_stack, "name": "treeView", "type": "QTreeView", "visible": 1}

# projectMainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "visible": 1, "windowTitle": "MuLiN Creator - C:/Users/DELL/Desktop/MuLiN PLC 비교/MuLiN 명령어 테스트 케이스/MuLiN 명령어 테스트 케이스.mdp"}
projectMainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "visible": 1, "windowTitle": "MuLiN Creator - C:/Users/User/Desktop/MuLiN PLC 비교/MuLiN 명령어 테스트 케이스/MuLiN 명령어 테스트 케이스.mdp"}

qFileDialog_Open_QPushButton = {"text": "Open", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": openFileDialog}  # 열기
qFileDialog_fileNameLabel_QLabel = {"name": "fileNameLabel", "type": "QLabel", "visible": 1, "window": openFileDialog}
fileNameEdit_QLineEdit = {"buddy": qFileDialog_fileNameLabel_QLabel, "name": "fileNameEdit", "type": "QLineEdit", "visible": 1}  # 입력창


muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_Qtitan_ToolButton = {"text": "연결", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": projectMainWindow}
muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_Qtitan_ToolButton_2 = {"text": "다운로드", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": projectMainWindow}
mvDownloadToDeviceDialog_MinervaD_MvDownloadToDeviceDialog = {"name": "MvDownloadToDeviceDialog", "type": "MinervaD::MvDownloadToDeviceDialog", "visible": 1}
mvDownloadToDeviceDialog_QPushButton = {"text": "확인", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mvDownloadToDeviceDialog_MinervaD_MvDownloadToDeviceDialog}
o_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "장치에 다운로드"}
o_QPushButton = {"text": "실행 중지", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": o_QMessageBox}
muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_Qtitan_ToolButton_3 = {"text": "모니터링", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": projectMainWindow}




muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_LadderEditorWidget_MinervaD_MvLadderEditorWidget = {"name": "LadderEditorWidget", "type": "MinervaD::MvLadderEditorWidget", "visible": 1, "window": projectMainWindow}
ladderEditorWidget_splitter_QSplitter = {"container": muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_LadderEditorWidget_MinervaD_MvLadderEditorWidget, "name": "splitter", "type": "QSplitter", "visible": 1}
splitter_LadderView_MinervaD_MvLadderViewFrame = {"container": ladderEditorWidget_splitter_QSplitter, "name": "LadderView", "type": "MinervaD::MvLadderViewFrame", "visible": 1}
ladderView_QGraphicsItem = {"acceptDrops": "yes", "container": splitter_LadderView_MinervaD_MvLadderViewFrame, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "occurrence": 5, "selectable": "yes", "type": "QGraphicsItem", "userType": 1, "visible": "yes"}
o_h3_b_font_color_darkorange_Function_Block_Arithmetic_font_b_h3_br_OUT_PASS_BOOL_QGraphicsItem = {"acceptDrops": "no", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "toolTip": "<h3><b><font color='darkorange'>Function Block : Arithmetic</font></b></h3>매개 변수 :<br>    [OUT] PASS : BOOL", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox = {"container": muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_LadderEditorWidget_MinervaD_MvLadderEditorWidget, "name": "selectFBInstanceCheckBox", "type": "QCheckBox", "visible": 1}
ladderEditorWidget_groupBox_QGroupBox = {"container": muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_LadderEditorWidget_MinervaD_MvLadderEditorWidget, "name": "groupBox", "type": "QGroupBox", "visible": 1}
groupBox_listWidget_QListWidget = {"container": ladderEditorWidget_groupBox_QGroupBox, "name": "listWidget", "type": "QListWidget", "visible": 1}
ladderEditorWidget_QPushButton = {"container": muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_LadderEditorWidget_MinervaD_MvLadderEditorWidget, "text": "확인", "type": "QPushButton", "unnamed": 1, "visible": 1}
splitter_VariableTableFrame_MinervaD_MvVariableTableFrame = {"container": ladderEditorWidget_splitter_QSplitter, "name": "VariableTableFrame", "type": "MinervaD::MvVariableTableFrame", "visible": 1}
variableTableFrame_treeView_MinervaD_MvCustomTreeView = {"container": splitter_VariableTableFrame_MinervaD_MvVariableTableFrame, "name": "treeView", "type": "MinervaD::MvCustomTreeView", "visible": 1}
ladderView_QGraphicsItem_2 = {"acceptDrops": "yes", "container": splitter_LadderView_MinervaD_MvLadderViewFrame, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "occurrence": 7, "selectable": "yes", "type": "QGraphicsItem", "userType": 1, "visible": "yes"}
o_h3_b_font_color_darkorange_Function_Block_Arithmetic_font_b_h3_br_OUT_PASS_BOOL_QGraphicsItem_2 = {"acceptDrops": "no", "container": ladderView_QGraphicsItem_2, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "toolTip": "<h3><b><font color='darkorange'>Function Block : Arithmetic</font></b></h3>매개 변수 :<br>    [OUT] PASS : BOOL", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_MvProjectTreeFrame_MinervaD_MvProjectTreeFrame = {"name": "MvProjectTreeFrame", "type": "MinervaD::MvProjectTreeFrame", "visible": 1, "window": projectMainWindow}
mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget = {"container": muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_MvProjectTreeFrame_MinervaD_MvProjectTreeFrame, "name": "treeWidget", "type": "MinervaD::MvProjectTreeWidget", "visible": 1}



ADD_OUT = {"column": 5, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "text": 35, "type": "QModelIndex"}
SUB_OUT = {"column": 5, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "text": "55.5", "type": "QModelIndex"}
MUL_OUT = {"column": 5, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "text": 111, "type": "QModelIndex"}
DIV_OUT = {"column": 5, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "text": 37, "type": "QModelIndex"}
MOD_OUT = {"column": 5, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "text": 5, "type": "QModelIndex"}
EXPT_OUT = {"column": 5, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "text": 32, "type": "QModelIndex"}
PASS = {"column": 5, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "text": "TRUE", "type": "QModelIndex"}
treeView_QScrollBar = {"container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "type": "QScrollBar", "unnamed": 1, "visible": 1}
mvSelectMonitoringFunctionBlockDialog_MinervaD_MvSelectMonitoringFunctionBlockDialog = {"name": "MvSelectMonitoringFunctionBlockDialog", "occurrence": 2, "type": "MinervaD::MvSelectMonitoringFunctionBlockDialog", "visible": 1}
treeView_QModelIndex = {"column": 4, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "occurrence": 2, "text": "", "type": "QModelIndex"}


muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_Monitoring_Qtitan_ToolButton = {"text": "Monitoring", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": projectMainWindow}
