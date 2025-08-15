# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
    QAction,
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
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMenuBar,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QTabWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 555)
        self.openDocumentationAction = QAction(MainWindow)
        self.openDocumentationAction.setObjectName("openDocumentationAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.verwaltungTab = QWidget()
        self.verwaltungTab.setObjectName("verwaltungTab")
        self.verticalLayout_3 = QVBoxLayout(self.verwaltungTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.searchEdit = QLineEdit(self.verwaltungTab)
        self.searchEdit.setObjectName("searchEdit")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.searchEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.printersTreeWidget = QTreeWidget(self.verwaltungTab)
        self.printersTreeWidget.setObjectName("printersTreeWidget")

        self.verticalLayout_2.addWidget(self.printersTreeWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteItemButton = QPushButton(self.verwaltungTab)
        self.deleteItemButton.setObjectName("deleteItemButton")

        self.horizontalLayout.addWidget(self.deleteItemButton)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.editPrinterButton = QPushButton(self.verwaltungTab)
        self.editPrinterButton.setObjectName("editPrinterButton")

        self.horizontalLayout_2.addWidget(self.editPrinterButton)

        self.createItemComboBox = QComboBox(self.verwaltungTab)
        self.createItemComboBox.addItem("")
        self.createItemComboBox.addItem("")
        self.createItemComboBox.addItem("")
        self.createItemComboBox.setObjectName("createItemComboBox")

        self.horizontalLayout_2.addWidget(self.createItemComboBox)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4.setStretch(0, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.installPrinterButton = QPushButton(self.verwaltungTab)
        self.installPrinterButton.setObjectName("installPrinterButton")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.installPrinterButton.sizePolicy().hasHeightForWidth()
        )
        self.installPrinterButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.installPrinterButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.verwaltungTab, "")
        self.installedTab = QWidget()
        self.installedTab.setObjectName("installedTab")
        self.verticalLayout_4 = QVBoxLayout(self.installedTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.installedPrintersListWidget = QListWidget(self.installedTab)
        self.installedPrintersListWidget.setObjectName("installedPrintersListWidget")

        self.verticalLayout_4.addWidget(self.installedPrintersListWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uninstallPrinterButton = QPushButton(self.installedTab)
        self.uninstallPrinterButton.setObjectName("uninstallPrinterButton")

        self.horizontalLayout_5.addWidget(self.uninstallPrinterButton)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.installedPrintersRefreshButton = QPushButton(self.installedTab)
        self.installedPrintersRefreshButton.setObjectName(
            "installedPrintersRefreshButton"
        )

        self.horizontalLayout_5.addWidget(self.installedPrintersRefreshButton)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.installedTab, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 229, 449))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setBold(True)
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.driverPathLabel = QLabel(self.scrollAreaWidgetContents)
        self.driverPathLabel.setObjectName("driverPathLabel")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.driverPathLabel.sizePolicy().hasHeightForWidth()
        )
        self.driverPathLabel.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setBold(False)
        self.driverPathLabel.setFont(font1)

        self.gridLayout.addWidget(self.driverPathLabel, 5, 1, 1, 1)

        self.availableLabel = QLabel(self.scrollAreaWidgetContents)
        self.availableLabel.setObjectName("availableLabel")
        self.availableLabel.setFont(font)

        self.gridLayout.addWidget(self.availableLabel, 6, 1, 1, 1)

        self.locationLabel = QLabel(self.scrollAreaWidgetContents)
        self.locationLabel.setObjectName("locationLabel")
        sizePolicy3.setHeightForWidth(
            self.locationLabel.sizePolicy().hasHeightForWidth()
        )
        self.locationLabel.setSizePolicy(sizePolicy3)
        self.locationLabel.setFont(font1)

        self.gridLayout.addWidget(self.locationLabel, 0, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.DNSNameLabel = QLabel(self.scrollAreaWidgetContents)
        self.DNSNameLabel.setObjectName("DNSNameLabel")
        sizePolicy3.setHeightForWidth(
            self.DNSNameLabel.sizePolicy().hasHeightForWidth()
        )
        self.DNSNameLabel.setSizePolicy(sizePolicy3)
        self.DNSNameLabel.setFont(font1)

        self.gridLayout.addWidget(self.DNSNameLabel, 3, 1, 1, 1)

        self.printerNameLabel = QLabel(self.scrollAreaWidgetContents)
        self.printerNameLabel.setObjectName("printerNameLabel")
        sizePolicy3.setHeightForWidth(
            self.printerNameLabel.sizePolicy().hasHeightForWidth()
        )
        self.printerNameLabel.setSizePolicy(sizePolicy3)
        self.printerNameLabel.setFont(font1)

        self.gridLayout.addWidget(self.printerNameLabel, 1, 1, 1, 1)

        self.printerModelLabel = QLabel(self.scrollAreaWidgetContents)
        self.printerModelLabel.setObjectName("printerModelLabel")
        sizePolicy3.setHeightForWidth(
            self.printerModelLabel.sizePolicy().hasHeightForWidth()
        )
        self.printerModelLabel.setSizePolicy(sizePolicy3)
        self.printerModelLabel.setFont(font1)

        self.gridLayout.addWidget(self.printerModelLabel, 2, 1, 1, 1)

        self.driverNameLabel = QLabel(self.scrollAreaWidgetContents)
        self.driverNameLabel.setObjectName("driverNameLabel")
        sizePolicy3.setHeightForWidth(
            self.driverNameLabel.sizePolicy().hasHeightForWidth()
        )
        self.driverNameLabel.setSizePolicy(sizePolicy3)
        self.driverNameLabel.setFont(font1)

        self.gridLayout.addWidget(self.driverNameLabel, 4, 1, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy4)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_5.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 33))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.openDocumentationAction)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Drucker Verwaltung", None)
        )
        self.openDocumentationAction.setText(
            QCoreApplication.translate("MainWindow", "Dokuseite \u00f6ffnen", None)
        )
        # if QT_CONFIG(shortcut)
        self.openDocumentationAction.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+H", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.searchEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                "Geben Sie den Druckernamen, Standort oder Domänennamen ein...",
                None,
            )
        )
        ___qtreewidgetitem = self.printersTreeWidget.headerItem()
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "Standort", None)
        )
        self.deleteItemButton.setText(
            QCoreApplication.translate("MainWindow", "L\u00f6schen", None)
        )
        # if QT_CONFIG(shortcut)
        self.deleteItemButton.setShortcut(
            QCoreApplication.translate("MainWindow", "Del", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.editPrinterButton.setText(
            QCoreApplication.translate("MainWindow", "Bearbeiten", None)
        )
        # if QT_CONFIG(shortcut)
        self.editPrinterButton.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+E", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.createItemComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", "Erstellen neuen...", None)
        )
        self.createItemComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", "Drucker", None)
        )
        self.createItemComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", "Standort", None)
        )

        self.installPrinterButton.setText(
            QCoreApplication.translate("MainWindow", "Installieren", None)
        )
        # if QT_CONFIG(shortcut)
        self.installPrinterButton.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+I", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.verwaltungTab),
            QCoreApplication.translate("MainWindow", "Druckerverwaltung", None),
        )
        self.uninstallPrinterButton.setText(
            QCoreApplication.translate("MainWindow", "Deinstallieren", None)
        )
        self.installedPrintersRefreshButton.setText(
            QCoreApplication.translate("MainWindow", "Aktualisieren", None)
        )
        # if QT_CONFIG(shortcut)
        self.installedPrintersRefreshButton.setShortcut(
            QCoreApplication.translate("MainWindow", "F5", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.installedTab),
            QCoreApplication.translate("MainWindow", "Installierte Drucker", None),
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Verf\u00fcgbar:", None)
        )
        self.driverPathLabel.setText(
            QCoreApplication.translate("MainWindow", "N/A", None)
        )
        self.availableLabel.setText(
            QCoreApplication.translate("MainWindow", "N/A", None)
        )
        self.locationLabel.setText(
            QCoreApplication.translate("MainWindow", "N/A", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "Standort:", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "Treibername:", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Druckermodell:", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "Treiberpfad:", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Druckername:", None)
        )
        self.DNSNameLabel.setText(QCoreApplication.translate("MainWindow", "N/A", None))
        self.printerNameLabel.setText(
            QCoreApplication.translate("MainWindow", "N/A", None)
        )
        self.printerModelLabel.setText(
            QCoreApplication.translate("MainWindow", "N/A", None)
        )
        self.driverNameLabel.setText(
            QCoreApplication.translate("MainWindow", "N/A", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", "DNS-Name:", None)
        )
        self.progressBar.setFormat("")
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Hilfe", None))

    # retranslateUi
