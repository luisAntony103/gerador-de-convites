# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_GeradorConvite(object):
    def setupUi(self, GeradorConvite):
        if not GeradorConvite.objectName():
            GeradorConvite.setObjectName(u"GeradorConvite")
        GeradorConvite.resize(825, 728)
        self.centralwidget = QWidget(GeradorConvite)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.key_box = QVBoxLayout()
        self.key_box.setObjectName(u"key_box")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.key_box.addItem(self.verticalSpacer_3)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.key_box.addWidget(self.label_10)

        self.key_list = QListWidget(self.centralwidget)
        self.key_list.setObjectName(u"key_list")

        self.key_box.addWidget(self.key_list)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.key_box.addWidget(self.label_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.key_box.addItem(self.verticalSpacer_4)


        self.gridLayout_3.addLayout(self.key_box, 0, 2, 1, 1)

        self.form = QGridLayout()
        self.form.setObjectName(u"form")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.form.addWidget(self.label_8, 10, 0, 1, 1)

        self.findInvite = QPushButton(self.centralwidget)
        self.findInvite.setObjectName(u"findInvite")

        self.form.addWidget(self.findInvite, 2, 0, 1, 1)

        self.destination_path = QLabel(self.centralwidget)
        self.destination_path.setObjectName(u"destination_path")

        self.form.addWidget(self.destination_path, 11, 1, 1, 1)

        self.findList = QPushButton(self.centralwidget)
        self.findList.setObjectName(u"findList")

        self.form.addWidget(self.findList, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.form.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.form.addWidget(self.label_4, 4, 0, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.form.addWidget(self.label_5, 5, 0, 1, 2)

        self.findDestination = QPushButton(self.centralwidget)
        self.findDestination.setObjectName(u"findDestination")

        self.form.addWidget(self.findDestination, 11, 0, 1, 1)

        self.list_path = QLabel(self.centralwidget)
        self.list_path.setObjectName(u"list_path")

        self.form.addWidget(self.list_path, 7, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.form.addWidget(self.label_2, 0, 0, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.form.addWidget(self.label_3, 1, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.form.addItem(self.verticalSpacer_2, 8, 0, 1, 2)

        self.invite_path = QLabel(self.centralwidget)
        self.invite_path.setObjectName(u"invite_path")

        self.form.addWidget(self.invite_path, 2, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.form.addWidget(self.label_7, 9, 0, 1, 2)


        self.gridLayout_3.addLayout(self.form, 0, 0, 1, 1)

        self.confirm = QGridLayout()
        self.confirm.setObjectName(u"confirm")
        self.generateInvites = QPushButton(self.centralwidget)
        self.generateInvites.setObjectName(u"generateInvites")

        self.confirm.addWidget(self.generateInvites, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.confirm.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.confirm.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.invite_progress_bar = QProgressBar(self.centralwidget)
        self.invite_progress_bar.setObjectName(u"invite_progress_bar")
        self.invite_progress_bar.setValue(0)

        self.confirm.addWidget(self.invite_progress_bar, 1, 0, 1, 3)


        self.gridLayout_3.addLayout(self.confirm, 1, 0, 1, 3)

        self.espaco = QVBoxLayout()
        self.espaco.setObjectName(u"espaco")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.espaco.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.espaco, 0, 1, 1, 1)

        GeradorConvite.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(GeradorConvite)
        self.statusbar.setObjectName(u"statusbar")
        GeradorConvite.setStatusBar(self.statusbar)

        self.retranslateUi(GeradorConvite)

        QMetaObject.connectSlotsByName(GeradorConvite)
    # setupUi

    def retranslateUi(self, GeradorConvite):
        GeradorConvite.setWindowTitle(QCoreApplication.translate("GeradorConvite", u"MainWindow", None))
        self.label_10.setText(QCoreApplication.translate("GeradorConvite", u"Palavras-chaves", None))
        self.label_11.setText(QCoreApplication.translate("GeradorConvite", u"Clique duas vezes para copiar a chave", None))
        self.label_8.setText(QCoreApplication.translate("GeradorConvite", u"Requer: Pasta", None))
        self.findInvite.setText(QCoreApplication.translate("GeradorConvite", u"Encontrar convite", None))
        self.destination_path.setText(QCoreApplication.translate("GeradorConvite", u"Nenhum arquivo selecionado", None))
        self.findList.setText(QCoreApplication.translate("GeradorConvite", u"Encontrar plan\u00edlia", None))
        self.label_4.setText(QCoreApplication.translate("GeradorConvite", u"Arquivo da plan\u00edlia", None))
        self.label_5.setText(QCoreApplication.translate("GeradorConvite", u"Requer: Plan\u00edlias (.xlsx, .xls, .csv)", None))
        self.findDestination.setText(QCoreApplication.translate("GeradorConvite", u"Encontrar Pasta", None))
        self.list_path.setText(QCoreApplication.translate("GeradorConvite", u"Nenhum arquivo selecionado", None))
        self.label_2.setText(QCoreApplication.translate("GeradorConvite", u"Arquivo do convite:", None))
        self.label_3.setText(QCoreApplication.translate("GeradorConvite", u"Requer: WORD (.docx)", None))
        self.invite_path.setText(QCoreApplication.translate("GeradorConvite", u"Nenhum arquivo selecionado", None))
        self.label_7.setText(QCoreApplication.translate("GeradorConvite", u"Pasta de sa\u00edda:", None))
        self.generateInvites.setText(QCoreApplication.translate("GeradorConvite", u"Gerar convites", None))
    # retranslateUi

