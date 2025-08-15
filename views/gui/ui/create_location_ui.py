# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_location.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_CreateLocationDialog(object):
    def setupUi(self, CreateLocationDialog):
        if not CreateLocationDialog.objectName():
            CreateLocationDialog.setObjectName("CreateLocationDialog")
        CreateLocationDialog.resize(400, 93)
        self.verticalLayout = QVBoxLayout(CreateLocationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(CreateLocationDialog)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.locationNameEdit = QLineEdit(CreateLocationDialog)
        self.locationNameEdit.setObjectName("locationNameEdit")

        self.verticalLayout.addWidget(self.locationNameEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(CreateLocationDialog)
        self.cancelButton.setObjectName("cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.createButton = QPushButton(CreateLocationDialog)
        self.createButton.setObjectName("createButton")

        self.horizontalLayout.addWidget(self.createButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CreateLocationDialog)

        QMetaObject.connectSlotsByName(CreateLocationDialog)

    # setupUi

    def retranslateUi(self, CreateLocationDialog):
        CreateLocationDialog.setWindowTitle(
            QCoreApplication.translate(
                "CreateLocationDialog", "Standort erstellen", None
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "CreateLocationDialog", "Geben Sie den Standortnamen ein:", None
            )
        )
        self.cancelButton.setText(
            QCoreApplication.translate("CreateLocationDialog", "Abbrechen", None)
        )
        self.createButton.setText(
            QCoreApplication.translate("CreateLocationDialog", "Erstellen", None)
        )

    # retranslateUi
