# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatorform.ui'
#
# Created: Thu Dec 29 12:43:57 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CalculatorForm(object):
    def setupUi(self, CalculatorForm):
        CalculatorForm.setObjectName("CalculatorForm")
        CalculatorForm.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5), QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalculatorForm.sizePolicy().hasHeightForWidth())
        CalculatorForm.setSizePolicy(sizePolicy)
        self.gridlayout = QtGui.QGridLayout(CalculatorForm)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 0, 6, 1, 1)
        self.label_3_2 = QtGui.QLabel(CalculatorForm)
        self.label_3_2.setGeometry(QtCore.QRect(169, 9, 20, 52))
        self.label_3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3_2.setObjectName("label_3_2")
        self.gridlayout.addWidget(self.label_3_2, 0, 4, 1, 1)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setContentsMargins(1, 1, 1, 1)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label_2_2_2 = QtGui.QLabel(CalculatorForm)
        self.label_2_2_2.setGeometry(QtCore.QRect(1, 1, 36, 17))
        self.label_2_2_2.setObjectName("label_2_2_2")
        self.vboxlayout.addWidget(self.label_2_2_2)
        self.outputWidget = QtGui.QLabel(CalculatorForm)
        self.outputWidget.setGeometry(QtCore.QRect(1, 24, 36, 27))
        self.outputWidget.setFrameShape(QtGui.QFrame.Box)
        self.outputWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.outputWidget.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignBottom|QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignHorizontal_Mask|QtCore.Qt.AlignJustify|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignVertical_Mask)
        self.outputWidget.setObjectName("outputWidget")
        self.vboxlayout.addWidget(self.outputWidget)
        self.gridlayout.addLayout(self.vboxlayout, 0, 5, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(1, 1, 1, 1)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.label_2 = QtGui.QLabel(CalculatorForm)
        self.label_2.setGeometry(QtCore.QRect(1, 1, 46, 19))
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)
        self.inputSpinBox2 = QtGui.QSpinBox(CalculatorForm)
        self.inputSpinBox2.setGeometry(QtCore.QRect(1, 26, 46, 25))
        self.inputSpinBox2.setObjectName("inputSpinBox2")
        self.vboxlayout1.addWidget(self.inputSpinBox2)
        self.gridlayout.addLayout(self.vboxlayout1, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(CalculatorForm)
        self.label_3.setGeometry(QtCore.QRect(63, 9, 20, 52))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(1, 1, 1, 1)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.label = QtGui.QLabel(CalculatorForm)
        self.label.setGeometry(QtCore.QRect(1, 1, 46, 19))
        self.label.setObjectName("label")
        self.vboxlayout2.addWidget(self.label)
        self.inputSpinBox1 = QtGui.QSpinBox(CalculatorForm)
        self.inputSpinBox1.setGeometry(QtCore.QRect(1, 26, 46, 25))
        self.inputSpinBox1.setObjectName("inputSpinBox1")
        self.vboxlayout2.addWidget(self.inputSpinBox1)
        self.gridlayout.addLayout(self.vboxlayout2, 0, 0, 1, 1)

        self.retranslateUi(CalculatorForm)
        QtCore.QMetaObject.connectSlotsByName(CalculatorForm)

    def retranslateUi(self, CalculatorForm):
        CalculatorForm.setWindowTitle(QtGui.QApplication.translate("CalculatorForm", "Calculator Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3_2.setText(QtGui.QApplication.translate("CalculatorForm", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2_2_2.setText(QtGui.QApplication.translate("CalculatorForm", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.outputWidget.setText(QtGui.QApplication.translate("CalculatorForm", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CalculatorForm", "Input 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CalculatorForm", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CalculatorForm", "Input 1", None, QtGui.QApplication.UnicodeUTF8))
