# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.resize_input_folder_button = QtWidgets.QPushButton(self.tab)
        self.resize_input_folder_button.setObjectName("resize_input_folder_button")
        self.verticalLayout_6.addWidget(self.resize_input_folder_button)
        self.resize_input_path_edit = QtWidgets.QLineEdit(self.tab)
        self.resize_input_path_edit.setObjectName("resize_input_path_edit")
        self.verticalLayout_6.addWidget(self.resize_input_path_edit)
        self.resize_output_folder_button = QtWidgets.QPushButton(self.tab)
        self.resize_output_folder_button.setObjectName("resize_output_folder_button")
        self.verticalLayout_6.addWidget(self.resize_output_folder_button)
        self.resize_output_path_edit = QtWidgets.QLineEdit(self.tab)
        self.resize_output_path_edit.setObjectName("resize_output_path_edit")
        self.verticalLayout_6.addWidget(self.resize_output_path_edit)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.resize_required_width_edit = QtWidgets.QLineEdit(self.tab)
        self.resize_required_width_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.resize_required_width_edit.setObjectName("resize_required_width_edit")
        self.verticalLayout_6.addWidget(self.resize_required_width_edit)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.resize_required_height_edit = QtWidgets.QLineEdit(self.tab)
        self.resize_required_height_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.resize_required_height_edit.setObjectName("resize_required_height_edit")
        self.verticalLayout_6.addWidget(self.resize_required_height_edit)
        self.resize_start_button = QtWidgets.QPushButton(self.tab)
        self.resize_start_button.setObjectName("resize_start_button")
        self.verticalLayout_6.addWidget(self.resize_start_button)
        self.resize_progressBar = QtWidgets.QProgressBar(self.tab)
        self.resize_progressBar.setTabletTracking(False)
        self.resize_progressBar.setAcceptDrops(False)
        self.resize_progressBar.setProperty("value", 0)
        self.resize_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.resize_progressBar.setTextVisible(True)
        self.resize_progressBar.setInvertedAppearance(False)
        self.resize_progressBar.setObjectName("resize_progressBar")
        self.verticalLayout_6.addWidget(self.resize_progressBar)
        self.tabWidget.addTab(self.tab, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_13)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.input_folder_button = QtWidgets.QPushButton(self.splitter_2)
        self.input_folder_button.setObjectName("input_folder_button")
        self.input_path_edit = QtWidgets.QLineEdit(self.splitter_2)
        self.input_path_edit.setObjectName("input_path_edit")
        self.output_folder_button = QtWidgets.QPushButton(self.splitter_2)
        self.output_folder_button.setObjectName("output_folder_button")
        self.output_path_edit = QtWidgets.QLineEdit(self.splitter_2)
        self.output_path_edit.setObjectName("output_path_edit")
        self.label_0 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_0.setFont(font)
        self.label_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_0.setScaledContents(False)
        self.label_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_0.setObjectName("label_0")
        self.required_width_edit = QtWidgets.QLineEdit(self.splitter_2)
        self.required_width_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.required_width_edit.setObjectName("required_width_edit")
        self.label_1 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.required_height_edit = QtWidgets.QLineEdit(self.splitter_2)
        self.required_height_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.required_height_edit.setObjectName("required_height_edit")
        self.start_button = QtWidgets.QPushButton(self.splitter_2)
        self.start_button.setObjectName("start_button")
        self.progressBar = QtWidgets.QProgressBar(self.splitter_2)
        self.progressBar.setTabletTracking(False)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_14)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_3 = QtWidgets.QSplitter(self.tab_14)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.input_folder_button_2 = QtWidgets.QPushButton(self.splitter_3)
        self.input_folder_button_2.setObjectName("input_folder_button_2")
        self.input_path_edit_2 = QtWidgets.QLineEdit(self.splitter_3)
        self.input_path_edit_2.setObjectName("input_path_edit_2")
        self.output_folder_button_2 = QtWidgets.QPushButton(self.splitter_3)
        self.output_folder_button_2.setObjectName("output_folder_button_2")
        self.output_path_edit_2 = QtWidgets.QLineEdit(self.splitter_3)
        self.output_path_edit_2.setObjectName("output_path_edit_2")
        self.label_7 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.required_width_edit_2 = QtWidgets.QLineEdit(self.splitter_3)
        self.required_width_edit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.required_width_edit_2.setObjectName("required_width_edit_2")
        self.label_8 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.required_height_edit_2 = QtWidgets.QLineEdit(self.splitter_3)
        self.required_height_edit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.required_height_edit_2.setObjectName("required_height_edit_2")
        self.start_button_2 = QtWidgets.QPushButton(self.splitter_3)
        self.start_button_2.setObjectName("start_button_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.splitter_3)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_4.addWidget(self.splitter_3)
        self.tabWidget.addTab(self.tab_14, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.npy_input_folder_button = QtWidgets.QPushButton(self.tab_2)
        self.npy_input_folder_button.setObjectName("npy_input_folder_button")
        self.verticalLayout_22.addWidget(self.npy_input_folder_button)
        self.npy_input_path_edit = QtWidgets.QLineEdit(self.tab_2)
        self.npy_input_path_edit.setObjectName("npy_input_path_edit")
        self.verticalLayout_22.addWidget(self.npy_input_path_edit)
        self.npy_output_folder_button = QtWidgets.QPushButton(self.tab_2)
        self.npy_output_folder_button.setObjectName("npy_output_folder_button")
        self.verticalLayout_22.addWidget(self.npy_output_folder_button)
        self.npy_output_path_edit = QtWidgets.QLineEdit(self.tab_2)
        self.npy_output_path_edit.setText("")
        self.npy_output_path_edit.setObjectName("npy_output_path_edit")
        self.verticalLayout_22.addWidget(self.npy_output_path_edit)
        self.npy_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.npy_lineEdit.setObjectName("npy_lineEdit")
        self.verticalLayout_22.addWidget(self.npy_lineEdit)
        self.npy_start_button = QtWidgets.QPushButton(self.tab_2)
        self.npy_start_button.setObjectName("npy_start_button")
        self.verticalLayout_22.addWidget(self.npy_start_button)
        self.npy_progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.npy_progressBar.setProperty("value", 0)
        self.npy_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.npy_progressBar.setObjectName("npy_progressBar")
        self.verticalLayout_22.addWidget(self.npy_progressBar)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_folder_button_3 = QtWidgets.QPushButton(self.tab_15)
        self.input_folder_button_3.setObjectName("input_folder_button_3")
        self.verticalLayout.addWidget(self.input_folder_button_3)
        self.input_path_edit_3 = QtWidgets.QLineEdit(self.tab_15)
        self.input_path_edit_3.setObjectName("input_path_edit_3")
        self.verticalLayout.addWidget(self.input_path_edit_3)
        self.output_folder_button_3 = QtWidgets.QPushButton(self.tab_15)
        self.output_folder_button_3.setObjectName("output_folder_button_3")
        self.verticalLayout.addWidget(self.output_folder_button_3)
        self.output_path_edit_3 = QtWidgets.QLineEdit(self.tab_15)
        self.output_path_edit_3.setText("")
        self.output_path_edit_3.setObjectName("output_path_edit_3")
        self.verticalLayout.addWidget(self.output_path_edit_3)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_15)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.start_button_3 = QtWidgets.QPushButton(self.tab_15)
        self.start_button_3.setObjectName("start_button_3")
        self.verticalLayout.addWidget(self.start_button_3)
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_15)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout.addWidget(self.progressBar_3)
        self.tabWidget.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_16)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.input_folder_button_4 = QtWidgets.QPushButton(self.tab_16)
        self.input_folder_button_4.setObjectName("input_folder_button_4")
        self.verticalLayout_5.addWidget(self.input_folder_button_4)
        self.input_path_edit_4 = QtWidgets.QLineEdit(self.tab_16)
        self.input_path_edit_4.setObjectName("input_path_edit_4")
        self.verticalLayout_5.addWidget(self.input_path_edit_4)
        self.output_folder_button_4 = QtWidgets.QPushButton(self.tab_16)
        self.output_folder_button_4.setObjectName("output_folder_button_4")
        self.verticalLayout_5.addWidget(self.output_folder_button_4)
        self.output_path_edit_4 = QtWidgets.QLineEdit(self.tab_16)
        self.output_path_edit_4.setObjectName("output_path_edit_4")
        self.verticalLayout_5.addWidget(self.output_path_edit_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.start_button_4 = QtWidgets.QPushButton(self.tab_16)
        self.start_button_4.setObjectName("start_button_4")
        self.verticalLayout_5.addWidget(self.start_button_4)
        self.progressBar_4 = QtWidgets.QProgressBar(self.tab_16)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout_5.addWidget(self.progressBar_4)
        self.tabWidget.addTab(self.tab_16, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crop images"))
        self.resize_input_folder_button.setText(_translate("MainWindow", "Input images folder"))
        self.resize_output_folder_button.setText(_translate("MainWindow", "Output images folder"))
        self.label_3.setText(_translate("MainWindow", "Width, px"))
        self.label_2.setText(_translate("MainWindow", "Height, px"))
        self.resize_start_button.setText(_translate("MainWindow", "Start"))
        self.resize_progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Resize Images"))
        self.input_folder_button.setText(_translate("MainWindow", "Input images folder"))
        self.output_folder_button.setText(_translate("MainWindow", "Output images folder"))
        self.label_0.setText(_translate("MainWindow", "Width, px"))
        self.label_1.setText(_translate("MainWindow", "Height, px"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "Crop Images"))
        self.input_folder_button_2.setText(_translate("MainWindow", "Input masks folder"))
        self.output_folder_button_2.setText(_translate("MainWindow", "Output masks folder"))
        self.label_7.setText(_translate("MainWindow", "Width, px"))
        self.label_8.setText(_translate("MainWindow", "Height, px"))
        self.start_button_2.setText(_translate("MainWindow", "Start"))
        self.progressBar_2.setFormat(_translate("MainWindow", "%p%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), _translate("MainWindow", "Crop Masks"))
        self.npy_input_folder_button.setText(_translate("MainWindow", ".npy files folder"))
        self.npy_output_folder_button.setText(_translate("MainWindow", "Output masks folder"))
        self.npy_lineEdit.setText(_translate("MainWindow", "Total number of files:"))
        self.npy_start_button.setText(_translate("MainWindow", "Start"))
        self.npy_progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", ".npy to mask"))
        self.input_folder_button_3.setText(_translate("MainWindow", "Input images folder"))
        self.output_folder_button_3.setText(_translate("MainWindow", "Output images .h5 folder"))
        self.lineEdit.setText(_translate("MainWindow", "Total number of files:"))
        self.start_button_3.setText(_translate("MainWindow", "Start"))
        self.progressBar_3.setFormat(_translate("MainWindow", "%p%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("MainWindow", "Compress Images"))
        self.input_folder_button_4.setText(_translate("MainWindow", "Input masks folder"))
        self.output_folder_button_4.setText(_translate("MainWindow", "Output masks.h5 folder"))
        self.lineEdit_2.setText(_translate("MainWindow", "Total number of files:"))
        self.start_button_4.setText(_translate("MainWindow", "Start"))
        self.progressBar_4.setFormat(_translate("MainWindow", "%p%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), _translate("MainWindow", "Compress Masks"))
