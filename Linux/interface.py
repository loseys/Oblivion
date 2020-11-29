#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import content_rc
import random

class Ui_MainWindow(object):
    """
    Oblivion GUI.
    """
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(891, 570)
        MainWindow.setMinimumSize(QSize(891, 570))
        MainWindow.setMaximumSize(QSize(891, 570))
        icon = QIcon()
        icon.addFile(u":/menu/media/oblivion-256.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setGeometry(QRect(0, 0, 171, 581))
        self.frame_menu.setBaseSize(QSize(1, 0))
        font = QFont()
        font.setKerning(False)
        self.frame_menu.setFont(font)
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.menu_analisar = QCommandLinkButton(self.frame_menu)
        self.menu_analisar.setObjectName(u"menu_analisar")
        self.menu_analisar.setGeometry(QRect(20, 70, 121, 30))
        self.menu_analisar.setMaximumSize(QSize(16777215, 16777215))
        self.menu_analisar.setSizeIncrement(QSize(0, 0))
        self.menu_analisar.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setKerning(True)
        self.menu_analisar.setFont(font1)
        self.menu_analisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_analisar.setStyleSheet(u"color: rgb(51, 51, 51);")
        icon1 = QIcon()
        icon1.addFile(u":/menu/media/menu_scan2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_analisar.setIcon(icon1)
        self.menu_analisar.setIconSize(QSize(24, 16))
        self.menu_modulos = QCommandLinkButton(self.frame_menu)
        self.menu_modulos.setObjectName(u"menu_modulos")
        self.menu_modulos.setGeometry(QRect(20, 180, 121, 30))
        self.menu_modulos.setMaximumSize(QSize(16777215, 16777215))
        self.menu_modulos.setSizeIncrement(QSize(0, 0))
        self.menu_modulos.setBaseSize(QSize(0, 0))
        self.menu_modulos.setFont(font1)
        self.menu_modulos.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_modulos.setStyleSheet(u"color: rgb(51, 51, 51);")
        icon2 = QIcon()
        icon2.addFile(u":/menu/media/menu_modules.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_modulos.setIcon(icon2)
        self.menu_modulos.setIconSize(QSize(24, 16))
        self.menu_analises = QCommandLinkButton(self.frame_menu)
        self.menu_analises.setObjectName(u"menu_analises")
        self.menu_analises.setGeometry(QRect(20, 100, 121, 30))
        self.menu_analises.setMaximumSize(QSize(16777215, 16777215))
        self.menu_analises.setSizeIncrement(QSize(0, 0))
        self.menu_analises.setBaseSize(QSize(0, 0))
        self.menu_analises.setFont(font1)
        self.menu_analises.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_analises.setStyleSheet(u"color: rgb(51, 51, 51);")
        icon3 = QIcon()
        icon3.addFile(u":/menu/media/menu_folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_analises.setIcon(icon3)
        self.menu_analises.setIconSize(QSize(24, 16))
        self.label_analise_2 = QLabel(self.frame_menu)
        self.label_analise_2.setObjectName(u"label_analise_2")
        self.label_analise_2.setGeometry(QRect(30, 50, 61, 16))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_analise_2.setFont(font2)
        self.label_analise_2.setStyleSheet(u"color: rgb(171, 171, 171);")
        self.label_outros = QLabel(self.frame_menu)
        self.label_outros.setObjectName(u"label_outros")
        self.label_outros.setGeometry(QRect(30, 160, 61, 16))
        self.label_outros.setFont(font2)
        self.label_outros.setStyleSheet(u"color: rgb(171, 171, 171);")
        self.menu_agendar = QCommandLinkButton(self.frame_menu)
        self.menu_agendar.setObjectName(u"menu_agendar")
        self.menu_agendar.setGeometry(QRect(20, 210, 121, 30))
        self.menu_agendar.setMaximumSize(QSize(16777215, 16777215))
        self.menu_agendar.setSizeIncrement(QSize(0, 0))
        self.menu_agendar.setBaseSize(QSize(0, 0))
        self.menu_agendar.setFont(font1)
        self.menu_agendar.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_agendar.setStyleSheet(u"color: rgb(51, 51, 51);")
        icon4 = QIcon()
        icon4.addFile(u":/menu/media/menu_clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_agendar.setIcon(icon4)
        self.menu_agendar.setIconSize(QSize(24, 16))
        self.line = QFrame(self.frame_menu)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(168, 35, 2, 541))
        font3 = QFont()
        font3.setFamily(u"Nachlieli CLM")
        font3.setKerning(False)
        self.line.setFont(font3)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.menu_decodificar = QCommandLinkButton(self.frame_menu)
        self.menu_decodificar.setObjectName(u"menu_decodificar")
        self.menu_decodificar.setGeometry(QRect(20, 240, 121, 30))
        self.menu_decodificar.setMaximumSize(QSize(16777215, 16777215))
        self.menu_decodificar.setSizeIncrement(QSize(0, 0))
        self.menu_decodificar.setBaseSize(QSize(0, 0))
        self.menu_decodificar.setFont(font1)
        self.menu_decodificar.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_decodificar.setStyleSheet(u"color: rgb(51, 51, 51);")
        icon5 = QIcon()
        icon5.addFile(u":/menu/media/menu_decodificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_decodificar.setIcon(icon5)
        self.menu_decodificar.setIconSize(QSize(24, 16))
        self.menu_ajuda = QCommandLinkButton(self.frame_menu)
        self.menu_ajuda.setObjectName(u"menu_ajuda")
        self.menu_ajuda.setGeometry(QRect(18, 268, 121, 30))
        self.menu_ajuda.setMaximumSize(QSize(16777215, 16777215))
        self.menu_ajuda.setSizeIncrement(QSize(0, 0))
        self.menu_ajuda.setBaseSize(QSize(0, 0))
        self.menu_ajuda.setFont(font1)
        self.menu_ajuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_ajuda.setStyleSheet(u"color: rgb(51, 51, 51);")
        icon6 = QIcon()
        icon6.addFile(u":/menu/media/menu_help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_ajuda.setIcon(icon6)
        self.menu_ajuda.setIconSize(QSize(30, 19))
        self.menu_analisar.raise_()
        self.menu_modulos.raise_()
        self.label_analise_2.raise_()
        self.label_outros.raise_()
        self.menu_agendar.raise_()
        self.line.raise_()
        self.menu_decodificar.raise_()
        self.menu_analises.raise_()
        self.menu_ajuda.raise_()
        self.frame_analisar = QFrame(self.centralwidget)
        self.frame_analisar.setObjectName(u"frame_analisar")
        self.frame_analisar.setGeometry(QRect(169, 31, 731, 551))
        self.frame_analisar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_analisar.setFrameShape(QFrame.StyledPanel)
        self.frame_analisar.setFrameShadow(QFrame.Raised)
        self.label_analise = QLabel(self.frame_analisar)
        self.label_analise.setObjectName(u"label_analise")
        self.label_analise.setGeometry(QRect(20, 13, 101, 21))
        font4 = QFont()
        font4.setFamily(u"Source Sans Pro ExtraLight")
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_analise.setFont(font4)
        self.label_analise.setStyleSheet(u"color: rgb(51, 51, 51);")
        self.line_5 = QFrame(self.frame_analisar)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(-1, 49, 802, 2))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.tabwidget_analise_config = QTabWidget(self.frame_analisar)
        self.tabwidget_analise_config.setObjectName(u"tabwidget_analise_config")
        self.tabwidget_analise_config.setGeometry(QRect(20, 68, 681, 451))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        self.tabwidget_analise_config.setFont(font5)
        self.tabwidget_analise_config.setStyleSheet(u"background-color:None;")
        self.tabwidget_analise_config.setTabPosition(QTabWidget.North)
        self.tabwidget_analise_config.setTabShape(QTabWidget.Rounded)
        self.tabwidget_analise_config.setElideMode(Qt.ElideNone)
        self.tabwidget_analise_config.setUsesScrollButtons(True)
        self.tabwidget_analise_config.setDocumentMode(False)
        self.tabwidget_analise_config.setTabsClosable(False)
        self.tabwidget_analise_config.setMovable(True)
        self.tabwidget_analise_config.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(12, 10, 651, 71))
        self.formLayoutWidget_3 = QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 20, 361, 51))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.db_delay = QDoubleSpinBox(self.formLayoutWidget_3)
        self.db_delay.setObjectName(u"db_delay")
        self.db_delay.setMaximum(9999999)
        self.db_delay.setMinimum(3)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.db_delay)

        self.db_looping = QCheckBox(self.formLayoutWidget_3)
        self.db_looping.setObjectName(u"db_looping")
        font6 = QFont()
        font6.setPointSize(9)
        self.db_looping.setFont(font6)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.db_looping)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(12, 90, 651, 81))
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 361, 51))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.db_fechar = QCheckBox(self.verticalLayoutWidget_3)
        self.db_fechar.setObjectName(u"db_fechar")
        self.db_fechar.setFont(font6)

        self.verticalLayout_3.addWidget(self.db_fechar)

        self.db_desligar = QCheckBox(self.verticalLayoutWidget_3)
        self.db_desligar.setObjectName(u"db_desligar")
        self.db_desligar.setFont(font6)

        self.verticalLayout_3.addWidget(self.db_desligar)

        self.tabwidget_analise_config.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayoutWidget = QWidget(self.tab_5)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 641, 266))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.config_modulos = QTreeWidget(self.verticalLayoutWidget)
        self.modulos_modulos_dataleak = QTreeWidgetItem(self.config_modulos)
        self.modulos_modulos_dataleak_common = QTreeWidgetItem(self.modulos_modulos_dataleak)
        self.modulos_modulos_dataleak_common.setCheckState(0, Qt.Unchecked);
        #self.modulos_modulos_dataleak_personalizada = QTreeWidgetItem(self.modulos_modulos_dataleak)
        #self.modulos_modulos_dataleak_personalizada.setCheckState(0, Qt.Unchecked);
        self.modulos_modulos_dataleak_googledorks = QTreeWidgetItem(self.modulos_modulos_dataleak)
        self.modulos_modulos_dataleak_googledorks.setCheckState(0, Qt.Unchecked);
        self.modulos_modulos_dataleak_wordlist = QTreeWidgetItem(self.modulos_modulos_dataleak)
        self.modulos_modulos_dataleak_wordlist.setCheckState(0, Qt.Unchecked);
        self.modulos_modulos_dataleak_api = QTreeWidgetItem(self.modulos_modulos_dataleak)
        self.modulos_modulos_dataleak_api.setCheckState(0, Qt.Unchecked);
        #self.modulos_modulos_naturallanguage = QTreeWidgetItem(self.config_modulos)
        #self.modulos_modulos_naturallanguage.setCheckState(0, Qt.Unchecked);
        self.modulos_modulos_vulscan = QTreeWidgetItem(self.config_modulos)
        self.modulos_modulos_vulscan.setCheckState(0, Qt.Unchecked);
        self.config_modulos.setObjectName(u"config_modulos")
        self.config_modulos.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.config_modulos)

        self.tabwidget_analise_config.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.config_formatos = QTreeWidget(self.tab_6)
        self.formatos = QTreeWidgetItem(self.config_formatos)
        self.formatos_copia = QTreeWidgetItem(self.formatos)
        self.formatos_copia_dadobruto = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_dadobruto.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_txt = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_txt.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_txt_ocult = QTreeWidgetItem(self.formatos_copia_txt)
        self.formatos_copia_txt_ocult.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_txt_cript = QTreeWidgetItem(self.formatos_copia_txt)
        self.formatos_copia_txt_cript.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_docx = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_docx.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_docx_ocult = QTreeWidgetItem(self.formatos_copia_docx)
        self.formatos_copia_docx_ocult.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_docx_cript = QTreeWidgetItem(self.formatos_copia_docx)
        self.formatos_copia_docx_cript.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_pdf = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_pdf.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_pdf_ocult = QTreeWidgetItem(self.formatos_copia_pdf)
        self.formatos_copia_pdf_ocult.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_pdf_cript = QTreeWidgetItem(self.formatos_copia_pdf)
        self.formatos_copia_pdf_cript.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_xlsx = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_xlsx.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_xlsx_ocult = QTreeWidgetItem(self.formatos_copia_xlsx)
        self.formatos_copia_xlsx_ocult.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_xlsx_cript = QTreeWidgetItem(self.formatos_copia_xlsx)
        self.formatos_copia_xlsx_cript.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_json = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_json.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_json_ocult = QTreeWidgetItem(self.formatos_copia_json)
        self.formatos_copia_json_ocult.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_json_cript = QTreeWidgetItem(self.formatos_copia_json)
        self.formatos_copia_json_cript.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_html = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_html.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_html_ocult = QTreeWidgetItem(self.formatos_copia_html)
        self.formatos_copia_html_ocult.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_html_cript = QTreeWidgetItem(self.formatos_copia_html)
        self.formatos_copia_html_cript.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_xls = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_xls.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_xls_ocult = QTreeWidgetItem(self.formatos_copia_xls)
        self.formatos_copia_xls_ocult.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_xls_cript = QTreeWidgetItem(self.formatos_copia_xls)
        self.formatos_copia_xls_cript.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_db = QTreeWidgetItem(self.formatos_copia)
        self.formatos_copia_db.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_db_ocult = QTreeWidgetItem(self.formatos_copia_db)
        self.formatos_copia_db_ocult.setCheckState(0, Qt.Unchecked);
        self.formatos_copia_db_cript = QTreeWidgetItem(self.formatos_copia_db)
        self.formatos_copia_db_cript.setCheckState(0, Qt.Unchecked);
        self.formatos_gerar_email = QTreeWidgetItem(self.formatos)
        self.formatos_gerar_email_dadobruto = QTreeWidgetItem(self.formatos_gerar_email)
        self.formatos_gerar_email_dadobruto.setCheckState(0, Qt.Unchecked);
        self.config_formatos.setObjectName(u"config_formatos")
        self.config_formatos.setGeometry(QRect(20, 10, 656, 391))
        self.config_formatos.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.config_formatos.setFrameShape(QFrame.NoFrame)
        self.config_formatos.setFrameShadow(QFrame.Plain)
        self.config_formatos.setHeaderHidden(False)
        self.config_formatos.header().setCascadingSectionResizes(False)
        self.tabwidget_analise_config.addTab(self.tab_6, "")
        self.analise_salvar = QPushButton(self.frame_analisar)
        self.analise_salvar.setObjectName(u"analise_salvar")
        self.analise_salvar.setGeometry(QRect(527, 18, 71, 23))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        self.analise_salvar.setFont(font7)
        self.analise_salvar.setStyleSheet(u"color: None;\n"
"background-color: None;")
        self.analise_nova_analise = QPushButton(self.frame_analisar)
        self.analise_nova_analise.setObjectName(u"analise_nova_analise")
        self.analise_nova_analise.setGeometry(QRect(608, 18, 101, 23))
        self.analise_nova_analise.setFont(font7)
        self.analise_nova_analise.setStyleSheet(u"color: None;\n"
"background-color: None;")
        icon7 = QIcon()
        icon7.addFile(u":/menu/media/analise_icone_analisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.analise_nova_analise.setIcon(icon7)
        self.analise_nova_analise.setIconSize(QSize(15, 16))
        self.widget_faixa = QWidget(self.centralwidget)
        self.widget_faixa.setObjectName(u"widget_faixa")
        self.widget_faixa.setGeometry(QRect(0, 0, 991, 31))
        self.widget_faixa.setStyleSheet(u"background-color: rgb(23, 44, 64);")
        self.widget_menu = QWidget(self.widget_faixa)
        self.widget_menu.setObjectName(u"widget_menu")
        self.widget_menu.setGeometry(QRect(6, 0, 119, 31))
        #faixada aqui
        #self.widget_menu.setStyleSheet(u"background-color: rgb(38, 55, 70);\n"
#"image: url(:/menu/media/oblivion_logo.png);")
        self.menu_configuracoes = QCommandLinkButton(self.widget_faixa)
        self.menu_configuracoes.setObjectName(u"menu_configuracoes")
        self.menu_configuracoes.setGeometry(QRect(812, -2, 32, 33))
        self.menu_configuracoes.setMaximumSize(QSize(16777215, 16777215))
        self.menu_configuracoes.setSizeIncrement(QSize(0, 0))
        self.menu_configuracoes.setBaseSize(QSize(0, 0))
        self.menu_configuracoes.setFont(font1)
        self.menu_configuracoes.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_configuracoes.setStyleSheet(u"color:None;\n"
"background-color:None;")
        icon8 = QIcon()
        icon8.addFile(u":/menu/media/menu_settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_configuracoes.setIcon(icon8)
        self.menu_configuracoes.setIconSize(QSize(24, 17))
        self.commandLinkButton = QCommandLinkButton(self.widget_faixa)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(846, -3, 32, 33))
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"color:None;\n"
"background-color:None;")
        icon9 = QIcon()
        icon9.addFile(u":/menu/media/analise_notification.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon9)
        self.commandLinkButton.setIconSize(QSize(24, 18))
        self.frame_analises = QFrame(self.centralwidget)
        self.frame_analises.setObjectName(u"frame_analises")
        self.frame_analises.setGeometry(QRect(169, 31, 731, 551))
        self.frame_analises.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_analises.setFrameShape(QFrame.StyledPanel)
        self.frame_analises.setFrameShadow(QFrame.Raised)
        self.label_analises = QLabel(self.frame_analises)
        self.label_analises.setObjectName(u"label_analises")
        self.label_analises.setGeometry(QRect(20, 7, 191, 33))
        self.label_analises.setFont(font4)
        self.label_analises.setStyleSheet(u"color: rgb(51, 51, 51);")
        self.line_7 = QFrame(self.frame_analises)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(-1, 49, 802, 2))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.tabWidget = QTabWidget(self.frame_analises)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 68, 681, 451))
        self.tabWidget.setFont(font7)
        self.tabWidget.setMovable(True)
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.listWidget_2 = QListWidget(self.tab_13)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(6, 3, 669, 411))
        self.listWidget_2.setFrameShape(QFrame.NoFrame)
        self.listWidget_2.setFrameShadow(QFrame.Sunken)
        self.listWidget_2.setMovement(QListView.Static)
        self.listWidget_2.setViewMode(QListView.ListMode)
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        #self.listWidget_3 = QListWidget(self.tab_14)
        #self.listWidget_3.setObjectName(u"listWidget_3")
        #self.listWidget_3.setGeometry(QRect(6, 3, 661, 411))
        #self.listWidget_3.setFrameShape(QFrame.NoFrame)
        #self.listWidget_3.setFrameShadow(QFrame.Sunken)
        #self.listWidget_3.setMovement(QListView.Static)
        #self.listWidget_3.setViewMode(QListView.ListMode)
        #self.tabWidget.addTab(self.tab_14, "")
        self.frame_modulos = QFrame(self.centralwidget)
        self.frame_modulos.setObjectName(u"frame_modulos")
        self.frame_modulos.setGeometry(QRect(169, 31, 731, 551))
        self.frame_modulos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_modulos.setFrameShape(QFrame.StyledPanel)
        self.frame_modulos.setFrameShadow(QFrame.Raised)
        self.label_modulos = QLabel(self.frame_modulos)
        self.label_modulos.setObjectName(u"label_modulos")
        self.label_modulos.setGeometry(QRect(20, 13, 191, 21))
        self.label_modulos.setFont(font4)
        self.label_modulos.setStyleSheet(u"color: rgb(51, 51, 51);")
        self.line_8 = QFrame(self.frame_modulos)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(-1, 49, 802, 2))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.tabWidget_modulos = QTabWidget(self.frame_modulos)
        self.tabWidget_modulos.setObjectName(u"tabWidget_modulos")
        self.tabWidget_modulos.setGeometry(QRect(20, 68, 681, 451))
        self.tabWidget_modulos.setFont(font7)
        self.tabWidget_modulos.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget_modulos.setMovable(True)
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.widget_2 = QWidget(self.tab_15)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(25, 20, 121, 121))
        self.toolButton_4 = QToolButton(self.widget_2)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(22, 0, 71, 61))
        font8 = QFont()
        font8.setPointSize(7)
        self.toolButton_4.setFont(font8)
        self.toolButton_4.setStyleSheet(u"\n"
"background-color: None;\n"
"border-style: outset;\n"
"border-radius:1px;\n"
"padding: 6px;\n"
"min-width:10px;")
        icon10 = QIcon()
        icon10.addFile(u":/modulos/media/modulo_leak.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon10)
        self.toolButton_4.setIconSize(QSize(68, 64))
        self.label_17 = QLabel(self.widget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(25, 61, 81, 16))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_17.setFont(font9)
        self.label_18 = QLabel(self.widget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(2, 81, 111, 31))
        self.label_18.setStyleSheet(u"color: rgb(98, 98, 98);")
        icon11 = QIcon()
        icon11.addFile(u":/modulos/media/modulo_natural_language.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12 = QIcon()
        icon12.addFile(u":/modulos/media/modulo_idioma.png", QSize(), QIcon.Normal, QIcon.Off)
        self.widget_10 = QWidget(self.tab_15)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(130, 20, 121, 111))
        self.toolButton_13 = QToolButton(self.widget_10)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setGeometry(QRect(29, 0, 71, 61))
        self.toolButton_13.setFont(font8)
        self.toolButton_13.setStyleSheet(u"\n"
"background-color: None;\n"
"border-style: outset;\n"
"border-radius:1px;\n"
"padding: 6px;\n"
"min-width:10px;")
        icon13 = QIcon()
        icon13.addFile(u":/modulos/media/modulo_vulnerabilidades.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_13.setIcon(icon13)
        self.toolButton_13.setIconSize(QSize(68, 64))
        self.label_35 = QLabel(self.widget_10)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(20, 61, 100, 16))
        self.label_35.setFont(font9)
        self.label_36 = QLabel(self.widget_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(20, 81, 111, 31))
        self.label_36.setStyleSheet(u"color: rgb(98, 98, 98);")
        self.tabWidget_modulos.addTab(self.tab_15, "")
        self.widget_2.raise_()
        self.widget_10.raise_()
        self.frame_agendar = QFrame(self.centralwidget)
        self.frame_agendar.setObjectName(u"frame_agendar")
        self.frame_agendar.setGeometry(QRect(169, 31, 731, 551))
        self.frame_agendar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_agendar.setFrameShape(QFrame.StyledPanel)
        self.frame_agendar.setFrameShadow(QFrame.Raised)
        self.label_analises_3 = QLabel(self.frame_agendar)
        self.label_analises_3.setObjectName(u"label_analises_3")
        self.label_analises_3.setGeometry(QRect(20, 3, 220, 41))
        self.label_analises_3.setFont(font4)
        self.label_analises_3.setStyleSheet(u"color: rgb(51, 51, 51);")
        self.line_10 = QFrame(self.frame_agendar)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(-1, 49, 802, 2))
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.tabWidget_3 = QTabWidget(self.frame_agendar)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(20, 68, 681, 451))
        self.tabWidget_3.setFont(font7)
        self.tabWidget_3.setMovable(True)
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.calendarWidget = QCalendarWidget(self.tab_18)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 10, 341, 183))
        self.calendarWidget.setStyleSheet(u"background-color: none;")
        self.calendarWidget.setGridVisible(True)
        self.formLayoutWidget = QWidget(self.tab_18)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 210, 341, 201))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.dateEdit = QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEdit)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.timeEdit = QTimeEdit(self.formLayoutWidget)
        self.timeEdit.setObjectName(u"timeEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.timeEdit)

        self.plainTextEdit = QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.plainTextEdit)

        self.config_agenda = QTreeWidget(self.tab_18)
        self.agenda_modulos = QTreeWidgetItem(self.config_agenda)
        self.agenda_modulos_vulscan = QTreeWidgetItem(self.agenda_modulos)
        self.agenda_modulos_vulscan.setCheckState(0, Qt.Unchecked);
        #self.agenda_modulos_naturallanguage = QTreeWidgetItem(self.agenda_modulos)
        #self.agenda_modulos_naturallanguage.setCheckState(0, Qt.Unchecked);
        self.agenda_modulos_dataleak = QTreeWidgetItem(self.agenda_modulos)
        #self.agenda_modulos_sitespersonalizados = QTreeWidgetItem(self.agenda_modulos_dataleak)
        #self.agenda_modulos_sitespersonalizados.setCheckState(0, Qt.Unchecked);
        self.agenda_modulos_commonwebsites = QTreeWidgetItem(self.agenda_modulos_dataleak)
        self.agenda_modulos_commonwebsites.setCheckState(0, Qt.Unchecked);
        self.agenda_modulos_googledorks = QTreeWidgetItem(self.agenda_modulos_dataleak)
        self.agenda_modulos_googledorks.setCheckState(0, Qt.Unchecked);
        self.agenda_modulos_wordlists = QTreeWidgetItem(self.agenda_modulos_dataleak)
        self.agenda_modulos_wordlists.setCheckState(0, Qt.Unchecked);
        self.agenda_modulos_leak_api = QTreeWidgetItem(self.agenda_modulos_dataleak)
        self.agenda_modulos_leak_api.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar = QTreeWidgetItem(self.config_agenda)
        self.agenda_gerar_copia = QTreeWidgetItem(self.agenda_gerar)
        self.agenda_gerar_copia_dadobruto = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_dadobruto.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_txt = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_txt.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_txt_ocult = QTreeWidgetItem(self.agenda_gerar_copia_txt)
        self.agenda_gerar_copia_txt_ocult.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_txt_cript = QTreeWidgetItem(self.agenda_gerar_copia_txt)
        self.agenda_gerar_copia_txt_cript.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_docx = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_docx.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_docx_ocult = QTreeWidgetItem(self.agenda_gerar_copia_docx)
        self.agenda_gerar_copia_docx_ocult.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_docx_cript = QTreeWidgetItem(self.agenda_gerar_copia_docx)
        self.agenda_gerar_copia_docx_cript.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_pdf = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_pdf.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_pdf_ocult = QTreeWidgetItem(self.agenda_gerar_copia_pdf)
        self.agenda_gerar_copia_pdf_ocult.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_pdf_cript = QTreeWidgetItem(self.agenda_gerar_copia_pdf)
        self.agenda_gerar_copia_pdf_cript.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_xlsx = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_xlsx.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_xlsx_ocult = QTreeWidgetItem(self.agenda_gerar_copia_xlsx)
        self.agenda_gerar_copia_xlsx_ocult.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_xlsx_cript = QTreeWidgetItem(self.agenda_gerar_copia_xlsx)
        self.agenda_gerar_copia_xlsx_cript.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_json = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_json.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_json_ocult = QTreeWidgetItem(self.agenda_gerar_copia_json)
        self.agenda_gerar_copia_json_ocult.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_json_cript = QTreeWidgetItem(self.agenda_gerar_copia_json)
        self.agenda_gerar_copia_json_cript.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_html = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_html.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_html_ocult = QTreeWidgetItem(self.agenda_gerar_copia_html)
        self.agenda_gerar_copia_html_ocult.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_html_cript = QTreeWidgetItem(self.agenda_gerar_copia_html)
        self.agenda_gerar_copia_html_cript.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_xsl = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_xsl.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_xsl_ocult = QTreeWidgetItem(self.agenda_gerar_copia_xsl)
        self.agenda_gerar_copia_xsl_ocult.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_xsl_cript = QTreeWidgetItem(self.agenda_gerar_copia_xsl)
        self.agenda_gerar_copia_xsl_cript.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_db = QTreeWidgetItem(self.agenda_gerar_copia)
        self.agenda_gerar_copia_db.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_db_ocult = QTreeWidgetItem(self.agenda_gerar_copia_db)
        self.agenda_gerar_copia_db_ocult.setCheckState(0, Qt.Unchecked);
        self.agenda_gerar_copia_db_cript = QTreeWidgetItem(self.agenda_gerar_copia_db)
        self.agenda_gerar_copia_db_cript.setCheckState(0, Qt.Unchecked);
        self.agendar_gerar_email = QTreeWidgetItem(self.agenda_gerar)

        #self.agenda_gerar_email_textopleno = QTreeWidgetItem(self.agendar_gerar_email)



        self.agenda_gerar_dadobruto = QTreeWidgetItem(self.agendar_gerar_email)
        self.agenda_gerar_dadobruto.setCheckState(0, Qt.Unchecked);
        self.config_agenda.setObjectName(u"config_agenda")
        self.config_agenda.setGeometry(QRect(385, 50, 291, 351))
        self.config_agenda.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.config_agenda.setFrameShape(QFrame.NoFrame)
        self.config_agenda.setFrameShadow(QFrame.Plain)
        self.config_agenda.setHeaderHidden(False)
        self.config_agenda.header().setCascadingSectionResizes(False)
        self.pushButton_2 = QPushButton(self.tab_18)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(592, 7, 75, 23))
        self.pushButton_2.setStyleSheet(u"background-color: None;")
        self.tabWidget_3.addTab(self.tab_18, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.listWidget = QListWidget(self.tab_19)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(4, 34, 671, 391))
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setViewMode(QListView.ListMode)
        self.pushButton = QPushButton(self.tab_19)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(592, 7, 75, 23))
        self.pushButton.setStyleSheet(u"background-color: None;")

        # aba historico

        #self.tabWidget_3.addTab(self.tab_19, "")
        self.frame_decodificar = QFrame(self.centralwidget)
        self.frame_decodificar.setObjectName(u"frame_decodificar")
        self.frame_decodificar.setGeometry(QRect(169, 31, 731, 551))
        self.frame_decodificar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_decodificar.setFrameShape(QFrame.StyledPanel)
        self.frame_decodificar.setFrameShadow(QFrame.Raised)
        self.label_analises_2 = QLabel(self.frame_decodificar)
        self.label_analises_2.setObjectName(u"label_analises_2")
        self.label_analises_2.setGeometry(QRect(20, 7, 191, 33))
        self.label_analises_2.setFont(font4)
        self.label_analises_2.setStyleSheet(u"color: rgb(51, 51, 51);")
        self.line_9 = QFrame(self.frame_decodificar)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(-1, 49, 802, 2))
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.groupBox = QGroupBox(self.frame_decodificar)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 68, 681, 451))
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(130, 40, 391, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_local_arquivo = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_local_arquivo.setObjectName(u"lineEdit_local_arquivo")

        self.gridLayout.addWidget(self.lineEdit_local_arquivo, 1, 1, 1, 1)

        self.lineEdit_chave = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_chave.setObjectName(u"lineEdit_chave")

        self.gridLayout.addWidget(self.lineEdit_chave, 0, 1, 1, 1)

        self.toolButton_selecionar_arq = QToolButton(self.gridLayoutWidget)
        self.toolButton_selecionar_arq.setObjectName(u"toolButton_selecionar_arq")
        self.toolButton_selecionar_arq.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.toolButton_selecionar_arq, 1, 2, 1, 1)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(270, 160, 101, 41))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.push_decodificar = QPushButton(self.verticalLayoutWidget_2)
        self.push_decodificar.setObjectName(u"push_decodificar")
        self.push_decodificar.setStyleSheet(u"background-color: None;")

        self.verticalLayout_2.addWidget(self.push_decodificar)

        self.frame_ajuda = QFrame(self.centralwidget)
        self.frame_ajuda.setObjectName(u"frame_ajuda")
        self.frame_ajuda.setGeometry(QRect(169, 31, 731, 551))
        self.frame_ajuda.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_ajuda.setFrameShape(QFrame.StyledPanel)
        self.frame_ajuda.setFrameShadow(QFrame.Raised)
        self.label_analises_4 = QLabel(self.frame_ajuda)
        self.label_analises_4.setObjectName(u"label_analises_4")
        self.label_analises_4.setGeometry(QRect(20, 3, 191, 41))
        self.label_analises_4.setFont(font4)
        self.label_analises_4.setStyleSheet(u"color: rgb(51, 51, 51);")
        self.line_11 = QFrame(self.frame_ajuda)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(-1, 49, 802, 2))
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_ajuda)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(20, 68, 681, 451))
        self.plainTextEdit_2.setReadOnly(True)
        self.frame_bemvindo = QFrame(self.centralwidget)
        self.frame_bemvindo.setObjectName(u"frame_bemvindo")
        self.frame_bemvindo.setGeometry(QRect(169, 31, 731, 551))
        self.frame_bemvindo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_bemvindo.setFrameShape(QFrame.StyledPanel)
        self.frame_bemvindo.setFrameShadow(QFrame.Raised)
        self.groupBox_5 = QGroupBox(self.frame_bemvindo)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 18, 681, 501))
        self.label_analises_6 = QLabel(self.groupBox_5)
        self.label_analises_6.setObjectName(u"label_analises_6")
        self.label_analises_6.setGeometry(QRect(10, 170, 530, 21))
        self.label_analises_6.setFont(font4)
        self.label_analises_6.setStyleSheet(u"color: rgb(51, 51, 51);")
        self.label_analises_7 = QLabel(self.groupBox_5)
        self.label_analises_7.setObjectName(u"label_analises_7")
        self.label_analises_7.setGeometry(QRect(525, 460, 151, 21))
        font10 = QFont()
        font10.setFamily(u"Source Sans Pro")
        font10.setPointSize(20)
        font10.setBold(True)
        font10.setWeight(75)
        font10.setStyleStrategy(QFont.PreferDefault)
        self.label_analises_7.setFont(font10)
        self.label_analises_7.setStyleSheet(u"color: rgb(51, 51, 51);")
        self.plainTextEdit_3 = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        #welcome1
        self.plainTextEdit_3.setGeometry(QRect(10, 210, 661, 200))

        font11 = QFont()
        font11.setFamily(u"MS Shell Dlg 2")
        font11.setPointSize(10)
        self.plainTextEdit_3.setFont(font11)

        self.plainTextEdit_3.setStyleSheet(u"color: rgb(43, 43, 43);")
        self.plainTextEdit_3.setFrameShape(QFrame.NoFrame)
        self.commandLinkButton_2 = QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        #oblivion logo
        self.commandLinkButton_2.setGeometry(QRect(269, 50, 200, 200))
        self.commandLinkButton_2.setStyleSheet(u"\n"
"background-color: None;\n"
"border-style: outset;\n"
"border-radius:1px;\n"
"padding: 6px;\n"
"min-width:10px;")
        icon14 = QIcon()
        icon14.addFile(u":/menu/media/mini.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_2.setIcon(icon14)
        self.commandLinkButton_2.setIconSize(QSize(100, 120))
        MainWindow.setCentralWidget(self.centralwidget)
        self.widget_faixa.raise_()
        self.frame_modulos.raise_()
        self.frame_menu.raise_()
        self.frame_decodificar.raise_()
        self.frame_analisar.raise_()
        self.frame_analises.raise_()
        self.frame_agendar.raise_()
        self.frame_ajuda.raise_()
        self.frame_bemvindo.raise_()

        self.retranslateUi(MainWindow)
        self.menu_analisar.clicked.connect(self.frame_analisar.raise_)
        self.menu_analises.clicked.connect(self.frame_analises.raise_)
        self.menu_modulos.clicked.connect(self.frame_modulos.raise_)
        self.menu_agendar.clicked.connect(self.frame_agendar.raise_)
        self.menu_decodificar.clicked.connect(self.frame_decodificar.raise_)
        self.menu_ajuda.clicked.connect(self.frame_ajuda.raise_)

        self.tabwidget_analise_config.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_modulos.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Oblivion", None))
        self.menu_analisar.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.menu_modulos.setText(QCoreApplication.translate("MainWindow", u"Modules", None))
        self.menu_analises.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_analise_2.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
        self.label_outros.setText(QCoreApplication.translate("MainWindow", u"OTHERS", None))
        self.menu_agendar.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.menu_decodificar.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.menu_ajuda.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_analise.setText(QCoreApplication.translate("MainWindow", u"Scan", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Delay scan(s)", None))
        self.db_looping.setText(QCoreApplication.translate("MainWindow", u"Loop scan", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Completion", None))
        self.db_fechar.setText(QCoreApplication.translate("MainWindow", u"Close after conclude", None))
        self.db_desligar.setText(QCoreApplication.translate("MainWindow", u"Turn off after conclude", None))
        self.tabwidget_analise_config.setTabText(self.tabwidget_analise_config.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Configurations", None))
        ___qtreewidgetitem = self.config_modulos.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Modules", None));

        __sortingEnabled = self.config_modulos.isSortingEnabled()
        self.config_modulos.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.config_modulos.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Data Leak", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Common websites", None));
        #___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        #___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Lista Personalizada", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Google dorks", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Word lists", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"APIs", None));
        #___qtreewidgetitem7 = self.config_modulos.topLevelItem(1)
        #___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Natural Language", None));
        ___qtreewidgetitem8 = self.config_modulos.topLevelItem(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Vulnerabilities Scan", None));
        self.config_modulos.setSortingEnabled(__sortingEnabled)

        self.tabwidget_analise_config.setTabText(self.tabwidget_analise_config.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Modules", None))
        ___qtreewidgetitem9 = self.config_formatos.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Results", None));

        __sortingEnabled1 = self.config_formatos.isSortingEnabled()
        self.config_formatos.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.config_formatos.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"Generate results", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"Local file", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Raw data (.txt)", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem11.child(1)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u".txt", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem13.child(1)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem11.child(2)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u".docx", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem16.child(1)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem11.child(3)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u".pdf", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem19.child(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem19.child(1)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem11.child(4)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u".xlsx", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem22.child(1)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem11.child(5)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u".json", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem25.child(0)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem25.child(1)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem11.child(6)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u".html", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem28.child(0)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem28.child(1)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem11.child(7)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u".xml", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem31.child(0)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem31.child(1)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem11.child(8)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u".db", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem34.child(0)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem36 = ___qtreewidgetitem34.child(1)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem10.child(1)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MainWindow", u"Google Drive", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem37.child(0)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MainWindow", u"Send files to Cloud", None));

        self.config_formatos.setSortingEnabled(__sortingEnabled1)

        self.tabwidget_analise_config.setTabText(self.tabwidget_analise_config.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Format", None))
        self.analise_salvar.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.analise_nova_analise.setText(QCoreApplication.translate("MainWindow", u"New scan", None))
        self.menu_configuracoes.setText("")
        self.commandLinkButton.setText("")
        self.label_analises.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_modulos.setText(QCoreApplication.translate("MainWindow", u"Modules", None))
        self.toolButton_4.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Data Leak", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"     Check for new \n"
"         data leaks", None))
        self.toolButton_13.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Vulnerabilities", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"  Check for new\n"
"         CVEs", None))
        self.tabWidget_modulos.setTabText(self.tabWidget_modulos.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"All", None))
        self.label_analises_3.setText(QCoreApplication.translate("MainWindow", u"Schedule scan", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time: ", None))
        hash_g = random.getrandbits(23)
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", f"", None))
        ___qtreewidgetitem63 = self.config_agenda.headerItem()
        ___qtreewidgetitem63.setText(0, QCoreApplication.translate("MainWindow", u"Results", None));

        __sortingEnabled2 = self.config_agenda.isSortingEnabled()
        self.config_agenda.setSortingEnabled(False)
        ___qtreewidgetitem64 = self.config_agenda.topLevelItem(0)
        ___qtreewidgetitem64.setText(0, QCoreApplication.translate("MainWindow", u"Modules", None));
        ___qtreewidgetitem65 = ___qtreewidgetitem64.child(0)
        ___qtreewidgetitem65.setText(0, QCoreApplication.translate("MainWindow", u"Vulnerabilities Scan", None));
        #___qtreewidgetitem66 = ___qtreewidgetitem64.child(1)
        #___qtreewidgetitem66.setText(0, QCoreApplication.translate("MainWindow", u"Natural Language", None));
        ___qtreewidgetitem67 = ___qtreewidgetitem64.child(1)
        ___qtreewidgetitem67.setText(0, QCoreApplication.translate("MainWindow", u"Data Leak", None));
        #___qtreewidgetitem68 = ___qtreewidgetitem67.child(0)
        #___qtreewidgetitem68.setText(0, QCoreApplication.translate("MainWindow", u"Sites personalizados", None));
        ___qtreewidgetitem69 = ___qtreewidgetitem67.child(0)
        ___qtreewidgetitem69.setText(0, QCoreApplication.translate("MainWindow", u"Common websites", None));
        ___qtreewidgetitem70 = ___qtreewidgetitem67.child(1)
        ___qtreewidgetitem70.setText(0, QCoreApplication.translate("MainWindow", u"Google dorks", None));
        ___qtreewidgetitem71 = ___qtreewidgetitem67.child(2)
        ___qtreewidgetitem71.setText(0, QCoreApplication.translate("MainWindow", u"Word lists", None));
        ___qtreewidgetitem72 = ___qtreewidgetitem67.child(3)
        ___qtreewidgetitem72.setText(0, QCoreApplication.translate("MainWindow", u"APIs", None));
        ___qtreewidgetitem73 = self.config_agenda.topLevelItem(1)
        ___qtreewidgetitem73.setText(0, QCoreApplication.translate("MainWindow", u"Generate results", None));
        ___qtreewidgetitem74 = ___qtreewidgetitem73.child(0)
        ___qtreewidgetitem74.setText(0, QCoreApplication.translate("MainWindow", u"Local file", None));
        ___qtreewidgetitem75 = ___qtreewidgetitem74.child(0)
        ___qtreewidgetitem75.setText(0, QCoreApplication.translate("MainWindow", u"Raw data (.txt)", None));
        ___qtreewidgetitem76 = ___qtreewidgetitem74.child(1)
        ___qtreewidgetitem76.setText(0, QCoreApplication.translate("MainWindow", u".txt", None));
        ___qtreewidgetitem77 = ___qtreewidgetitem76.child(0)
        ___qtreewidgetitem77.setText(0, QCoreApplication.translate("MainWindow", u"Occult passwords", None));
        ___qtreewidgetitem78 = ___qtreewidgetitem76.child(1)
        ___qtreewidgetitem78.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem79 = ___qtreewidgetitem74.child(2)
        ___qtreewidgetitem79.setText(0, QCoreApplication.translate("MainWindow", u".docx", None));
        ___qtreewidgetitem80 = ___qtreewidgetitem79.child(0)
        ___qtreewidgetitem80.setText(0, QCoreApplication.translate("MainWindow", u"Ocult passwords", None));
        ___qtreewidgetitem81 = ___qtreewidgetitem79.child(1)
        ___qtreewidgetitem81.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem82 = ___qtreewidgetitem74.child(3)
        ___qtreewidgetitem82.setText(0, QCoreApplication.translate("MainWindow", u".pdf", None));
        ___qtreewidgetitem83 = ___qtreewidgetitem82.child(0)
        ___qtreewidgetitem83.setText(0, QCoreApplication.translate("MainWindow", u"Ocult passwords", None));
        ___qtreewidgetitem84 = ___qtreewidgetitem82.child(1)
        ___qtreewidgetitem84.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem85 = ___qtreewidgetitem74.child(4)
        ___qtreewidgetitem85.setText(0, QCoreApplication.translate("MainWindow", u".xlsx", None));
        ___qtreewidgetitem86 = ___qtreewidgetitem85.child(0)
        ___qtreewidgetitem86.setText(0, QCoreApplication.translate("MainWindow", u"Ocult passwords", None));
        ___qtreewidgetitem87 = ___qtreewidgetitem85.child(1)
        ___qtreewidgetitem87.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem88 = ___qtreewidgetitem74.child(5)
        ___qtreewidgetitem88.setText(0, QCoreApplication.translate("MainWindow", u".json", None));
        ___qtreewidgetitem89 = ___qtreewidgetitem88.child(0)
        ___qtreewidgetitem89.setText(0, QCoreApplication.translate("MainWindow", u"Ocult passwords", None));
        ___qtreewidgetitem90 = ___qtreewidgetitem88.child(1)
        ___qtreewidgetitem90.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem91 = ___qtreewidgetitem74.child(6)
        ___qtreewidgetitem91.setText(0, QCoreApplication.translate("MainWindow", u".html", None));
        ___qtreewidgetitem92 = ___qtreewidgetitem91.child(0)
        ___qtreewidgetitem92.setText(0, QCoreApplication.translate("MainWindow", u"Ocult passwords", None));
        ___qtreewidgetitem93 = ___qtreewidgetitem91.child(1)
        ___qtreewidgetitem93.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem94 = ___qtreewidgetitem74.child(7)
        ___qtreewidgetitem94.setText(0, QCoreApplication.translate("MainWindow", u".xml", None));
        ___qtreewidgetitem95 = ___qtreewidgetitem94.child(0)
        ___qtreewidgetitem95.setText(0, QCoreApplication.translate("MainWindow", u"Ocult passwords", None));
        ___qtreewidgetitem96 = ___qtreewidgetitem94.child(1)
        ___qtreewidgetitem96.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem97 = ___qtreewidgetitem74.child(8)
        ___qtreewidgetitem97.setText(0, QCoreApplication.translate("MainWindow", u".db", None));
        ___qtreewidgetitem98 = ___qtreewidgetitem97.child(0)
        ___qtreewidgetitem98.setText(0, QCoreApplication.translate("MainWindow", u"Ocult passwords", None));
        ___qtreewidgetitem99 = ___qtreewidgetitem97.child(1)
        ___qtreewidgetitem99.setText(0, QCoreApplication.translate("MainWindow", u"Encrypt", None));
        ___qtreewidgetitem100 = ___qtreewidgetitem73.child(1)
        ___qtreewidgetitem100.setText(0, QCoreApplication.translate("MainWindow", u"Google Drive", None));

        ___qtreewidgetitem101 = ___qtreewidgetitem100.child(0)
        ___qtreewidgetitem102 = ___qtreewidgetitem101.child(0)
        ___qtreewidgetitem103 = ___qtreewidgetitem100.child(0)

        ___qtreewidgetitem103.setText(0, QCoreApplication.translate("MainWindow", u"Send files to Cloud", None));
        self.config_agenda.setSortingEnabled(__sortingEnabled2)

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_analises_2.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.groupBox.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"File path", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Key (optional)", None))
        self.toolButton_selecionar_arq.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.push_decodificar.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.label_analises_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"For more detailed information read the Oblivion's documentation or access us GitHub repo.", None))
        self.groupBox_5.setTitle("")
        self.label_analises_6.setText(QCoreApplication.translate("MainWindow", u"                 Welcome to Oblivion   ", None))
        self.label_analises_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">Oblivion 1.0.0</span></p></body></html>", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"                                                        Thanks for trying Oblivion.\n\n                               We would love your feedback and contributions to continue\n              make it better. Please raise issues and pull-requests directly on our GitHub repo.", None))
        self.commandLinkButton_2.setText("")
    # retranslateUi

