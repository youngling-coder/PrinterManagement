# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_printer.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_CreatePrinterDialog(object):
    def setupUi(self, CreatePrinterDialog):
        if not CreatePrinterDialog.objectName():
            CreatePrinterDialog.setObjectName(u"CreatePrinterDialog")
        CreatePrinterDialog.resize(393, 215)
        self.formLayout = QFormLayout(CreatePrinterDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(CreatePrinterDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.locationComboBox = QComboBox(CreatePrinterDialog)
        self.locationComboBox.setObjectName(u"locationComboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.locationComboBox)

        self.label = QLabel(CreatePrinterDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.printerNameEdit = QLineEdit(CreatePrinterDialog)
        self.printerNameEdit.setObjectName(u"printerNameEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.printerNameEdit)

        self.label_3 = QLabel(CreatePrinterDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.printerModelEdit = QLineEdit(CreatePrinterDialog)
        self.printerModelEdit.setObjectName(u"printerModelEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.printerModelEdit)

        self.label_7 = QLabel(CreatePrinterDialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.DNSNameEdit = QLineEdit(CreatePrinterDialog)
        self.DNSNameEdit.setObjectName(u"DNSNameEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.DNSNameEdit)

        self.label_5 = QLabel(CreatePrinterDialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.driverNameEdit = QLineEdit(CreatePrinterDialog)
        self.driverNameEdit.setObjectName(u"driverNameEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.driverNameEdit)

        self.label_2 = QLabel(CreatePrinterDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.driverPathEdit = QLineEdit(CreatePrinterDialog)
        self.driverPathEdit.setObjectName(u"driverPathEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.driverPathEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(CreatePrinterDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.createButton = QPushButton(CreatePrinterDialog)
        self.createButton.setObjectName(u"createButton")

        self.horizontalLayout.addWidget(self.createButton)


        self.formLayout.setLayout(7, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(6, QFormLayout.ItemRole.FieldRole, self.verticalSpacer)


        self.retranslateUi(CreatePrinterDialog)

        QMetaObject.connectSlotsByName(CreatePrinterDialog)
    # setupUi

    def retranslateUi(self, CreatePrinterDialog):
        CreatePrinterDialog.setWindowTitle(QCoreApplication.translate("CreatePrinterDialog", u"Drucker erstellen", None))
        self.label_4.setText(QCoreApplication.translate("CreatePrinterDialog", u"Standort:", None))
        self.label.setText(QCoreApplication.translate("CreatePrinterDialog", u"Druckername:", None))
        self.label_3.setText(QCoreApplication.translate("CreatePrinterDialog", u"Druckermodell:", None))
        self.label_7.setText(QCoreApplication.translate("CreatePrinterDialog", u"DNS-Name:", None))
        self.label_5.setText(QCoreApplication.translate("CreatePrinterDialog", u"Treibername:", None))
        self.driverNameEdit.setText(QCoreApplication.translate("CreatePrinterDialog", u"Canon Generic PCL6 Driver", None))
        self.label_2.setText(QCoreApplication.translate("CreatePrinterDialog", u"Treiberpfad:", None))
        self.driverPathEdit.setText(QCoreApplication.translate("CreatePrinterDialog", u"CNP60MA64.inf", None))
        self.cancelButton.setText(QCoreApplication.translate("CreatePrinterDialog", u"Abbrechen", None))
        self.createButton.setText(QCoreApplication.translate("CreatePrinterDialog", u"Erstellen", None))
    # retranslateUi

