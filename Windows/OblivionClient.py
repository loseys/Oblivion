# -*- coding: utf-8 -*- --noconsole

import sys
import threading
import ctypes
import time
import random
import pathlib
import base64
import glob
import logging

import coloredlogs
import verboselogs
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtCore import (QMetaObject, QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtWidgets import *
from interface import Ui_MainWindow
from os import environ
from sqlalchemy import create_engine
from etc.email.send_email import *
from etc.api.scylla import *
from etc.api.intelxapi import *
from etc.api.intelligencex import *
from etc.api.hibpwned import *
from etc.scrap.wordlists_search import *
from etc.scrap.pastebin import *
from etc.scrap.google_dorks import *
from etc.api.cves import *
from etc.create import *
from etc.notification.telegram import *
from etc.decript import decript_file
from etc.api.keys import *


# Global variables/Variáveis globais.
db_file = 'data.db'
path_central = str(pathlib.Path(__file__).parent.absolute())


def suppress_qt_warnings():
    """
    Suppresses some warnings of graphics/Suprimir alguns avisos da parte gráfica.
    Suppresses some warnings of graphics/Suprimir alguns avisos da parte gráfica.
    """
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


def logando_main(tipo, mensagem):
    """
    :param tipo: Sets the log type/Seta o tipo de log.
    :param mensagem: Sets the message of log/Seta a mensagem do log.
    :return: Returns the complete log's body/Retorn o corpo completo do log.
    """
    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG')
    coloredlogs.install(level='DEBUG', logger=logger)
    logging.basicConfig(format='%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s')
    logger = verboselogs.VerboseLogger('')

    if tipo == 'verbose':
        logger.verbose(mensagem)

    elif tipo == 'debug':
        logger.debug(mensagem)

    elif tipo == 'info':
        logger.info(mensagem)

    elif tipo == 'warning':
        logger.warning(mensagem)

    elif tipo == 'error':
        logger.error(mensagem)

    elif tipo == 'critical':
        logger.critical(mensagem)

    else:
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Gets the Oblivion's GUI/Pega a parte gráfica do Oblivion.
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        print("Oblivion [version 1.0.0]", "Copyright (c) 2020, Loseys - BSD License.\n", sep='\n'); logando_main('info','Starting the Oblivion')
        self.setupUi(self)
        self.analise_nova_analise.clicked.connect(self.segundo_plano)
        self.toolButton_4.clicked.connect(self.window2)
        self.setWindowIcon(QtGui.QIcon('icone.png'))
        myappid = 'ImproveSecurity.Oblivion.Scan.Beta'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.config_modulos.expandToDepth(1)
        self.config_formatos.expandToDepth(1)
        self.menu_configuracoes.clicked.connect(self.configuracao_oblivion)
        self.analise_salvar.clicked.connect(self.loop_set)
        self.cancelar_analise = False
        self.arquivo_decript = None
        self.analise_salvar.setDisabled(True)
        self.push_decodificar.clicked.connect(self.decript_f)
        self.toolButton_selecionar_arq.clicked.connect(self.abrir_f)
        self.pushButton_2.clicked.connect(self.agendar_tarefa)
        now = datetime.datetime.now()
        self.dateEdit.setDate(QDate(now.year, now.month, now.day))
        self.timeEdit.setTime(QTime(now.hour, now.minute))
        self.menu_analises.clicked.connect(self.historico_listar)
        #self.modulos_modulos_naturallanguage.setDisabled(1)
        self.setWindowIcon(QtGui.QIcon(f'{path_central}/media/oblivion-256.png'))


    def historico_listar(self):
        """
        Lists all the scans listed on Oblivion's historic/Lista todos os scans do histórico.
        """
        try:
            self.listWidget_2.clear()
            with open(f'{path_central}/etc/logs/activity.txt', 'r') as historico:
                analises = historico.read()
                analises = analises.split('\n')
                for e in analises:

                    if e != '' and e != ' ':
                        self.listWidget_2.addItem(e)

        except:
            logando_main('error', 'Was not possible to load the historic')


    def agendar_tarefa(self):
        """
        Creates the scheduled scan/Cria análise agendada.
        """
        hash_f = random.getrandbits(28)
        data_agenda = self.dateEdit.text()
        data_agenda = data_agenda.replace('/','-')
        hora_agenda = self.timeEdit.text()
        hora_agenda = hora_agenda.replace(':','_')
        path_oblivion = os.path.dirname(__file__)
        path_scripts = str(path_oblivion) + '/'
        path_schedule = path_scripts + f'etc/schedule/scripts/{self.plainTextEdit.toPlainText()}_{data_agenda}-{hora_agenda}.txt'
        path_start = path_oblivion + '/schedule.py'
        print(path_start)

        with open(f'etc/schedule/scripts/{self.plainTextEdit.toPlainText()}_{data_agenda}-{hora_agenda}.txt', 'w+') as criar_config:
            criar_config.write(
f"""agenda_modulos_vulscan={self.agenda_modulos_vulscan.checkState(0)}
agenda_modulos_commonwebsites={self.agenda_modulos_commonwebsites.checkState(0)}
agenda_modulos_googledorks={self.agenda_modulos_googledorks.checkState(0)}
agenda_modulos_wordlists={self.agenda_modulos_wordlists.checkState(0)}
agenda_modulos_leak_api={self.agenda_modulos_leak_api.checkState(0)}
agenda_gerar_copia_dadobruto={self.agenda_gerar_copia_dadobruto.checkState(0)}
agenda_gerar_copia_txt={self.agenda_gerar_copia_txt.checkState(0)}
agenda_gerar_copia_txt_ocult={self.agenda_gerar_copia_txt_ocult.checkState(0)}
agenda_gerar_copia_txt_cript={self.agenda_gerar_copia_txt_cript.checkState(0)}
agenda_gerar_copia_docx={self.agenda_gerar_copia_docx.checkState(0)}
agenda_gerar_copia_docx_ocult={self.agenda_gerar_copia_docx_ocult.checkState(0)}
agenda_gerar_copia_docx_cript={self.agenda_gerar_copia_docx_cript.checkState(0)}
agenda_gerar_copia_pdf={self.agenda_gerar_copia_pdf.checkState(0)}
agenda_gerar_copia_pdf_ocult={self.agenda_gerar_copia_pdf_ocult.checkState(0)}
agenda_gerar_copia_pdf_cript={self.agenda_gerar_copia_pdf_cript.checkState(0)}
agenda_gerar_copia_xlsx={self.agenda_gerar_copia_xlsx.checkState(0)}
agenda_gerar_copia_xlsx_ocult={self.agenda_gerar_copia_xlsx_ocult.checkState(0)}
agenda_gerar_copia_xlsx_cript={self.agenda_gerar_copia_xlsx_cript.checkState(0)}
agenda_gerar_copia_json={self.agenda_gerar_copia_json.checkState(0)}
agenda_gerar_copia_json_ocult={self.agenda_gerar_copia_json_ocult.checkState(0)}
agenda_gerar_copia_json_cript={self.agenda_gerar_copia_json_cript.checkState(0)}
agenda_gerar_copia_html={self.agenda_gerar_copia_html.checkState(0)}
agenda_gerar_copia_html_ocult={self.agenda_gerar_copia_html_ocult.checkState(0)}
agenda_gerar_copia_html_cript={self.agenda_gerar_copia_html_cript.checkState(0)}
agenda_gerar_copia_xsl={self.agenda_gerar_copia_xsl.checkState(0)}
agenda_gerar_copia_xsl_ocult={self.agenda_gerar_copia_xsl_ocult.checkState(0)}
agenda_gerar_copia_xsl_cript={self.agenda_gerar_copia_xsl_cript.checkState(0)}
agenda_gerar_copia_db={self.agenda_gerar_copia_db.checkState(0)}
agenda_gerar_copia_db_ocult={self.agenda_gerar_copia_db_ocult.checkState(0)}
agenda_gerar_copia_db_cript={self.agenda_gerar_copia_db_cript.checkState(0)}
agenda_gerar_dadobruto={self.agenda_gerar_dadobruto.checkState(0)}""")

        try:
            executar = (f'SCHTASKS /create /tn "Oblivion {hash_f} - {self.plainTextEdit.toPlainText()}" /tr "{path_start} {path_schedule}" /sc ONCE /sd {self.dateEdit.text()} /st {self.timeEdit.text()}')
            os.system(executar)

        except:
            logando_main('error', 'Was not possible to create the schedule')

    def abrir_f(self):
        """
        Selects the file path to decrypt/Seleciona o path do arquivo para descriptografar.
        """
        self.arquivo_decript = str(QtWidgets.QFileDialog.getOpenFileName()[0])
        self.lineEdit_local_arquivo.setText(self.arquivo_decript)

    def decript_f(self):
        """
        Fixs bar spaces in the path file of decrypt function/Arruma alguns espaços do path do arquivo que será
        descriptografado.
        """
        resolver_key = self.lineEdit_chave.text().replace(' ','')

        if resolver_key:
            decript_file(arquivo=self.lineEdit_local_arquivo.text(), chave=resolver_key)

        else:

            try:
                decript_file(arquivo=self.lineEdit_local_arquivo.text())

            except:
                pass

    def loop_set(self):
        """
        Function of the stop button, if pressed will stop the scan/Função do botão de cancelar, caso seja pressionado
        a análise será cancelada.

        Note: this function have a delay to complete/Essa função apresenta um delay para ser concluida.
        """
        self.cancelar_analise = True

    def window2(self):
        """
        Shows the window of input the passwords, e-mails and documents/Mostra a janela onde coloca-se as senhas, e-mails
        e os documentos.
        """
        self.w = Window2()
        self.w.show()

    def configuracao_oblivion(self):
        """
        Shows the configuration window/Mostra a tela de configuração.
        """
        self.cfo = WindowConfigOblivion()
        self.cfo.show()

    def segundo_plano(self, interval=1):
        """
        Starts the thread process/Inicia o processo de thread.
        """
        self.interval = interval
        self.thread = threading.Thread(target=self.rundaemon, args=())
        self.thread.daemon = True
        self.thread.start()

    def rundaemon(self):
        """
        Calls the scan function/Chama a função de scan.
        """
        self.nova_analise()

    def nova_analise(self):
        """
        Scan function/Função da análise.
        """
        with open(f'{path_central}/etc/logs/activity.txt', 'a') as historico:
            historico.write(f'\n{datetime.datetime.now()}')
        self.analise_nova_analise.setDisabled(True)
        self.analise_salvar.setDisabled(False)
        situacaoIntelx = None
        situacaoDehashed = None
        situacaoHaveIPwned = None
        situacaoScylla = None
        situacaoEmailrep = None
        situacao_loop = self.db_looping.isChecked()

        while True:
            timer_analise_f = (self.db_delay.text())
            timer_analise_f = str(timer_analise_f)
            timer_analise_f = timer_analise_f.replace(',','.')
            timer_analise = float(timer_analise_f)
            time.sleep(timer_analise)
            exportar_dados = []
            exportar_dados_wl =[]
            exportar_dados_pbdb = []
            exportar_dados_dorks = []
            exportar_dados_nltk = []
            exportar_dados_cves = []

            with open('etc/config', 'r') as file:
                abrir_arquivo_config = file.read()
                abrir_arquivo_config = abrir_arquivo_config.split('\n')

            for i in abrir_arquivo_config:

                if 'intelx' in i:
                    i = i.replace('intelx:', '')

                    if i == 'yes':
                        situacaoIntelx = True

                    else:
                        situacaoIntelx = False

                if 'dehashed' in i:
                    i = i.replace('dehashed:', '')

                    if i == 'yes':
                        situacaoDehashed = True
                    else:
                        situacaoDehashed = False

                if 'haveipwned' in i:
                    i = i.replace('haveipwned:', '')

                    if i == 'yes':
                        situacaoHaveIPwned = True

                    else:
                        situacaoHaveIPwned = False

                if 'scylla' in i:
                    i = i.replace('scylla:', '')

                    if i == 'yes':
                        situacaoScylla = True

                    else:
                        situacaoScylla = False

                if 'emailrep' in i:
                    i = i.replace('emailrep:', '')

                    if i == 'yes':
                        situacaoEmailrep = True

                    else:
                        situacaoEmailrep = False

            if self.modulos_modulos_dataleak_common.checkState(0):
                logando_main('info', 'Verifying the common websites')
                exportar_dados_pbdb = []
                dados_separados = self.pegar_dados_arquivo()

                for i in dados_separados:

                    if '00SHSTRx00' in i:
                        i = i.replace(':00SHSTRx00', '')
                        i = str(i)

                        if self.formatos_copia_dadobruto.checkState(0):
                            puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_pbdb.append(puxar_pbdb)

                        else:
                            puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_pbdb.append(puxar_pbdb)

                    if '00EMSTRx00' in i:
                        i = i.replace(':00EMSTRx00', '')
                        i = str(i)

                        if self.formatos_copia_dadobruto.checkState(0):
                            puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_pbdb.append(puxar_pbdb)

                        else:
                            puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_pbdb.append(puxar_pbdb)

                    if '00DMSTRx00' in i:
                        i = i.replace(':00DMSTRx00', '')
                        i = str(i)

                        if self.formatos_copia_dadobruto.checkState(0):
                            puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_pbdb.append(puxar_pbdb)

                        else:
                            puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_pbdb.append(puxar_pbdb)

            #if self.modulos_modulos_dataleak_personalizada.checkState(0):
            #    pass

            if self.modulos_modulos_dataleak_googledorks.checkState(0):
                exportar_dados_dorks = []
                logando_main('info', 'Sweeping the google dorks')
                dados_separados = self.pegar_dados_arquivo()
                for i in dados_separados:

                    if '00SHSTRx00' in i:
                        i = i.replace(':00SHSTRx00', '')

                        if self.formatos_copia_dadobruto.checkState(0):
                            dados_dorks_separados = google_scrap(termo=i, dadobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_dorks.append(dados_dorks_separados)

                        else:
                            dados_dorks_separados = google_scrap(termo=i, dadobruto=False, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_dorks.append(dados_dorks_separados)

                    elif '00EMSTRx00' in i:
                        i = i.replace(':00EMSTRx00', '')

                        if self.formatos_copia_dadobruto.checkState(0):
                            dados_dorks_separados = google_scrap(termo=i, dadobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_dorks.append(dados_dorks_separados)

                        else:
                            dados_dorks_separados = google_scrap(termo=i, dadobruto=False, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_dorks.append(dados_dorks_separados)

                    if '00DMSTRx00' in i:
                        i = i.replace(':00DMSTRx00', '')

                        if self.formatos_copia_dadobruto.checkState(0):
                            dados_dorks_separados = google_scrap(termo=i, dadobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_dorks.append(dados_dorks_separados)

                        else:
                            dados_dorks_separados = google_scrap(termo=i, dadobruto=False, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            exportar_dados_dorks.append(dados_dorks_separados)

            if self.modulos_modulos_dataleak_wordlist.checkState(0):
                exportar_dados_wl = []
                logando_main('info', 'Checking the word lists')
                dados_separados = self.pegar_dados_arquivo()
                for i in dados_separados:

                    if '00SHSTRx00' in i:
                        i = i.replace(':00SHSTRx00','')
                        dados_wl_separados = verificar_dados(i)
                        exportar_dados_wl += dados_wl_separados

            if self.modulos_modulos_dataleak_api.checkState(0):
                logando_main('info', 'Initializing the APIs requisitation')
                dados_separados = self.pegar_dados_arquivo()
                for i in dados_separados:

                    if '00EMSTRx00' in i:
                        i = i.replace(':00EMSTRx00','')

                        # Have I Been Pwned/email
                        if situacaoHaveIPwned == True:
                            listaf_haveipwned = check_breach(i)
                            for ex3 in listaf_haveipwned:

                                if i in ex3:
                                    exportar_dados.append(ex3)

                        # Scylla/email
                        if situacaoScylla == True:
                            temp_scyla = []

                            if self.formatos_copia_dadobruto.checkState(0):
                                listaf_scylla = chamar_limpar_scylla(email=i, dadobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                                for ex1 in listaf_scylla:

                                    if i in ex1:
                                        exportar_dados.append(ex1)
                                        temp_scyla.append(ex1)
                                for item_lista in temp_scyla:
                                    list_temporaria = item_lista.split(':')
                                    dominio_vazado = list_temporaria[2]
                                    scylla_dado_bruto(dominio_vazado,gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            else:
                                listaf_scylla = chamar_limpar_scylla(email=i)
                                for ex1 in listaf_scylla:

                                    if i in ex1:
                                        exportar_dados.append(ex1)

                        # Intelligencex/email
                        if situacaoIntelx == True:
                            if self.formatos_copia_dadobruto.checkState(0):
                                listaf_inteligencex = intelligencex_sid_raw(i, conteudobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                                for ex2 in listaf_inteligencex:

                                    if i in ex2:
                                        exportar_dados.append(ex2)
                            else:
                                listaf_inteligencex = intelligencex_sid_raw(i)
                                for ex2 in listaf_inteligencex:

                                    if i in ex2:
                                        exportar_dados.append(ex2)

                    elif '00SHSTRx00' in i:
                        i = i.replace(':00SHSTRx00', '')

                        # Have I Been Pwned/senha
                        if situacaoHaveIPwned == True:
                            listaf_haveipwned = check_breach(i)
                            for ex3 in listaf_haveipwned:

                                if i in ex3:
                                    exportar_dados.append(ex3)

                        # Scylla/senha
                        if situacaoScylla == True:
                            temp_scyla = []

                            if self.formatos_copia_dadobruto.checkState(0):
                                listaf_scylla = chamar_limpar_scylla(senha=i, dadobruto=True, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                                for ex1 in listaf_scylla:

                                    if i in ex1:
                                        exportar_dados.append(ex1)
                                        temp_scyla.append(ex1)
                                for item_lista in temp_scyla:
                                    list_temporaria = item_lista.split(':')
                                    dominio_vazado = list_temporaria[2]
                                    scylla_dado_bruto(dominio_vazado, gdr=str(self.formatos_gerar_email_dadobruto.checkState(0)))
                            else:
                                listaf_scylla = chamar_limpar_scylla(senha=i)
                                for ex1 in listaf_scylla:

                                    if i in ex1:
                                        exportar_dados.append(ex1)

                    elif '00DMSTRx00' in i:
                        i = i.replace(':00DMSTRx00', '')

                        # Intelligencex/email
                        if situacaoIntelx == True:

                            if self.formatos_copia_dadobruto.checkState(0):
                                listaf_inteligencex = intelligencex_sid_raw(i, conteudobruto=True, gdr=str(
                                    self.formatos_gerar_email_dadobruto.checkState(0)))
                                for ex2 in listaf_inteligencex:

                                    if i in ex2:
                                        exportar_dados.append(ex2)
                            else:
                                listaf_inteligencex = intelligencex_sid_raw(i)
                                for ex2 in listaf_inteligencex:

                                    if i in ex2:
                                        exportar_dados.append(ex2)

            if self.modulos_modulos_vulscan.checkState(0):
                logando_main('info', 'Scanning the last CVEs')
                exportar_dados_cves = []
                export_cve_t = iniciar_analise_total_cves()
                exportar_dados_cves += export_cve_t

                data_atual = datetime.date.today()
                definir = os.environ

                for valor, item in definir.items():

                    if valor == 'APPDATA':
                        lista_item = item.split('\\')
                        usuario = lista_item[2]
                documentos_f = f'C:/Users/{usuario}/Documents'

                if exportar_dados_cves != [] or exportar_dados_cves != None or exportar_dados_cves != ' ':
                    with open(f'{documentos_f}/CVEs_results.txt', 'w') as resultado_cves:
                        for e in exportar_dados_cves:
                            resultado_cves.write(e)

            # Debug: results of scan/resultados das análises
            #print(f'API --> {exportar_dados}')
            #print(f'WORDLIST --> {exportar_dados_wl}')
            #print(f'CW Pastebin --> {exportar_dados_pbdb}')
            #print(f'Dorks --> {exportar_dados_dorks}')
            #print(f'NLTK --> {exportar_dados_nltk}')
            #print(f'CVEs --> {exportar_dados_cves}')

            if exportar_dados == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == [
                'None'] or exportar_dados_dorks == [None]:
                exportar_dados = []

            if exportar_dados_wl == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == [
                'None'] or exportar_dados_dorks == [None]:
                exportar_dados_wl = []

            if exportar_dados_pbdb == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == [
                'None'] or exportar_dados_dorks == [None]:
                exportar_dados_pbdb = []

            if exportar_dados_dorks == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == [
                'None'] or exportar_dados_dorks == [None]:
                exportar_dados_dorks = []

            if exportar_dados_cves == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == [
                'None'] or exportar_dados_dorks == [None]:
                exportar_dados_cves = []

            if exportar_dados or exportar_dados_wl or exportar_dados_pbdb or exportar_dados_dorks:

                if exportar_dados:
                    logando_main('info', 'Saving the results')
                    gerar_resultados(nome='API_', conteudo=exportar_dados, gdrive=str(self.formatos_gerar_email_dadobruto.checkState(0)),
                        txt_f=str(self.formatos_copia_txt.checkState(0)), txt_ocult=str(self.formatos_copia_txt_ocult.checkState(0)),txt_cript=str(self.formatos_copia_txt_cript.checkState(0)),
                        docx_f=str(self.formatos_copia_docx.checkState(0)), docx_ocult=str(self.formatos_copia_docx_ocult.checkState(0)), docx_cript=str(self.formatos_copia_docx_cript.checkState(0)),
                        pdf_f=str(self.formatos_copia_pdf.checkState(0)), pdf_ocult=str(self.formatos_copia_pdf_ocult.checkState(0)), pdf_cript=str(self.formatos_copia_pdf_cript.checkState(0)),
                        xlsx_f=str(self.formatos_copia_xlsx.checkState(0)), xlsx_ocult=str(self.formatos_copia_xlsx_ocult.checkState(0)), xlsx_cript=str(self.formatos_copia_xlsx_cript.checkState(0)),
                        json_f=str(self.formatos_copia_json.checkState(0)), json_ocult=str(self.formatos_copia_json_ocult.checkState(0)), json_cript=str(self.formatos_copia_json_cript.checkState(0)),
                        html_f=str(self.formatos_copia_html.checkState(0)), html_ocult=str(self.formatos_copia_html_ocult.checkState(0)), html_cript=str(self.formatos_copia_html_cript.checkState(0)),
                        xsl_f=str(self.formatos_copia_xls.checkState(0)), xsl_ocult=str(self.formatos_copia_xls_ocult.checkState(0)), xsl_cript=str(self.formatos_copia_xls_cript.checkState(0)),
                        db_f=str(self.formatos_copia_db.checkState(0)), db_ocult=str(self.formatos_copia_db_ocult.checkState(0)), db_cript=str(self.formatos_copia_db_cript.checkState(0)))

                if exportar_dados_wl:
                    logando_main('info', 'Saving the results')
                    gerar_resultados(nome='WORDLIST_', conteudo=exportar_dados_wl, gdrive=str(self.formatos_gerar_email_dadobruto.checkState(0)),
                        txt_f=str(self.formatos_copia_txt.checkState(0)), txt_ocult=str(self.formatos_copia_txt_ocult.checkState(0)),txt_cript=str(self.formatos_copia_txt_cript.checkState(0)),
                        docx_f=str(self.formatos_copia_docx.checkState(0)), docx_ocult=str(self.formatos_copia_docx_ocult.checkState(0)), docx_cript=str(self.formatos_copia_docx_cript.checkState(0)),
                        pdf_f=str(self.formatos_copia_pdf.checkState(0)), pdf_ocult=str(self.formatos_copia_pdf_ocult.checkState(0)), pdf_cript=str(self.formatos_copia_pdf_cript.checkState(0)),
                        xlsx_f=str(self.formatos_copia_xlsx.checkState(0)), xlsx_ocult=str(self.formatos_copia_xlsx_ocult.checkState(0)), xlsx_cript=str(self.formatos_copia_xlsx_cript.checkState(0)),
                        json_f=str(self.formatos_copia_json.checkState(0)), json_ocult=str(self.formatos_copia_json_ocult.checkState(0)), json_cript=str(self.formatos_copia_json_cript.checkState(0)),
                        html_f=str(self.formatos_copia_html.checkState(0)), html_ocult=str(self.formatos_copia_html_ocult.checkState(0)), html_cript=str(self.formatos_copia_html_cript.checkState(0)),
                        xsl_f=str(self.formatos_copia_xls.checkState(0)), xsl_ocult=str(self.formatos_copia_xls_ocult.checkState(0)), xsl_cript=str(self.formatos_copia_xls_cript.checkState(0)),
                        db_f=str(self.formatos_copia_db.checkState(0)), db_ocult=str(self.formatos_copia_db_ocult.checkState(0)), db_cript=str(self.formatos_copia_db_cript.checkState(0)))

                if exportar_dados_pbdb:
                    logando_main('info', 'Saving the results')
                    gerar_resultados(nome='COMMONWEBSITES', conteudo=exportar_dados_pbdb, gdrive=str(self.formatos_gerar_email_dadobruto.checkState(0)),
                        txt_f=str(self.formatos_copia_txt.checkState(0)), txt_ocult=str(self.formatos_copia_txt_ocult.checkState(0)),txt_cript=str(self.formatos_copia_txt_cript.checkState(0)),
                        docx_f=str(self.formatos_copia_docx.checkState(0)), docx_ocult=str(self.formatos_copia_docx_ocult.checkState(0)), docx_cript=str(self.formatos_copia_docx_cript.checkState(0)),
                        pdf_f=str(self.formatos_copia_pdf.checkState(0)), pdf_ocult=str(self.formatos_copia_pdf_ocult.checkState(0)), pdf_cript=str(self.formatos_copia_pdf_cript.checkState(0)),
                        xlsx_f=str(self.formatos_copia_xlsx.checkState(0)), xlsx_ocult=str(self.formatos_copia_xlsx_ocult.checkState(0)), xlsx_cript=str(self.formatos_copia_xlsx_cript.checkState(0)),
                        json_f=str(self.formatos_copia_json.checkState(0)), json_ocult=str(self.formatos_copia_json_ocult.checkState(0)), json_cript=str(self.formatos_copia_json_cript.checkState(0)),
                        html_f=str(self.formatos_copia_html.checkState(0)), html_ocult=str(self.formatos_copia_html_ocult.checkState(0)), html_cript=str(self.formatos_copia_html_cript.checkState(0)),
                        xsl_f=str(self.formatos_copia_xls.checkState(0)), xsl_ocult=str(self.formatos_copia_xls_ocult.checkState(0)), xsl_cript=str(self.formatos_copia_xls_cript.checkState(0)),
                        db_f=str(self.formatos_copia_db.checkState(0)), db_ocult=str(self.formatos_copia_db_ocult.checkState(0)), db_cript=str(self.formatos_copia_db_cript.checkState(0)))

                if exportar_dados_dorks:
                    logando_main('info', 'Saving the results')
                    gerar_resultados(nome='DORKS', conteudo=exportar_dados_dorks, gdrive=str(self.formatos_gerar_email_dadobruto.checkState(0)),
                        txt_f=str(self.formatos_copia_txt.checkState(0)), txt_ocult=str(self.formatos_copia_txt_ocult.checkState(0)),txt_cript=str(self.formatos_copia_txt_cript.checkState(0)),
                        docx_f=str(self.formatos_copia_docx.checkState(0)), docx_ocult=str(self.formatos_copia_docx_ocult.checkState(0)), docx_cript=str(self.formatos_copia_docx_cript.checkState(0)),
                        pdf_f=str(self.formatos_copia_pdf.checkState(0)), pdf_ocult=str(self.formatos_copia_pdf_ocult.checkState(0)), pdf_cript=str(self.formatos_copia_pdf_cript.checkState(0)),
                        xlsx_f=str(self.formatos_copia_xlsx.checkState(0)), xlsx_ocult=str(self.formatos_copia_xlsx_ocult.checkState(0)), xlsx_cript=str(self.formatos_copia_xlsx_cript.checkState(0)),
                        json_f=str(self.formatos_copia_json.checkState(0)), json_ocult=str(self.formatos_copia_json_ocult.checkState(0)), json_cript=str(self.formatos_copia_json_cript.checkState(0)),
                        html_f=str(self.formatos_copia_html.checkState(0)), html_ocult=str(self.formatos_copia_html_ocult.checkState(0)), html_cript=str(self.formatos_copia_html_cript.checkState(0)),
                        xsl_f=str(self.formatos_copia_xls.checkState(0)), xsl_ocult=str(self.formatos_copia_xls_ocult.checkState(0)), xsl_cript=str(self.formatos_copia_xls_cript.checkState(0)),
                        db_f=str(self.formatos_copia_db.checkState(0)), db_ocult=str(self.formatos_copia_db_ocult.checkState(0)), db_cript=str(self.formatos_copia_db_cript.checkState(0)))

                with open(f'{path_central}/etc/parameters.txt') as pegar_conf_e:
                    pegar_ce = pegar_conf_e.read()

                    if 'email_notification:yes' in pegar_ce:

                        if 'email_body:yes' in pegar_ce:
                            expd = ('\n'.join(map(str, exportar_dados)))
                            expd = expd.replace('\n', '<br>')
                            expw = ('\n'.join(map(str, exportar_dados_wl)))
                            expw = expw.replace('\n', '<br>')
                            expp = ('\n'.join(map(str, exportar_dados_pbdb)))
                            expp = expp.replace('\n', '<br>')
                            expg = ('\n'.join(map(str, exportar_dados_dorks)))
                            expg = expg.replace('\n', '<br>')

                            corpo_email_dados = f'<strong>API results:<br></strong><br>{expd}<br><strong><br>Word Lists results:<br></strong><br>{expw}<br>' \
                                                f'<strong><br>Common Websites results:<br></strong><br>{expp}<br><strong><br><br>Google Dorks results:<br></strong><br>{expg}<br>'

                            try:
                                enviar_email_oblivion(status_nosafe=True, data_nosafe=corpo_email_dados)

                            except:
                                pass
                            
                        else:

                            try:
                                enviar_email_oblivion()

                            except:
                                pass
                            
                    if 'telegram_notification:yes' in pegar_ce:

                        if 'telegram_body:yes' in pegar_ce:
                            expd = ('\n'.join(map(str, exportar_dados)))
                            #expd = expd.replace('\n', '<br>')
                            expw = ('\n'.join(map(str, exportar_dados_wl)))
                            #expw = expw.replace('\n', '<br>')
                            expp = ('\n'.join(map(str, exportar_dados_pbdb)))
                            #expp = expp.replace('\n', '<br>')
                            expg = ('\n'.join(map(str, exportar_dados_dorks)))
                            #expg = expg.replace('\n', '<br>')

                            corpo_telegram_dados = f'\n*API results:*\n\n{expd}\n\n*Word Lists results:*\n\n{expw}\n'\
                                                f'\n*Common Websites results:*\n\n{expp}\n\n*Google Dorks results:*\n\n{expg}\n'

                            try:
                                notificar_telegram(status_nosafe=True, data_nosafe=corpo_telegram_dados)

                            except:
                                pass
                            
                        else:

                            try:
                                notificar_telegram()
                                
                            except:
                                pass
                            
                break

            if self.cancelar_analise == True:
                break

            if situacao_loop == False:
                break

        self.cancelar_analise = False
        logando_main('info', 'Scan successful')
        self.analise_nova_analise.setDisabled(False)
        self.analise_salvar.setDisabled(True)

        if self.db_fechar.isChecked():
            app.quit()

        if self.db_desligar.isChecked():
            try:
                os.system('shutdown /s')

            except:
                os.system('shutdown now')


    def pegar_dados_arquivo(self):
        """
        Collects data from database file/Coleta os dados do arquivo de banco de dados.
        """
        db_connect = create_engine(f'sqlite:///{db_file}')
        id_items_f = []
        id_items_limpo = []
        conn = db_connect.connect()

        try:
            query = conn.execute("select email from data")
            # id1 = ([i[0] for i in query.cursor.fetchall()])

            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00SHSTRx00'
                id_items_f.append(ii)

        except:
            pass

        try:
            query = conn.execute("select senha from data")
            # id1 = ([i[0] for i in query.cursor.fetchall()])

            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00EMSTRx00'
                id_items_f.append(ii)

        except:
            pass

        try:
            query = conn.execute("select documento from data")
            # id1 = ([i[0] for i in query.cursor.fetchall()])

            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00DMSTRx00'
                id_items_f.append(ii)

        except:
            pass

        for e in id_items_f:

            if e != '' and not ' ' in e and not 'None:' in e:
                id_items_limpo.append(e)

        return id_items_limpo


class WindowConfigOblivion(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Window of configuration/Janela de configuração.
    """
    def __init__(self):
        super().__init__()
        self.resize(701, 491)
        self.setWindowIcon(QtGui.QIcon(f'{path_central}/media/oblivion-256.png'))
        self.setMinimumSize(QSize(701, 491))
        self.setMaximumSize(QSize(701, 491))
        icon = QIcon()
        icon.addFile(u":/menu/media/oblivion-256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(QtGui.QIcon('/media/oblivion-256.png'))
        self.setWindowIcon(icon)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 711, 501))
        self.frame.setMinimumSize(QSize(681, 0))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_notificacao = QFrame(self.frame)
        self.frame_notificacao.setObjectName(u"frame_notificacao")
        self.frame_notificacao.setGeometry(QRect(101, 10, 601, 491))
        self.frame_notificacao.setFrameShape(QFrame.StyledPanel)
        self.frame_notificacao.setFrameShadow(QFrame.Raised)
        self.groupBox_2 = QGroupBox(self.frame_notificacao)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 8, 577, 251))
        self.plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(178, 20, 383, 71))
        self.plainTextEdit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 29, 160, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setChecked(False)
        self.verticalLayout_2.addWidget(self.checkBox_7)
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 100, 551, 141))
        self.groupBox_4 = QGroupBox(self.frame_notificacao)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(11, 270, 577, 181))
        self.plainTextEdit_3 = QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(180, 20, 383, 51))
        self.plainTextEdit_3.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 167, 55))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_12 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setChecked(True)
        self.verticalLayout_3.addWidget(self.checkBox_12)
        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setChecked(False)
        self.verticalLayout_3.addWidget(self.checkBox_8)
        self.plainTextEdit_4 = QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(10, 80, 553, 91))
        self.pushButton_2 = QPushButton(self.frame_notificacao)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(520, 456, 72, 26))
        self.pushButton_2.setStyleSheet(u"background-color: None;")
        self.frame_apis = QFrame(self.frame)
        self.frame_apis.setObjectName(u"frame_apis")
        self.frame_apis.setGeometry(QRect(102, 10, 601, 491))
        self.frame_apis.setFrameShape(QFrame.StyledPanel)
        self.frame_apis.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_apis)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(519, 456, 72, 26))
        self.pushButton.setStyleSheet(u"background-color: None;")
        self.groupBox = QGroupBox(self.frame_apis)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 8, 577, 111))
        self.formLayoutWidget_2 = QWidget(self.groupBox)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 20, 551, 81))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.formLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.checkBox)
        self.lineEdit = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit)
        self.checkBox_3 = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.checkBox_3)
        self.lineEdit_3 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_3)
        self.checkBox_4 = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)
        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.checkBox_4)
        self.lineEdit_5 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_5)
        self.groupBox_3 = QGroupBox(self.frame_apis)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 124, 577, 51))
        self.formLayoutWidget_3 = QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 20, 551, 22))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_14 = QCheckBox(self.formLayoutWidget_3)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setChecked(True)
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.checkBox_14)
        self.lineEdit_10 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_10)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 101, 491))
        self.widget.setStyleSheet(u"background-color: rgb(23, 44, 64);")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 101, 101))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"background-color:none;\n"
                                        "color:white;\n"
                                        "border-style: outset;\n"
                                        "border-radius:10px;\n"
                                        "border-color:black;\n"
                                        "font:bold 12px;\n"
                                        "padding: 6px;\n"
                                        "min-width:10px;")

        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"background-color:none;\n"
                                        "color:white;\n"
                                        "border-style: outset;\n"
                                        "border-radius:10px;\n"
                                        "border-color:black;\n"
                                        "font:bold 12px;\n"
                                        "padding: 6px;\n"
                                        "min-width:10px;")

        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"background-color:none;\n"
                                        "color:white;\n"
                                        "border-style: outset;\n"
                                        "border-radius:10px;\n"
                                        "border-color:black;\n"
                                        "font:bold 12px;\n"
                                        "padding: 6px;\n"
                                        "min-width:10px;")

        self.verticalLayout.addWidget(self.pushButton_6)
        #self.pushButton_7 = QPushButton(self.widget)
        #self.pushButton_7.setObjectName(u"pushButton_7")
        #self.pushButton_7.setGeometry(QRect(90, 210, 89, 26))
        #self.pushButton_7.setFont(font1)
        #self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        #self.pushButton_7.setStyleSheet(u"background-color:none;\n"
        #                                "color:white;\n"
        #                                "border-style: outset;\n"
        #                                "border-radius:10px;\n"
        #                                "border-color:black;\n"
        #                                "font:bold 12px;\n"
        #                                "padding: 6px;\n"
        #                                "min-width:10px;")
        self.frame_autenticacao = QFrame(self.frame)
        self.frame_autenticacao.setObjectName(u"frame_autenticacao")
        self.frame_autenticacao.setGeometry(QRect(101, 10, 601, 491))
        self.frame_autenticacao.setFrameShape(QFrame.StyledPanel)
        self.frame_autenticacao.setFrameShadow(QFrame.Raised)
        self.groupBox_5 = QGroupBox(self.frame_autenticacao)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(11, 8, 577, 91))
        self.formLayoutWidget = QWidget(self.groupBox_5)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(49, 22, 201, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)
        self.pushButton_8 = QPushButton(self.formLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color: None;")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_8)
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 12, 301, 61))
        self.verticalLayoutWidget_5 = QWidget(self.groupBox_5)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 20, 43, 21))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName(u"label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.groupBox_6 = QGroupBox(self.frame_autenticacao)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 225, 577, 81))
        self.formLayoutWidget_4 = QWidget(self.groupBox_6)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(49, 19, 201, 51))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.formLayoutWidget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: None;")
        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.pushButton_9)
        self.lineEdit_7 = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_7)
        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 14, 301, 51))
        self.verticalLayoutWidget_6 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 20, 41, 21))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_6)
        self.label_5.setObjectName(u"label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.pushButton_3 = QPushButton(self.frame_autenticacao)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(520, 456, 72, 26))
        self.pushButton_3.setStyleSheet(u"background-color: None;")
        self.groupBox_7 = QGroupBox(self.frame_autenticacao)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 107, 577, 111))
        self.formLayoutWidget_5 = QWidget(self.groupBox_7)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(49, 22, 201, 81))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_8 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit_8)
        self.lineEdit_9 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)
        self.pushButton_10 = QPushButton(self.formLayoutWidget_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"background-color: None;")
        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.pushButton_10)
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(270, 34, 301, 41))
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_7)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 22, 41, 41))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.widget.raise_()
        self.frame_notificacao.raise_()
        self.frame_autenticacao.raise_()
        self.frame_apis.raise_()
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        self.pushButton_4.clicked.connect(self.frame_apis.
        raise_)
        self.pushButton_5.clicked.connect(self.frame_notificacao.
        raise_)
        self.pushButton_6.clicked.connect(self.frame_autenticacao.
        raise_)
        QMetaObject.connectSlotsByName(self)

        with open(f'{path_central}/etc/email/body.html', 'r') as pegar_html:
            corpo_do_html = str(pegar_html.read())

        with open(f'{path_central}/etc/notification/message.txt', 'r') as pegar_mensagem:
            corpo_da_mensagem = str(pegar_mensagem.read())

        self.plainTextEdit_2.setPlainText(corpo_do_html)
        self.plainTextEdit_4.setPlainText(corpo_da_mensagem)

        with open(f'{path_central}/etc/api/keys_db.txt', 'r') as pegar_keys_f:
            conteudo_keys_f = pegar_keys_f.read().split('\n')
            for e in conteudo_keys_f:

                if 'intelligencex_key' in e:
                    e = e.split(' ')
                    intelligencex_key_f = str(e[2].replace("'", ''))

                if 'haveibeenpwned_key' in e:
                    e = e.split(' ')
                    haveibeenpwned_key_f = str(e[2].replace("'", ''))

                if 'telegram_bot' in e:
                    e = e.split(' ')
                    telegram_bot_f = str(e[2].replace("'", ''))

        # setando keys
        self.lineEdit.setText(intelligencex_key_f)
        self.lineEdit_3.setText(haveibeenpwned_key_f)
        self.lineEdit_10.setText(telegram_bot_f)

        with open(f'{path_central}/etc/config', 'r') as aplicar_config:
            configs = aplicar_config.read()
            configs = str(configs)

            if 'intelx:yes' in configs:
                self.checkBox.setChecked(1)

            else:
                self.checkBox.setChecked(0)

            if 'haveipwned:yes' in configs:
                self.checkBox_3.setChecked(1)

            else:
                self.checkBox_3.setChecked(0)

            if 'scylla:yes' in configs:
                self.checkBox_4.setChecked(1)

            else:
                self.checkBox_4.setChecked(0)

        self.pushButton.clicked.connect(self.salvar_configs)
        self.pushButton_3.clicked.connect(self.salvar_configs)
        self.pushButton_2.clicked.connect(self.salvar_configs)

        with open(f'{path_central}/etc/parameters.txt', 'r') as aplicar_not:
            e_ap = aplicar_not.read()

            if 'email_notification:yes' in e_ap:
                self.checkBox_2.setChecked(1)

            else:
                self.checkBox_2.setChecked(0)

            if 'email_body:yes' in e_ap:
                self.checkBox_7.setChecked(1)

            else:
                self.checkBox_7.setChecked(0)

            if 'telegram_notification:yes' in e_ap:
                self.checkBox_12.setChecked(1)

            else:
                self.checkBox_12.setChecked(0)

            if 'telegram_body:yes' in e_ap:
                self.checkBox_8.setChecked(1)

            else:
                self.checkBox_8.setChecked(0)

        with open(f'{path_central}/etc/email/emails.txt', 'r') as lista_emails:
            aplicar_lista = lista_emails.read()
            self.plainTextEdit.setPlainText(aplicar_lista)

        with open(f'{path_central}/etc/notification/users.txt', 'r') as lista_ids:
            aplicar_ids = lista_ids.read()
            self.plainTextEdit_3.setPlainText(aplicar_ids)

        self.pushButton_8.clicked.connect(self.autenticar_id_gd)
        self.pushButton_10.clicked.connect(self.aplicar_gmail)
        self.pushButton_9.clicked.connect(self.aplicar_tbot)

    def aplicar_tbot(self):
        """
        Authentication of Telegram Bot/Autenticação do Bot de Telegram.
        """
        with open(f'{path_central}/etc/api/keys_db.txt', 'r') as aplicar_bk:
            conteudo_bk = aplicar_bk.read()
            conteudo_bk = conteudo_bk.split('\n')

        with open(f'{path_central}/etc/api/keys_db.txt', 'w') as novo_idb:
            for e in conteudo_bk:

                if not 'telegram_bot' in e and e != ' ' and e != '':
                    e = str(e)
                    novo_idb.write(f'{e}\n')

                if 'telegram_bot' in e and e != ' ' and e != '':
                    ee = str(self.lineEdit_7.text())
                    ee = ee.replace(' ', '')
                    novo_idb.write(f"telegram_bot = '{ee}'\n")

    def aplicar_gmail(self):
        """
        Add new email to file/Adiciona novo e-mail no arquivo.
        """
        with open(f'{path_central}/etc/email/parameters.txt', 'w') as aplicar_novo_p:
            v1 = (base64.b32encode(bytearray(f"{self.lineEdit_8.text()}", 'ascii')).decode('utf-8'))
            v2 = (base64.b32encode(bytearray(f"{self.lineEdit_9.text()}", 'ascii')).decode('utf-8'))
            aplicar_novo_p.write(f'id_1:{v1}\nid_2:{v2}')

    def autenticar_id_gd(self):
        """
        Authentication of Google Drive/Autenticação do Google Drive.
        """
        id_usuario = str(self.lineEdit_4.text())
        autenticar_id(id_usuario, f'authentication.txt',
                                 'text/plain', f'{path_central}/etc/api/googledrv/authentication.txt')
        with open(f'{path_central}/etc/api/googledrv/id_folder.txt', 'w') as novo_id:
            novo_id.write(id_usuario)

    def salvar_configs(self):
        """
        Saves the alterations of the configuration window/Salva as alterações da página de configuração.
        """
        k_intelx = f"intelligencex_key = '{self.lineEdit.text()}'"
        k_hibp = f"haveibeenpwned_key = '{self.lineEdit_3.text()}'"
        k_telegram = f"telegram_bot = '{self.lineEdit_10.text()}'"

        with open(f'{path_central}/etc/api/keys_db.txt', 'w') as aplicar_keys:
            aplicar_keys.write(f'{k_intelx}\n{k_hibp}\n{k_telegram}')

        with open(f'{path_central}/etc/config', 'w') as aplicar_checkbox:

            if self.checkBox.isChecked():
                aplicar_checkbox.write('intelx:yes\n')

            else:
                aplicar_checkbox.write('intelx:no\n')

            if self.checkBox_3.isChecked():
                aplicar_checkbox.write('haveipwned:yes\n')

            else:
                aplicar_checkbox.write('haveipwned:no\n')

            if self.checkBox_4.isChecked():
                aplicar_checkbox.write('scylla:yes\n')

            else:
                aplicar_checkbox.write('scylla:no\n')

        with open(f'{path_central}/etc/parameters.txt', 'w') as setar_not:

            if self.checkBox_2.isChecked():
                setar_not.write('email_notification:yes\n')

            else:
                setar_not.write('email_notification:no\n')

            if self.checkBox_7.isChecked():
                setar_not.write('email_body:yes\n')

            else:
                setar_not.write('email_body:no\n')

            if self.checkBox_12.isChecked():
                setar_not.write('telegram_notification:yes\n')

            else:
                setar_not.write('telegram_notification:no\n')

            if self.checkBox_8.isChecked():
                setar_not.write('telegram_body:yes\n')

            else:
                setar_not.write('telegram_body:no\n')

        with open(f'{path_central}/etc/email/emails.txt', 'w') as escrever_emails:
            escrever_emails.write(self.plainTextEdit.toPlainText())

        with open(f'{path_central}/etc/notification/users.txt', 'w') as escrever_ids:
            escrever_ids.write(self.plainTextEdit_3.toPlainText())

        with open(f'{path_central}/etc/email/body.html', 'w') as escrever_html:
            escrever_html.write(self.plainTextEdit_2.toPlainText())

        with open(f'{path_central}/etc/notification/message.txt', 'w') as escrever_mensagem:
            escrever_mensagem.write(self.plainTextEdit_4.toPlainText())


    def retranslateUi(self, MainWindow):
        """
        Applies the strings of the buttons/Aplica as strings dos botões.
        """
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Notify by e-mail", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Send scan result by \n"
                                                                         "e-mail (not secure)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Telegram", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Notify by telegram", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Send scan result by \n"
                                                                   "Telegram (not secure)", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Keys", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Intelx", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Have I Pwned", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Scylla", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Others", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"Telegram bot", None))
        self.lineEdit_10.setText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"APIs", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Autentication", None))
        #self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Google Drive", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Authenticate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"Before authenticate your Google Drive you need to activate\n"
                                                        "the  API of your  Google Drive  account and put the token in\n"
                                                        "root folder of Oblivion.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ID folder", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Telegram", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Authenticate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"Before authenticate  your Telegram bot you need to send a\n"                                                        
                                                        "mensage to bot.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"API bot", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"G-Mail", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Authenticate", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow",
                                                         u"Before  authenticate your g-mail account you need to allow\n"
                                                         "devices third-hand in the settings of your g-mail.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"G-mail", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Pass", None))


class Window2(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Window of send the passwords;e-mails;documents to database file/Janela de enviar credênciais para a database.
    """
    def __init__(self):
        super().__init__()
        self.resize(701, 486)
        self.setMinimumSize(QSize(701, 0))
        self.setMaximumSize(QSize(701, 16777215))
        icon = QIcon()
        icon.addFile(u":/menu/media/oblivion-256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 711, 501))
        self.frame.setMinimumSize(QSize(681, 0))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 23):
            self.tableWidget.setRowCount(23)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, __qtablewidgetitem25)

        vl = self.db_data()
        xc = 0
        yc = 0
        zc = 0
        try:
            for e in vl:

                if ':00EMSTRx00' in e:
                    e = e.replace(':00EMSTRx00', '')
                    self.tableWidget.setItem(yc, 0, QTableWidgetItem(e))
                    yc += 1

                if ':00SHSTRx00' in e:
                    e = e.replace(':00SHSTRx00', '')
                    self.tableWidget.setItem(xc, 1, QTableWidgetItem(e))
                    xc += 1

                if ':00DMSTRx00' in e:
                    e = e.replace(':00DMSTRx00', '')
                    self.tableWidget.setItem(zc, 2, QTableWidgetItem(e))
                    zc += 1
        except:
            pass

        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(14, 49, 673, 432))
        self.tableWidget.setStyleSheet(u"background-color: None;")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(608, 20, 80, 22))
        self.pushButton.setStyleSheet(u"background-color: none;")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.salvar_db)


    def salvar_db(self):
        """
        Sends the credentials to database file/Envia os dados para o arquivo database.
        """
        try:
            os.remove(db_file)
            xxx = 0
            conn = sqlite3.connect(db_file)
            c = conn.cursor()
            c.execute('''CREATE TABLE data (email text, senha text, documento text)''')
            contar_x = int(self.tableWidget.rowCount()) # linha
            contar_y = int(self.tableWidget.columnCount()) # coluna
            temp_x = 0
            temp_y = 0
            total_contar = contar_x * contar_y
            tmp_lista_db = []

            for e in range(contar_x * contar_y):
                situacao = str(self.tableWidget.item(temp_x, temp_y))

                if 'object' in situacao:
                    dados_tabela = self.tableWidget.item(temp_x, temp_y).text()
                    tmp_lista_db.append(dados_tabela)

                if situacao == 'None':
                    tmp_lista_db.append('None')

                if temp_y == 2:
                    if tmp_lista_db[0] == '':
                        tmp_lista_db[0] = 'None'

                    if tmp_lista_db[1] == '':
                        tmp_lista_db[1] = 'None'

                    if tmp_lista_db[2] == '':
                        tmp_lista_db[2] = 'None'

                    c.execute(f'''INSERT INTO data
                                    VALUES('{tmp_lista_db[0]}', '{tmp_lista_db[1]}', '{tmp_lista_db[2]}')''')
                    temp_y = -1
                    temp_x += 1
                    tmp_lista_db.clear()

                temp_y += 1

            conn.commit()
            conn.close()

        except:
            pass


    def db_data(self):
        """
        Collects data from database file/Coletando dados do arquivo de database.
        """
        db_connect = create_engine(f'sqlite:///{db_file}')
        id_items2 = []
        conn = db_connect.connect()

        try:
            query = conn.execute("select email from data")
            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00EMSTRx00'
                id_items2.append(ii)

        except:
            logando_main('warning', 'Was not possible to load the passwords')


        try:
            query = conn.execute("select senha from data")
            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00SHSTRx00'
                id_items2.append(ii)

        except:
            logando_main('warning', 'Was not possible to load the passwords')

        try:
            query = conn.execute("select documento from data")

            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00DMSTRx00'
                id_items2.append(ii)

        except:
            logando_main('warning', 'Was not possible to load the documents')

        arrumar_id_items2 = []
        for ef in id_items2:

            if 'None:' in ef:
                ef = ''
                arrumar_id_items2.append(ef)
            arrumar_id_items2.append(ef)

        return arrumar_id_items2


    def retranslateUi(self, MainWindow):
        """
        Applies the strings of the buttons/Aplica as strings dos botões.
        """
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"passwords", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"e-mails", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"documents", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(20)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(21)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(22)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"23", None));
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))


if __name__ == "__main__":
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
