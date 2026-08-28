# encoding: UTF-8

from objectmaphelper import *

login_win           = {"name": "TXLogin", "type": "TXLogin", "visible": 1}
login_stack         = {"name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "window": login_win}
login_remote_tab    = {"container": login_stack, "name": "tabRemoteView", "type": "QWidget"}
login_pw            = {"container": login_remote_tab, "objectName": "lineEdit_PASS_M2I", "type": "QLineEdit"}
login_connect       = {"objectName": "pushButton_OK", "type": "QPushButton", "window": login_win}
keyUI_win = {"name": "TXStringKeyUI", "type": "TXStringKeyUI", "visible": 1}
keyUI_edit = {"objectName": "leString", "type": "QLineEdit", "window": keyUI_win}
keyUI_frame = {"name": "frame", "type": "QFrame", "window": keyUI_win}
keyUI_fmDefault = {"container": keyUI_frame, "name": "fmDefault", "type": "QFrame"}
keyUI_enter = {"container": keyUI_fmDefault, "objectName": "tbEnter", "type": "QToolButton"}
viewer_win = {"name": "MainWindow", "type": "MainWindow", "visible": 1}
viewer_oriscreen = {"text": "Original Screen", "type": "QToolButton", "window": viewer_win}
viewer_disconnect = {"text": "Disconnect", "type": "QToolButton", "window": viewer_win}
viewer_connect = {"text": "Connect", "type": "QToolButton", "window": viewer_win}
