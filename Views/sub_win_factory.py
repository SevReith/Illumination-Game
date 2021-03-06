# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_win_factory.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_mid_left = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_mid_left.setFont(font)
        self.lbl_mid_left.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_mid_left.setObjectName("lbl_mid_left")
        self.gridLayout.addWidget(self.lbl_mid_left, 1, 1, 1, 1)
        self.lbl_top = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_top.setFont(font)
        self.lbl_top.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_top.setObjectName("lbl_top")
        self.gridLayout.addWidget(self.lbl_top, 0, 1, 1, 2)
        self.lbl_mid_right = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_mid_right.setFont(font)
        self.lbl_mid_right.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_mid_right.setObjectName("lbl_mid_right")
        self.gridLayout.addWidget(self.lbl_mid_right, 1, 2, 1, 1)
        self.btn_increase_factory = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_increase_factory.setObjectName("btn_increase_factory")
        self.gridLayout.addWidget(self.btn_increase_factory, 2, 1, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_tab2_top = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_tab2_top.setObjectName("lbl_tab2_top")
        self.verticalLayout.addWidget(self.lbl_tab2_top)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_tab2_left = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_tab2_left.setObjectName("lbl_tab2_left")
        self.horizontalLayout_5.addWidget(self.lbl_tab2_left)
        self.lbl_tab2_right = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_tab2_right.setObjectName("lbl_tab2_right")
        self.horizontalLayout_5.addWidget(self.lbl_tab2_right)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_tab2_dismantle_fixed_pos_lay = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_tab2_dismantle_fixed_pos_lay.setObjectName("btn_tab2_dismantle_fixed_pos_lay")
        self.horizontalLayout.addWidget(self.btn_tab2_dismantle_fixed_pos_lay)
        self.btn_tab2_build_fixed_pos_lay = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_tab2_build_fixed_pos_lay.setObjectName("btn_tab2_build_fixed_pos_lay")
        self.horizontalLayout.addWidget(self.btn_tab2_build_fixed_pos_lay)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_tab3_top = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_tab3_top.setObjectName("lbl_tab3_top")
        self.verticalLayout_2.addWidget(self.lbl_tab3_top)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_tab3_left = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_tab3_left.setObjectName("lbl_tab3_left")
        self.verticalLayout_5.addWidget(self.lbl_tab3_left)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_tab3_right = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_tab3_right.setObjectName("lbl_tab3_right")
        self.verticalLayout_6.addWidget(self.lbl_tab3_right)
        self.lbl_tab3_right_dept = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_tab3_right_dept.setObjectName("lbl_tab3_right_dept")
        self.verticalLayout_6.addWidget(self.lbl_tab3_right_dept)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_tab3_build_process_lay = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_tab3_build_process_lay.setObjectName("btn_tab3_build_process_lay")
        self.gridLayout_2.addWidget(self.btn_tab3_build_process_lay, 0, 0, 1, 1)
        self.btn_tab3_dismantle_process_lay = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_tab3_dismantle_process_lay.setObjectName("btn_tab3_dismantle_process_lay")
        self.gridLayout_2.addWidget(self.btn_tab3_dismantle_process_lay, 1, 0, 1, 1)
        self.btn_tab3_destroy_dept = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_tab3_destroy_dept.setObjectName("btn_tab3_destroy_dept")
        self.gridLayout_2.addWidget(self.btn_tab3_destroy_dept, 1, 1, 1, 1)
        self.btn_tab3_add_department = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_tab3_add_department.setObjectName("btn_tab3_add_department")
        self.gridLayout_2.addWidget(self.btn_tab3_add_department, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_tab4_top = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.lbl_tab4_top.setObjectName("lbl_tab4_top")
        self.verticalLayout_3.addWidget(self.lbl_tab4_top)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_tab4_left = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.lbl_tab4_left.setObjectName("lbl_tab4_left")
        self.horizontalLayout_7.addWidget(self.lbl_tab4_left)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbl_tab4_right = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.lbl_tab4_right.setObjectName("lbl_tab4_right")
        self.verticalLayout_7.addWidget(self.lbl_tab4_right)
        self.lbl_tab4_right_dept = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.lbl_tab4_right_dept.setObjectName("lbl_tab4_right_dept")
        self.verticalLayout_7.addWidget(self.lbl_tab4_right_dept)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_tab4_build_cellular_lay = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_tab4_build_cellular_lay.setObjectName("btn_tab4_build_cellular_lay")
        self.gridLayout_3.addWidget(self.btn_tab4_build_cellular_lay, 0, 0, 1, 1)
        self.btn_tab5_dismantle_cellular_lay = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_tab5_dismantle_cellular_lay.setObjectName("btn_tab5_dismantle_cellular_lay")
        self.gridLayout_3.addWidget(self.btn_tab5_dismantle_cellular_lay, 1, 0, 1, 1)
        self.btn_tab4_add_department = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_tab4_add_department.setObjectName("btn_tab4_add_department")
        self.gridLayout_3.addWidget(self.btn_tab4_add_department, 0, 1, 1, 1)
        self.btn_tab4_destroy_dept = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_tab4_destroy_dept.setObjectName("btn_tab4_destroy_dept")
        self.gridLayout_3.addWidget(self.btn_tab4_destroy_dept, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_tab5_top = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.lbl_tab5_top.setObjectName("lbl_tab5_top")
        self.verticalLayout_4.addWidget(self.lbl_tab5_top)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_tab5_left = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.lbl_tab5_left.setObjectName("lbl_tab5_left")
        self.horizontalLayout_8.addWidget(self.lbl_tab5_left)
        self.lbl_tab5_right = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.lbl_tab5_right.setObjectName("lbl_tab5_right")
        self.horizontalLayout_8.addWidget(self.lbl_tab5_right)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btn_tab5_dismantle_line_lay = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_tab5_dismantle_line_lay.setObjectName("btn_tab5_dismantle_line_lay")
        self.horizontalLayout_4.addWidget(self.btn_tab5_dismantle_line_lay)
        self.btn_tab5_build_line_lay = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_tab5_build_line_lay.setObjectName("btn_tab5_build_line_lay")
        self.horizontalLayout_4.addWidget(self.btn_tab5_build_line_lay)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Factory"))
        self.lbl_mid_left.setText(_translate("Form", "TextLabel"))
        self.lbl_top.setText(_translate("Form", "TextLabel"))
        self.lbl_mid_right.setText(_translate("Form", "TextLabel"))
        self.btn_increase_factory.setText(_translate("Form", "Increase Factory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Info"))
        self.lbl_tab2_top.setText(_translate("Form", "TextLabel"))
        self.lbl_tab2_left.setText(_translate("Form", "TextLabel"))
        self.lbl_tab2_right.setText(_translate("Form", "TextLabel"))
        self.btn_tab2_dismantle_fixed_pos_lay.setText(_translate("Form", "Dismantle Fixed Position Layout"))
        self.btn_tab2_build_fixed_pos_lay.setText(_translate("Form", "Build Fixed Position Layout"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Fixed Position Layout"))
        self.lbl_tab3_top.setText(_translate("Form", "TextLabel"))
        self.lbl_tab3_left.setText(_translate("Form", "TextLabel"))
        self.lbl_tab3_right.setText(_translate("Form", "TextLabel"))
        self.lbl_tab3_right_dept.setText(_translate("Form", "TextLabel"))
        self.btn_tab3_build_process_lay.setToolTip(_translate("Form", "<html><head/><body><p>You can only build 1 Process layout!</p><p>Add departments to increase the production output!</p></body></html>"))
        self.btn_tab3_build_process_lay.setText(_translate("Form", "Build Process Layout"))
        self.btn_tab3_dismantle_process_lay.setText(_translate("Form", "Dismantle Process Layout"))
        self.btn_tab3_destroy_dept.setText(_translate("Form", "Dismantle Department"))
        self.btn_tab3_add_department.setToolTip(_translate("Form", "<html><head/><body><p>You can increase the output of the Process layout by building additional departments within the layout.</p><p>Each department becomes more expensive!</p></body></html>"))
        self.btn_tab3_add_department.setText(_translate("Form", "Add Department"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Process Layout"))
        self.lbl_tab4_top.setText(_translate("Form", "TextLabel"))
        self.lbl_tab4_left.setText(_translate("Form", "TextLabel"))
        self.lbl_tab4_right.setText(_translate("Form", "TextLabel"))
        self.lbl_tab4_right_dept.setText(_translate("Form", "TextLabel"))
        self.btn_tab4_build_cellular_lay.setToolTip(_translate("Form", "<html><head/><body><p>You can only build 1 Cellular layout!</p><p>Add departments to increase the production output!</p></body></html>"))
        self.btn_tab4_build_cellular_lay.setText(_translate("Form", "Build Cellular Layout"))
        self.btn_tab5_dismantle_cellular_lay.setText(_translate("Form", "Dismantle Cellular Layout"))
        self.btn_tab4_add_department.setToolTip(_translate("Form", "<html><head/><body><p>You can increase the output of the Cellular layout by building additional departments within the layout.</p><p>Each department becomes more expensive!</p></body></html>"))
        self.btn_tab4_add_department.setText(_translate("Form", "Add Department"))
        self.btn_tab4_destroy_dept.setText(_translate("Form", "Dismantle Department"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Cellular Layout"))
        self.lbl_tab5_top.setText(_translate("Form", "TextLabel"))
        self.lbl_tab5_left.setText(_translate("Form", "TextLabel"))
        self.lbl_tab5_right.setText(_translate("Form", "TextLabel"))
        self.btn_tab5_dismantle_line_lay.setText(_translate("Form", "Dismantle Line Layout"))
        self.btn_tab5_build_line_lay.setText(_translate("Form", "Build Line Layout"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Line Layout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
