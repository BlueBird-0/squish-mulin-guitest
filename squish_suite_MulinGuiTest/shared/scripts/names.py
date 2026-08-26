# encoding: UTF-8

from objectmaphelper import *

muLiN_Creator_MinervaD_MvMainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "windowTitle": "MuLiN Creator"}

muLiN_Creator_QMenu = {"title": "파일", "type": "QMenu", "unnamed": 1, "visible": 0, "window": muLiN_Creator_MinervaD_MvMainWindow}
o_QAction_menu_file = {"container": muLiN_Creator_QMenu, "text": "파일", "type": "QAction", "unnamed": 1, "visible": True}
o_QAction_menu_openProject = {"container": muLiN_Creator_QMenu, "text": "프로젝트 열기", "type": "QAction", "unnamed": 1, "visible": True}
qFileDialog_QFileDialog = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
qFileDialog_splitter_QSplitter = {"name": "splitter", "type": "QSplitter", "visible": 1, "window": qFileDialog_QFileDialog}
splitter_frame_QFrame = {"container": qFileDialog_splitter_QSplitter, "name": "frame", "type": "QFrame", "visible": 1}
frame_stackedWidget_QStackedWidget = {"container": splitter_frame_QFrame, "name": "stackedWidget", "type": "QStackedWidget", "visible": 1}
stackedWidget_treeView_QTreeView = {"container": frame_stackedWidget_QStackedWidget, "name": "treeView", "type": "QTreeView", "visible": 1}

treeView_testProjectFolders = {"column": 0, "container": stackedWidget_treeView_QTreeView, "type": "QModelIndex"}
treeView_project_mdps = {"column": 0, "container": stackedWidget_treeView_QTreeView, "type": "QModelIndex"}

muLiN_Creator_QMenu_2 = {"type": "QMenu", "unnamed": 1, "visible": 0, "window": muLiN_Creator_MinervaD_MvMainWindow}
qFileDialog_Open_QPushButton = {"text": "Open", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": qFileDialog_QFileDialog}
mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog = {"name": "MvRecoverProjectDialog", "type": "MinervaD::MvRecoverProjectDialog", "visible": 1}
muLiN_Creator_QMenuBar = {"type": "QMenuBar", "unnamed": 1, "visible": 1, "window": muLiN_Creator_MinervaD_MvMainWindow}
muLiN_Creator_QMenu_3 = {"title": "파일", "type": "QMenu", "unnamed": 1, "visible": 1, "window": muLiN_Creator_MinervaD_MvMainWindow}
mvRecoverProjectDialog_btnClose_QPushButton = {"name": "btnClose", "type": "QPushButton", "visible": 1, "window": mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog}
muLiN_Creator_Documents_mdp_MinervaD_MvMainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "visible": 1}
muLiN_Creator_Documents_mdp_QMenuBar = {"type": "QMenuBar", "unnamed": 1, "visible": 1, "window": muLiN_Creator_Documents_mdp_MinervaD_MvMainWindow}
muLiN_Creator_Documents_mdp_QMenu = {"title": "프로젝트", "type": "QMenu", "unnamed": 1, "visible": 1, "window": muLiN_Creator_Documents_mdp_MinervaD_MvMainWindow}
MinervaD_MvMainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "visible": 1}
o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MvMessageFrame_MinervaD_MvMessageFrame = {"name": "MvMessageFrame", "type": "MinervaD::MvMessageFrame", "visible": 1, "window": MinervaD_MvMainWindow}
mvMessageFrame_qt_tabwidget_stackedwidget_QStackedWidget_2 = {"container": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MvMessageFrame_MinervaD_MvMessageFrame, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
qt_tabwidget_stackedwidget_tabBuild_QWidget_2 = {"container": mvMessageFrame_qt_tabwidget_stackedwidget_QStackedWidget_2, "name": "tabBuild", "type": "QWidget", "visible": 1}
tabBuild_btnError_QToolButton_2 = {"container": qt_tabwidget_stackedwidget_tabBuild_QWidget_2, "name": "btnError", "type": "QToolButton", "visible": 1}
o_Qtitan_ToolButton = {"text": "연결", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
o_Qtitan_ToolButton_2 = {"text": "다운로드", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
mvDownloadToDeviceDialog_MinervaD_MvDownloadToDeviceDialog = {"name": "MvDownloadToDeviceDialog", "type": "MinervaD::MvDownloadToDeviceDialog", "visible": 1}
mvDownloadToDeviceDialog_QPushButton = {"text": "확인", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mvDownloadToDeviceDialog_MinervaD_MvDownloadToDeviceDialog}
o_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "장치에 다운로드"}
o_QPushButton = {"text": "실행 중지", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": o_QMessageBox}
o_Qtitan_ToolButton_3 = {"text": "모니터링 시작", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
mvProjectTreeFrame_MinervaD_MvProjectTreeFrame = {"name": "MvProjectTreeFrame", "type": "MinervaD::MvProjectTreeFrame", "visible": 1, "window": MinervaD_MvMainWindow}
ladderEditorWidget_MinervaD_MvLadderEditorWidget = {"name": "LadderEditorWidget", "type": "MinervaD::MvLadderEditorWidget", "visible": 1, "window": MinervaD_MvMainWindow}
ladderEditorWidget_splitter_QSplitter = {"container": ladderEditorWidget_MinervaD_MvLadderEditorWidget, "name": "splitter", "type": "QSplitter", "visible": 1}
MinervaD_MvLadderViewFrame = {"container": ladderEditorWidget_splitter_QSplitter, "name": "LadderView", "type": "MinervaD::MvLadderViewFrame", "visible": 1}
ladderView_QGraphicsItem = {"acceptDrops": "yes", "container": MinervaD_MvLadderViewFrame, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 1, "visible": "yes"}
o_QGraphicsItem = {"acceptDrops": "no", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
o_QGraphicsItem_2 = {"acceptDrops": "no", "container": o_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
o_h2_b_font_color_blue_font_b_h2_b_30_b_br_QGraphicsItem = {"acceptDrops": "no", "container": o_QGraphicsItem_2, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 19, "visible": "yes"}
o_QGraphicsItem_ADD = {"acceptDrops": "no", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "toolTip": "<h3><b><font color='blue'>Function : ADD</font></b></h3><b>입력들의 합을 계산 후 OUT에 출력합니다.</b><br><br>매개 변수 :<br>    [IN] IN1 : ANY_NUM<br>    [IN] IN2 : ANY_NUM<br>    [OUT] OUT : ANY_NUM", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
o_h3_b_font_color_blue_Function_ADD_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem = {"acceptDrops": "no", "container": o_QGraphicsItem_ADD, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
ladderView_QScrollBar = {"container": MinervaD_MvLadderViewFrame, "type": "QScrollBar", "unnamed": 1, "visible": 1}
ladderView_QGraphicsItem_2 = {"acceptDrops": "yes", "container": MinervaD_MvLadderViewFrame, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 1, "visible": "yes"}
o_h3_b_font_color_blue_Function_SUB_font_b_h3_b_IN1_IN2_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem = {"acceptDrops": "no", "container": ladderView_QGraphicsItem_2, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "toolTip": "<h3><b><font color='blue'>Function : SUB</font></b></h3><b>IN1에서 IN2를 뺄샘 후 OUT에 출력합니다.</b><br><br>매개 변수 :<br>    [IN] IN1 : ANY_NUM<br>    [IN] IN2 : ANY_NUM<br>    [OUT] OUT : ANY_NUM", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
o_h3_b_font_color_blue_Function_SUB_font_b_h3_b_IN1_IN2_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem_2 = {"acceptDrops": "no", "container": o_h3_b_font_color_blue_Function_SUB_font_b_h3_b_IN1_IN2_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
o_h2_b_font_color_blue_font_b_h2_b_7_b_br_QGraphicsItem = {"acceptDrops": "no", "container": o_h3_b_font_color_blue_Function_SUB_font_b_h3_b_IN1_IN2_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem_2, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "toolTip": "<h2><b><font color='blue'>모니터링 데이터</font></b></h2><b>  '7'</b><br>", "type": "QGraphicsItem", "userType": 19, "visible": "yes"}
o_h3_b_font_color_blue_Function_ADD_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem_2 = {"acceptDrops": "no", "container": o_QGraphicsItem_ADD, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
ladderView_QGraphicsItem_3 = {"acceptDrops": "yes", "container": MinervaD_MvLadderViewFrame, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 1, "visible": "yes"}
o_h3_b_font_color_blue_Function_MUL_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem = {"acceptDrops": "no", "container": ladderView_QGraphicsItem_3, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "toolTip": "<h3><b><font color='blue'>Function : MUL</font></b></h3><b>입력들의 곱을 계산 후 OUT에 출력합니다.</b><br><br>매개 변수 :<br>    [IN] IN1 : ANY_NUM<br>    [IN] IN2 : ANY_NUM<br>    [OUT] OUT : ANY_NUM", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
o_h3_b_font_color_blue_Function_MUL_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem_2 = {"acceptDrops": "no", "container": o_h3_b_font_color_blue_Function_MUL_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}

# ADD 함수 블록 부모
parent_ADD_Block = {
    "type": "QGraphicsItem",
    "toolTip": Wildcard("*Function_ADD*"),
    "acceptDrops":"yes"
}

# SUB 함수 블록 부모
parent_SUB_Block = {
    "type": "QGraphicsItem",
    "toolTip": Wildcard("*Function_SUB*"),
    "acceptDrops":"yes"
}

# MUL 함수 블록 부모
parent_MUL_Block = {
    "type": "QGraphicsItem",
    "toolTip": Wildcard("*Function_MUL*"),
    "acceptDrops":"yes"
}

monitoring_data_ADD_QGraphicsItem = {
    "type": "QGraphicsItem",
    "container": parent_ADD_Block,
    "userType": 19,
    "toolTip": Wildcard("*모니터링 데이터*")
}

# [SUB 블록의 모니터링 데이터 객체]
monitoring_data_SUB_QGraphicsItem = {
    "type": "QGraphicsItem",
    "container": parent_SUB_Block,
    "userType": 19,
    "toolTip": Wildcard("*모니터링 데이터*")
}

# [MUL 블록의 모니터링 데이터 객체]
monitoring_data_MUL_QGraphicsItem = {
    "type": "QGraphicsItem",
    "container": parent_MUL_Block,
    "userType": 19,
    "toolTip": Wildcard("*모니터링 데이터*")
}
o_QMenu = {"title": "최근 프로젝트들", "type": "QMenu", "unnamed": 1, "visible": 1, "window": muLiN_Creator_QMenu_3}
mvRecoverProjectDialog_tbRecoveryList_QTableWidget = {"name": "tbRecoveryList", "type": "QTableWidget", "visible": 1, "window": mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog}
tbRecoveryList_QPushButton = {"container": mvRecoverProjectDialog_tbRecoveryList_QTableWidget, "text": "복구", "type": "QPushButton", "unnamed": 1, "visible": 1}
o_QMessageBox_2 = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "프로젝트 복구"}
mvNewProjectDialog_MinervaD_MvNewProjectDialog = {"name": "MvNewProjectDialog", "type": "MinervaD::MvNewProjectDialog", "visible": 1}
mvNewProjectDialog_btnNext_QPushButton = {"name": "btnNext", "type": "QPushButton", "visible": 1, "window": mvNewProjectDialog_MinervaD_MvNewProjectDialog}
mvNewProjectDialog_qt_tabwidget_stackedwidget_QStackedWidget = {"name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1, "window": mvNewProjectDialog_MinervaD_MvNewProjectDialog}
qt_tabwidget_stackedwidget_tab_1_QWidget = {"container": mvNewProjectDialog_qt_tabwidget_stackedwidget_QStackedWidget, "name": "tab_1", "type": "QWidget", "visible": 1}
tab_1_edProjectName_MinervaD_MvLineEditor = {"container": qt_tabwidget_stackedwidget_tab_1_QWidget, "name": "edProjectName", "type": "MinervaD::MvLineEditor", "visible": 1}
o_QMenu_2 = {"type": "QMenu", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
mvProjectTreeFrame_OK_QPushButton = {"container": mvProjectTreeFrame_MinervaD_MvProjectTreeFrame, "text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1}
splitter_VariableTableFrame_MinervaD_MvVariableTableFrame = {"container": ladderEditorWidget_splitter_QSplitter, "name": "VariableTableFrame", "type": "MinervaD::MvVariableTableFrame", "visible": 1}
variableTableFrame_pushButtonRowsNew_QPushButton = {"container": splitter_VariableTableFrame_MinervaD_MvVariableTableFrame, "name": "pushButtonRowsNew", "type": "QPushButton", "visible": 1}
variableTableFrame_treeView_MinervaD_MvCustomTreeView = {"container": splitter_VariableTableFrame_MinervaD_MvVariableTableFrame, "name": "treeView", "type": "MinervaD::MvCustomTreeView", "visible": 1}
treeView_MinervaD_MvLineEditor = {"columnIndex": 2, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "rowIndex": 0, "type": "MinervaD::MvLineEditor", "unnamed": 1, "visible": 1}
treeView_MinervaD_MvLineEditor_2 = {"columnIndex": 2, "container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "rowIndex": 1, "type": "MinervaD::MvLineEditor", "unnamed": 1, "visible": 1}
o_font_color_red_Errors_br_WMD02005_font_QGraphicsItem = {"container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "toolTip": "<font color='red'>Errors :<br>[WMD02005] 완성되지 않은 로직이 있습니다.</font>", "type": "QGraphicsItem", "userType": 9, "visible": "yes"}
o_font_color_red_Errors_br_WMD02005_font_QGraphicsItem_2 = {"container": o_font_color_red_Errors_br_WMD02005_font_QGraphicsItem, "enabled": "yes", "focusable": "yes", "type": "QGraphicsItem", "userType": 2, "visible": "yes"}
o_QGraphicsItem_3 = {"acceptDrops": "no", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 3, "visible": "yes"}
o_QGraphicsItem_4 = {"acceptDrops": "no", "container": o_QGraphicsItem_3, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 11, "visible": "yes"}
ladderView_MvDataEditor_MinervaD_MvDataEditor = {"container": MinervaD_MvLadderViewFrame, "name": "MvDataEditor", "type": "MinervaD::MvDataEditor", "visible": 1}
mvDataEditor_mvSpinBox_MinervaD_MvSpinLineEdit = {"container": ladderView_MvDataEditor_MinervaD_MvDataEditor, "name": "mvSpinBox", "type": "MinervaD::MvSpinLineEdit", "visible": 1}
o_QTableView = {"type": "QTableView", "unnamed": 1, "visible": 1}
o_QGraphicsItem_5 = {"acceptDrops": "yes", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 9, "visible": "yes"}
o_QGraphicsItem_6 = {"acceptDrops": "yes", "container": o_QGraphicsItem_5, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 2, "visible": "yes"}
mvAddToTableDialog_MinervaD_MvAddToTableDialog = {"name": "MvAddToTableDialog", "type": "MinervaD::MvAddToTableDialog", "visible": 1}
mvAddToTableDialog_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mvAddToTableDialog_MinervaD_MvAddToTableDialog}
mvNewVariableDialog_MinervaD_MvNewVariableDialog = {"name": "MvNewVariableDialog", "type": "MinervaD::MvNewVariableDialog", "visible": 1}
mvNewVariableDialog_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mvNewVariableDialog_MinervaD_MvNewVariableDialog}
o_QGraphicsItem_7 = {"acceptDrops": "yes", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 9, "visible": "yes"}
o_QGraphicsItem_8 = {"acceptDrops": "no", "container": o_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 16, "visible": "yes"}
ladderView_MvBoxTypeEditor_MinervaD_MvBoxNameEditor = {"container": MinervaD_MvLadderViewFrame, "name": "MvBoxTypeEditor", "type": "MinervaD::MvBoxNameEditor", "visible": 1}
mvBoxTypeEditor_mvSpinBox_MinervaD_MvSpinLineEdit = {"container": ladderView_MvBoxTypeEditor_MinervaD_MvBoxNameEditor, "name": "mvSpinBox", "type": "MinervaD::MvSpinLineEdit", "visible": 1}
o_QGraphicsItem_9 = {"acceptDrops": "no", "container": o_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
o_QGraphicsItem_10 = {"acceptDrops": "no", "container": o_QGraphicsItem_9, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 11, "visible": "yes"}
o_QGraphicsItem_11 = {"acceptDrops": "no", "container": o_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
o_QGraphicsItem_12 = {"acceptDrops": "no", "container": o_QGraphicsItem_11, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 11, "visible": "yes"}
o_QGraphicsItem_13 = {"acceptDrops": "no", "container": o_QGraphicsItem_2, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 11, "visible": "yes"}
networkGraphicsItem = {"type": "65538", "userType": "2", "visible":"true"}

tbRecoveryList_QPushButton_2 = {"container": mvRecoverProjectDialog_tbRecoveryList_QTableWidget, "text": "복구", "type": "QPushButton", "unnamed": 1, "visible": 1}
o_Yes_QPushButton = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": o_QMessageBox_2}
o_Close_QPushButton = {"text": "Close", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": o_QMessageBox_2}
o_font_color_red_Errors_br_WMD02005_font_QGraphicsItem_3 = {"acceptDrops": "yes", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "toolTip": "<font color='red'>Errors :<br>[WMD02005] 완성되지 않은 로직이 있습니다.</font>", "type": "QGraphicsItem", "userType": 9, "visible": "yes"}
o_font_color_red_Errors_br_WMD02005_font_QGraphicsItem_4 = {"acceptDrops": "yes", "container": o_font_color_red_Errors_br_WMD02005_font_QGraphicsItem_3, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 2, "visible": "yes"}
o_font_color_0000ff_Warnings_br_WMD02005_font_QGraphicsItem = {"acceptDrops": "yes", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "toolTip": "<font color='#0000ff'>Warnings :<br>[WMD02005] 완성되지 않은 로직이 있습니다.</font>", "type": "QGraphicsItem", "userType": 9, "visible": "yes"}

ladderView = {"container": ladderEditorWidget_splitter_QSplitter, "name": "viewWidget", "type": "QWidget", "visible": 1}

barLeft_Qtitan_DockBarSite = {"name": "BarLeft", "type": "Qtitan::DockBarSite", "visible": 1, "window": MinervaD_MvMainWindow}
barLeft_QStatusBar = {"aboveWidget": barLeft_Qtitan_DockBarSite, "type": "QStatusBar", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
mvMessageFrame_tabWidget_QTabWidget = {"container": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MvMessageFrame_MinervaD_MvMessageFrame, "name": "tabWidget", "type": "QTabWidget", "visible": 1}
tabBuild_tbBuildErrors_QTableWidget = {"container": qt_tabwidget_stackedwidget_tabBuild_QWidget_2, "name": "tbBuildErrors", "type": "QTableWidget", "visible": 1}
tbBuildErrors_qt_tableview_cornerbutton_QTableCornerButton = {"container": tabBuild_tbBuildErrors_QTableWidget, "name": "qt_tableview_cornerbutton", "type": "QTableCornerButton", "visible": 1}
tbBuildErrors_qt_tableview_cornerbutton_QHeaderView = {"container": tabBuild_tbBuildErrors_QTableWidget, "leftWidget": tbBuildErrors_qt_tableview_cornerbutton_QTableCornerButton, "orientation": 1, "type": "QHeaderView", "unnamed": 1, "visible": 1}
o_Qtitan_DockTitleBar = {"type": "Qtitan::DockTitleBar", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
o_Qtitan_DockPanelSplitter = {"type": "Qtitan::DockPanelSplitter", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
o_Qtitan_DockDocumentLayoutPanel = {"type": "Qtitan::DockDocumentLayoutPanel", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
o_Qtitan_DockPanelSplitter_2 = {"type": "Qtitan::DockPanelSplitter", "unnamed": 1, "visible": 1, "window": MinervaD_MvMainWindow}
mvAddPouDialog_MinervaD_MvAddPouDialog = {"name": "MvAddPouDialog", "type": "MinervaD::MvAddPouDialog", "visible": 0}
mvAddPouDialog_MinervaD_MvAddPouDialog_2 = {"name": "MvAddPouDialog", "type": "MinervaD::MvAddPouDialog", "visible": 1}
mvProjectTreeFrame_teDescription_MinervaD_MvPlainTextEditor = {"container": mvProjectTreeFrame_MinervaD_MvProjectTreeFrame, "name": "teDescription", "type": "MinervaD::MvPlainTextEditor", "visible": 1}
splitter_MvNetworkControlFrame_MinervaD_MvNetworkControlFrame = {"container": ladderEditorWidget_splitter_QSplitter, "name": "MvNetworkControlFrame", "type": "MinervaD::MvNetworkControlFrame", "visible": 1}
mvNetworkControlFrame_btnContact_MinervaD_MvDragablePushButton = {"container": splitter_MvNetworkControlFrame_MinervaD_MvNetworkControlFrame, "name": "btnContact", "type": "MinervaD::MvDragablePushButton", "visible": 1}
splitter_QFrame = {"container": ladderEditorWidget_splitter_QSplitter, "type": "QFrame", "unnamed": 1, "visible": 1}
treeView_QHeaderView = {"container": variableTableFrame_treeView_MinervaD_MvCustomTreeView, "orientation": 1, "type": "QHeaderView", "unnamed": 1, "visible": 1}
o_A_QAction = {"text": "접점(A접점) 삽입", "type": "QAction", "unnamed": 1, "visible": True}
mvAddToTableDialog_MinervaD_MvAddToTableDialog_2 = {"name": "MvAddToTableDialog", "type": "MinervaD::MvAddToTableDialog", "visible": 0}
mvNewVariableDialog_MinervaD_MvNewVariableDialog_2 = {"name": "MvNewVariableDialog", "type": "MinervaD::MvNewVariableDialog", "visible": 0}
o_QAction = {"text": "코일 삽입", "type": "QAction", "unnamed": 1, "visible": True}
o_QGraphicsItem_14 = {"acceptDrops": "no", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 4, "visible": "yes"}
o_QGraphicsItem_15 = {"acceptDrops": "no", "container": o_QGraphicsItem_14, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 11, "visible": "yes"}
ladderView_QScrollBar_2 = {"container": MinervaD_MvLadderViewFrame, "type": "QScrollBar", "unnamed": 1, "visible": 1}
o_font_color_0000ff_Warnings_br_WMD02005_font_QGraphicsItem_2 = {"acceptDrops": "yes", "container": o_font_color_0000ff_Warnings_br_WMD02005_font_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 2, "visible": "yes"}
o_font_color_0000ff_Warnings_br_WMD02005_font_QGraphicsItem_3 = {"acceptDrops": "yes", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "toolTip": "<font color='#0000ff'>Warnings :<br>[WMD02005] 완성되지 않은 로직이 있습니다.</font>", "type": "QGraphicsItem", "userType": 9, "visible": "yes"}
o_font_color_0000ff_Warnings_br_WMD02005_font_QGraphicsItem_4 = {"acceptDrops": "yes", "container": o_font_color_0000ff_Warnings_br_WMD02005_font_QGraphicsItem_3, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 2, "visible": "yes"}
mvNetworkControlFrame_btnCoil_MinervaD_MvDragablePushButton = {"container": splitter_MvNetworkControlFrame_MinervaD_MvNetworkControlFrame, "name": "btnCoil", "type": "MinervaD::MvDragablePushButton", "visible": 1}
mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget = {"container": mvProjectTreeFrame_MinervaD_MvProjectTreeFrame, "name": "treeWidget", "type": "MinervaD::MvProjectTreeWidget", "visible": 1}
treeWidget_UserFcTest_QModelIndex = {"column": 0, "container": mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "text": "UserFcTest", "type": "QModelIndex"}
userFcTest_POU_QModelIndex = {"column": 0, "container": treeWidget_UserFcTest_QModelIndex, "text": "POU", "type": "QModelIndex"}
pOU_QModelIndex = {"column": 0, "container": userFcTest_POU_QModelIndex, "text": "함수", "type": "QModelIndex"}
o_Function1_QModelIndex = {"column": 0, "container": pOU_QModelIndex, "text": "Function1", "type": "QModelIndex"}
