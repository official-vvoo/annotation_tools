# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(901, 716)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(680, 334, 200, 311))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 201, 291))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBoxClass0 = QCheckBox(self.verticalLayoutWidget)
        self.checkBoxClass0.setObjectName(u"checkBoxClass0")

        self.horizontalLayout_2.addWidget(self.checkBoxClass0)

        self.editClass0NameBox = QToolButton(self.verticalLayoutWidget)
        self.editClass0NameBox.setObjectName(u"editClass0NameBox")

        self.horizontalLayout_2.addWidget(self.editClass0NameBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBoxClass1 = QCheckBox(self.verticalLayoutWidget)
        self.checkBoxClass1.setObjectName(u"checkBoxClass1")

        self.horizontalLayout_8.addWidget(self.checkBoxClass1)

        self.editClass1NameBox = QToolButton(self.verticalLayoutWidget)
        self.editClass1NameBox.setObjectName(u"editClass1NameBox")

        self.horizontalLayout_8.addWidget(self.editClass1NameBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBoxClass2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBoxClass2.setObjectName(u"checkBoxClass2")

        self.horizontalLayout_7.addWidget(self.checkBoxClass2)

        self.editClass2NameBox = QToolButton(self.verticalLayoutWidget)
        self.editClass2NameBox.setObjectName(u"editClass2NameBox")

        self.horizontalLayout_7.addWidget(self.editClass2NameBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBoxClass3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBoxClass3.setObjectName(u"checkBoxClass3")

        self.horizontalLayout_6.addWidget(self.checkBoxClass3)

        self.editClass3NameBox = QToolButton(self.verticalLayoutWidget)
        self.editClass3NameBox.setObjectName(u"editClass3NameBox")

        self.horizontalLayout_6.addWidget(self.editClass3NameBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBoxClass4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBoxClass4.setObjectName(u"checkBoxClass4")

        self.horizontalLayout_5.addWidget(self.checkBoxClass4)

        self.editClass4NameBox = QToolButton(self.verticalLayoutWidget)
        self.editClass4NameBox.setObjectName(u"editClass4NameBox")

        self.horizontalLayout_5.addWidget(self.editClass4NameBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBoxClass5 = QCheckBox(self.verticalLayoutWidget)
        self.checkBoxClass5.setObjectName(u"checkBoxClass5")

        self.horizontalLayout_9.addWidget(self.checkBoxClass5)

        self.editClass5NameBox = QToolButton(self.verticalLayoutWidget)
        self.editClass5NameBox.setObjectName(u"editClass5NameBox")

        self.horizontalLayout_9.addWidget(self.editClass5NameBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBoxClass6 = QCheckBox(self.verticalLayoutWidget)
        self.checkBoxClass6.setObjectName(u"checkBoxClass6")

        self.horizontalLayout_4.addWidget(self.checkBoxClass6)

        self.editClass6NameBox = QToolButton(self.verticalLayoutWidget)
        self.editClass6NameBox.setObjectName(u"editClass6NameBox")

        self.horizontalLayout_4.addWidget(self.editClass6NameBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(9, 15, 661, 631))
        self.MaskTab = QWidget()
        self.MaskTab.setObjectName(u"MaskTab")
        self.imageMaskViewer = QLabel(self.MaskTab)
        self.imageMaskViewer.setObjectName(u"imageMaskViewer")
        self.imageMaskViewer.setGeometry(QRect(8, 5, 640, 480))
        self.imageMaskViewer.setAlignment(Qt.AlignCenter)
        self.labelInfoEdit = QTextEdit(self.MaskTab)
        self.labelInfoEdit.setObjectName(u"labelInfoEdit")
        self.labelInfoEdit.setGeometry(QRect(8, 490, 640, 110))
        self.tabWidget.addTab(self.MaskTab, "")
        self.LabelTab = QWidget()
        self.LabelTab.setObjectName(u"LabelTab")
        self.labelInfoViewer = QTextBrowser(self.LabelTab)
        self.labelInfoViewer.setObjectName(u"labelInfoViewer")
        self.labelInfoViewer.setGeometry(QRect(8, 490, 640, 110))
        font = QFont()
        font.setPointSize(8)
        self.labelInfoViewer.setFont(font)
        self.imageLabelViewer = QLabel(self.LabelTab)
        self.imageLabelViewer.setObjectName(u"imageLabelViewer")
        self.imageLabelViewer.setGeometry(QRect(8, 5, 640, 480))
        self.imageLabelViewer.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.LabelTab, "")
        self.imageListViewer = QListWidget(self.centralwidget)
        self.imageListViewer.setObjectName(u"imageListViewer")
        self.imageListViewer.setGeometry(QRect(680, 25, 200, 200))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(670, 230, 213, 102))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.viewClasButton = QRadioButton(self.horizontalLayoutWidget)
        self.viewClasButton.setObjectName(u"viewClasButton")
        font1 = QFont()
        font1.setPointSize(11)
        self.viewClasButton.setFont(font1)

        self.verticalLayout.addWidget(self.viewClasButton)

        self.viewBboxButton = QRadioButton(self.horizontalLayoutWidget)
        self.viewBboxButton.setObjectName(u"viewBboxButton")
        self.viewBboxButton.setFont(font1)

        self.verticalLayout.addWidget(self.viewBboxButton)

        self.viewSegmButton = QRadioButton(self.horizontalLayoutWidget)
        self.viewSegmButton.setObjectName(u"viewSegmButton")
        self.viewSegmButton.setFont(font1)

        self.verticalLayout.addWidget(self.viewSegmButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.loadImageButton = QPushButton(self.horizontalLayoutWidget)
        self.loadImageButton.setObjectName(u"loadImageButton")

        self.verticalLayout_2.addWidget(self.loadImageButton)

        self.loadMaskButton = QPushButton(self.horizontalLayoutWidget)
        self.loadMaskButton.setObjectName(u"loadMaskButton")

        self.verticalLayout_2.addWidget(self.loadMaskButton)

        self.loadLabelButton = QPushButton(self.horizontalLayoutWidget)
        self.loadLabelButton.setObjectName(u"loadLabelButton")

        self.verticalLayout_2.addWidget(self.loadLabelButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.tabWidget.raise_()
        self.groupBox.raise_()
        self.imageListViewer.raise_()
        self.horizontalLayoutWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 901, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.imageListViewer.itemSelectionChanged.connect(MainWindow.image_selection_changed)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"View Class", None))
        self.checkBoxClass0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.editClass0NameBox.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBoxClass1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.editClass1NameBox.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBoxClass2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.editClass2NameBox.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBoxClass3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.editClass3NameBox.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBoxClass4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.editClass4NameBox.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBoxClass5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.editClass5NameBox.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBoxClass6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.editClass6NameBox.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.imageMaskViewer.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MaskTab), QCoreApplication.translate("MainWindow", u"Mask Info", None))
        self.imageLabelViewer.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LabelTab), QCoreApplication.translate("MainWindow", u"Label Info", None))
        self.viewClasButton.setText(QCoreApplication.translate("MainWindow", u"class", None))
        self.viewBboxButton.setText(QCoreApplication.translate("MainWindow", u"bbox", None))
        self.viewSegmButton.setText(QCoreApplication.translate("MainWindow", u"segmentation", None))
        self.loadImageButton.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.loadMaskButton.setText(QCoreApplication.translate("MainWindow", u"Load Mask", None))
        self.loadLabelButton.setText(QCoreApplication.translate("MainWindow", u"Load Label", None))
    # retranslateUi

