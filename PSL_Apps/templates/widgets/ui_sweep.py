# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSL_Apps/templates/widgets/sweep.ui'
#
# Created: Tue Aug  9 01:56:31 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(395, 29)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(0, 2, 1, 1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.enable = QtGui.QCheckBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable.sizePolicy().hasHeightForWidth())
        self.enable.setSizePolicy(sizePolicy)
        self.enable.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enable.setFont(font)
        self.enable.setObjectName(_fromUtf8("enable"))
        self.horizontalLayout.addWidget(self.enable)
        self.startBox = QtGui.QDoubleSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBox.sizePolicy().hasHeightForWidth())
        self.startBox.setSizePolicy(sizePolicy)
        self.startBox.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.startBox.setFont(font)
        self.startBox.setPrefix(_fromUtf8(""))
        self.startBox.setObjectName(_fromUtf8("startBox"))
        self.horizontalLayout.addWidget(self.startBox)
        self.stopBox = QtGui.QDoubleSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBox.sizePolicy().hasHeightForWidth())
        self.stopBox.setSizePolicy(sizePolicy)
        self.stopBox.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.stopBox.setFont(font)
        self.stopBox.setPrefix(_fromUtf8(""))
        self.stopBox.setObjectName(_fromUtf8("stopBox"))
        self.horizontalLayout.addWidget(self.stopBox)
        self.numBox = QtGui.QSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numBox.sizePolicy().hasHeightForWidth())
        self.numBox.setSizePolicy(sizePolicy)
        self.numBox.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.numBox.setFont(font)
        self.numBox.setSuffix(_fromUtf8(""))
        self.numBox.setMinimum(2)
        self.numBox.setMaximum(1000)
        self.numBox.setProperty("value", 10)
        self.numBox.setObjectName(_fromUtf8("numBox"))
        self.horizontalLayout.addWidget(self.numBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.enable.setText(_translate("Form", "title", None))

