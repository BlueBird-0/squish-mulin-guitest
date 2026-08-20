# encoding: UTF-8

from objectmaphelper import *

muLiN_Creator_MinervaD_MvMainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "visible": 1, "windowTitle": "MuLiN Creator"}

muLiN_Creator_QMenu = {"title": "파일", "type": "QMenu", "unnamed": 1, "visible": 0, "window": muLiN_Creator_MinervaD_MvMainWindow}
o_QAction_menu_file = {"container": muLiN_Creator_QMenu, "text": "파일", "type": "QAction", "unnamed": 1, "visible": True}
o_QAction_menu_openProject = {"container": muLiN_Creator_QMenu, "text": "프로젝트 열기", "type": "QAction", "unnamed": 1, "visible": True}
qFileDialog_QFileDialog = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
qFileDialog_splitter_QSplitter = {"name": "splitter", "type": "QSplitter", "visible": 1, "window": qFileDialog_QFileDialog}
splitter_frame_QFrame = {"container": qFileDialog_splitter_QSplitter, "name": "frame", "type": "QFrame", "visible": 1}
frame_stackedWidget_QStackedWidget = {"container": splitter_frame_QFrame, "name": "stackedWidget", "type": "QStackedWidget", "visible": 1}
stackedWidget_treeView_QTreeView = {"container": frame_stackedWidget_QStackedWidget, "name": "treeView", "type": "QTreeView", "visible": 1}
treeView_testProject_SquishTest1 = {"column": 0, "container": stackedWidget_treeView_QTreeView, "text": "SquishTest1", "type": "QModelIndex"}
treeView_testProject_SquishTest2 = {"column": 0, "container": stackedWidget_treeView_QTreeView, "text": "SquishTest2", "type": "QModelIndex"}
treeView_testProject_SquishTest3 = {"column": 0, "container": stackedWidget_treeView_QTreeView, "text": "SquishTest3", "type": "QModelIndex"}

treeView_SquishTest1_mdp_QModelIndex = {"column": 0, "container": stackedWidget_treeView_QTreeView, "text": "SquishTest1.mdp", "type": "QModelIndex"}
treeView_SquishTest2_mdp_QModelIndex = {"column": 0, "container": stackedWidget_treeView_QTreeView, "text": "SquishTest2.mdp", "type": "QModelIndex"}
treeView_SquishTest3_mdp_QModelIndex = {"column": 0, "container": stackedWidget_treeView_QTreeView, "text": "SquishTest3.mdp", "type": "QModelIndex"}

muLiN_Creator_QMenu_2 = {"occurrence": 13, "type": "QMenu", "unnamed": 1, "visible": 0, "window": muLiN_Creator_MinervaD_MvMainWindow}
qFileDialog_Open_QPushButton = {"text": "Open", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": qFileDialog_QFileDialog}
mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog = {"name": "MvRecoverProjectDialog", "type": "MinervaD::MvRecoverProjectDialog", "visible": 1}
muLiN_Creator_QMenuBar = {"type": "QMenuBar", "unnamed": 1, "visible": 1, "window": muLiN_Creator_MinervaD_MvMainWindow}
muLiN_Creator_QMenu_3 = {"title": "파일", "type": "QMenu", "unnamed": 1, "visible": 1, "window": muLiN_Creator_MinervaD_MvMainWindow}
mvRecoverProjectDialog_btnClose_QPushButton = {"name": "btnClose", "type": "QPushButton", "visible": 1, "window": mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog}
muLiN_Creator_Documents_mdp_MinervaD_MvMainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "visible": 1}
muLiN_Creator_Documents_mdp_QMenuBar = {"type": "QMenuBar", "unnamed": 1, "visible": 1, "window": muLiN_Creator_Documents_mdp_MinervaD_MvMainWindow}
muLiN_Creator_Documents_mdp_QMenu = {"title": "프로젝트", "type": "QMenu", "unnamed": 1, "visible": 1, "window": muLiN_Creator_Documents_mdp_MinervaD_MvMainWindow}
o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MinervaD_MvMainWindow = {"type": "MinervaD::MvMainWindow", "unnamed": 1, "visible": 1}
o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MvMessageFrame_MinervaD_MvMessageFrame = {"name": "MvMessageFrame", "type": "MinervaD::MvMessageFrame", "visible": 1, "window": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MinervaD_MvMainWindow}
mvMessageFrame_qt_tabwidget_stackedwidget_QStackedWidget_2 = {"container": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MvMessageFrame_MinervaD_MvMessageFrame, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
qt_tabwidget_stackedwidget_tabBuild_QWidget_2 = {"container": mvMessageFrame_qt_tabwidget_stackedwidget_QStackedWidget_2, "name": "tabBuild", "type": "QWidget", "visible": 1}
tabBuild_btnError_QToolButton_2 = {"container": qt_tabwidget_stackedwidget_tabBuild_QWidget_2, "name": "btnError", "type": "QToolButton", "visible": 1}
o_Qtitan_ToolButton = {"text": "연결", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MinervaD_MvMainWindow}
o_Qtitan_ToolButton_2 = {"text": "다운로드", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MinervaD_MvMainWindow}
mvDownloadToDeviceDialog_MinervaD_MvDownloadToDeviceDialog = {"name": "MvDownloadToDeviceDialog", "type": "MinervaD::MvDownloadToDeviceDialog", "visible": 1}
mvDownloadToDeviceDialog_QPushButton = {"text": "확인", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mvDownloadToDeviceDialog_MinervaD_MvDownloadToDeviceDialog}
o_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "장치에 다운로드"}
o_QPushButton = {"text": "실행 중지", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": o_QMessageBox}
o_Qtitan_ToolButton_3 = {"text": "모니터링 시작", "type": "Qtitan::ToolButton", "unnamed": 1, "visible": 1, "window": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MinervaD_MvMainWindow}
mvProjectTreeFrame_MinervaD_MvProjectTreeFrame = {"name": "MvProjectTreeFrame", "type": "MinervaD::MvProjectTreeFrame", "visible": 1, "window": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MinervaD_MvMainWindow}
mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget = {"container": mvProjectTreeFrame_MinervaD_MvProjectTreeFrame, "name": "treeWidget", "type": "MinervaD::MvProjectTreeWidget", "visible": 1}
treeWidget_SquishTest3_QModelIndex = {"column": 0, "container": mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "text": "SquishTest3", "type": "QModelIndex"}
squishTest3_POU_QModelIndex = {"column": 0, "container": treeWidget_SquishTest3_QModelIndex, "text": "POU", "type": "QModelIndex"}
pOU_QModelIndex = {"column": 0, "container": squishTest3_POU_QModelIndex, "text": "프로그램", "type": "QModelIndex"}
o_Program1_QModelIndex = {"column": 0, "container": pOU_QModelIndex, "text": "Program1", "type": "QModelIndex"}
ladderEditorWidget_MinervaD_MvLadderEditorWidget = {"name": "LadderEditorWidget", "type": "MinervaD::MvLadderEditorWidget", "visible": 1, "window": o_MuLiN_Creator_C_Users_IHJEON_Documents_SquishTest1_SquishTest1_mdp_MinervaD_MvMainWindow}
ladderEditorWidget_splitter_QSplitter = {"container": ladderEditorWidget_MinervaD_MvLadderEditorWidget, "name": "splitter", "type": "QSplitter", "visible": 1}
splitter_LadderView_MinervaD_MvLadderViewFrame = {"container": ladderEditorWidget_splitter_QSplitter, "name": "LadderView", "type": "MinervaD::MvLadderViewFrame", "visible": 1}
ladderView_QGraphicsItem = {"acceptDrops": "yes", "container": splitter_LadderView_MinervaD_MvLadderViewFrame, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 1, "visible": "yes"}
o_QGraphicsItem = {"acceptDrops": "no", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
o_QGraphicsItem_2 = {"acceptDrops": "no", "container": o_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "occurrence": 3, "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
o_h2_b_font_color_blue_font_b_h2_b_30_b_br_QGraphicsItem = {"acceptDrops": "no", "container": o_QGraphicsItem_2, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 19, "visible": "yes"}
o_QGraphicsItem_ADD = {"acceptDrops": "no", "container": ladderView_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "toolTip": "<h3><b><font color='blue'>Function : ADD</font></b></h3><b>입력들의 합을 계산 후 OUT에 출력합니다.</b><br><br>매개 변수 :<br>    [IN] IN1 : ANY_NUM<br>    [IN] IN2 : ANY_NUM<br>    [OUT] OUT : ANY_NUM", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
o_h3_b_font_color_blue_Function_ADD_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem = {"acceptDrops": "no", "container": o_QGraphicsItem_ADD, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "occurrence": 3, "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
ladderView_QScrollBar = {"container": splitter_LadderView_MinervaD_MvLadderViewFrame, "occurrence": 2, "type": "QScrollBar", "unnamed": 1, "visible": 1}
ladderView_QGraphicsItem_2 = {"acceptDrops": "yes", "container": splitter_LadderView_MinervaD_MvLadderViewFrame, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "occurrence": 2, "selectable": "yes", "type": "QGraphicsItem", "userType": 1, "visible": "yes"}
o_h3_b_font_color_blue_Function_SUB_font_b_h3_b_IN1_IN2_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem = {"acceptDrops": "no", "container": ladderView_QGraphicsItem_2, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "toolTip": "<h3><b><font color='blue'>Function : SUB</font></b></h3><b>IN1에서 IN2를 뺄샘 후 OUT에 출력합니다.</b><br><br>매개 변수 :<br>    [IN] IN1 : ANY_NUM<br>    [IN] IN2 : ANY_NUM<br>    [OUT] OUT : ANY_NUM", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
o_h3_b_font_color_blue_Function_SUB_font_b_h3_b_IN1_IN2_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem_2 = {"acceptDrops": "no", "container": o_h3_b_font_color_blue_Function_SUB_font_b_h3_b_IN1_IN2_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "occurrence": 3, "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
o_h2_b_font_color_blue_font_b_h2_b_7_b_br_QGraphicsItem = {"acceptDrops": "no", "container": o_h3_b_font_color_blue_Function_SUB_font_b_h3_b_IN1_IN2_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem_2, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "toolTip": "<h2><b><font color='blue'>모니터링 데이터</font></b></h2><b>  '7'</b><br>", "type": "QGraphicsItem", "userType": 19, "visible": "yes"}
o_h3_b_font_color_blue_Function_ADD_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem_2 = {"acceptDrops": "no", "container": o_QGraphicsItem_ADD, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}
ladderView_QGraphicsItem_3 = {"acceptDrops": "yes", "container": splitter_LadderView_MinervaD_MvLadderViewFrame, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "occurrence": 3, "selectable": "yes", "type": "QGraphicsItem", "userType": 1, "visible": "yes"}
o_h3_b_font_color_blue_Function_MUL_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem = {"acceptDrops": "no", "container": ladderView_QGraphicsItem_3, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "yes", "selectable": "yes", "toolTip": "<h3><b><font color='blue'>Function : MUL</font></b></h3><b>입력들의 곱을 계산 후 OUT에 출력합니다.</b><br><br>매개 변수 :<br>    [IN] IN1 : ANY_NUM<br>    [IN] IN2 : ANY_NUM<br>    [OUT] OUT : ANY_NUM", "type": "QGraphicsItem", "userType": 5, "visible": "yes"}
o_h3_b_font_color_blue_Function_MUL_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem_2 = {"acceptDrops": "no", "container": o_h3_b_font_color_blue_Function_MUL_font_b_h3_b_OUT_b_br_br_br_IN_IN1_ANY_NUM_br_IN_IN2_ANY_NUM_br_OUT_OUT_ANY_NUM_QGraphicsItem, "enabled": "yes", "focusable": "yes", "lineColor": "#000000", "movable": "no", "occurrence": 3, "selectable": "yes", "type": "QGraphicsItem", "userType": 14, "visible": "yes"}

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
