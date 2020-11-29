#!/usr/bin/python

import coloredlogs
import verboselogs
import logging
import pathlib
from etc.serverx.config.config_server import *
from etc.email.send_email import *
from etc.api.scylla import *
from etc.api.intelxapi import *
from etc.api.intelligencex import *
from etc.api.hibpwned import *
from etc.scrap.wordlists_search import *
from etc.scrap.pastebin import *
from etc.scrap.google_dorks import *
#from etc.api.cves import *
from etc.create import *
from etc.notification.telegram import *
from etc.decript import decript_file
from etc.api.keys import *
from etc.serverx.config.config_server import *


# Global variables/Variáveis globais.
path_atual_server_w = str(pathlib.Path(__file__).parent.absolute())
path_server_w = path_atual_server_w.replace('/etc/serverx/system/windows','')


def logando_wp(tipo, mensagem):
    """
    Generates the log message/Gera a mensagem de log.

    :param tipo: Sets the log type/Seta o tipo de log
    :param mensagem: Sets the message of log/Seta a mensagem do log
    :return: Returns the complete log's body/Retorna o corpo completo do log
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


def srv_aplicar_separar(dados, atributos, loop_scan=False, key=None):
    """
    :param dados: Password, e-mail or document/Senha, e-mail ou documento.
    :param atributos: Attributes of file formats/Atributos dos formatos do arquivo
    :param loop_scan: Scan in loop mode/Scan em modo contínuo.
    """
    while True:
        #print(dados,atributos)
        dados_separados = dados
        srv_exportar_dados = []
        srv_exportar_dados_wl = []
        srv_exportar_dados_pbdb = []
        srv_exportar_dados_dorks = []
        srv_exportar_dados_nltk = []
        srv_exportar_dados_cves = []

        if 'common_web' in atributos:
            modulos_modulos_dataleak_common = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            modulos_modulos_dataleak_common = False

        if 'google_dorks' in atributos:
            modulos_modulos_dataleak_googledorks = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            modulos_modulos_dataleak_googledorks = False

        if 'wordlists' in atributos:
            modulos_modulos_dataleak_wordlist = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            modulos_modulos_dataleak_wordlist = False

        if 'api' in atributos:
            modulos_modulos_dataleak_api = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            modulos_modulos_dataleak_api = False

        if 'dado_bruto' in atributos:
            formatos_copia_dadobruto = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            formatos_copia_dadobruto = False

        if 'txt_f' in atributos:
            txt_f = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            txt_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'txt_ocult' in atributos:
            txt_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            txt_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'txt_cript' in atributos:
            txt_cript = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            txt_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'docx_f' in atributos:
            docx_f = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            docx_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'docx_ocult' in atributos:
            docx_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            docx_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'docx_cript' in atributos:
            docx_cript = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            docx_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'pdf_f' in atributos:
            pdf_f = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            pdf_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'pdf_ocult' in atributos:
            pdf_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            pdf_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'pdf_cript' in atributos:
            pdf_cript = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            pdf_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'xlsx_f' in atributos:
            xlsx_f = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            xlsx_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'xlsx_ocult' in atributos:
            xlsx_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            xlsx_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'xlsx_cript' in atributos:
            xlsx_cript = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            xlsx_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'json_f' in atributos:
            json_f = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            json_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'json_ocult' in atributos:
            json_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            json_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'json_cript' in atributos:
            json_cript = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            json_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'html_f' in atributos:
            html_f = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            html_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'html_ocult' in atributos:
            html_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            html_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'html_cript' in atributos:
            html_cript = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            html_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'xsl_f' in atributos:
            xsl_f = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            xsl_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'xsl_ocult' in atributos:
            xsl_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            xsl_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'xsl_cript' in atributos:
            xsl_cript = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            xsl_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'db_f' in atributos:
            db_f = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            db_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'db_ocult' in atributos:
            db_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            db_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'db_cript' in atributos:
            db_cript = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            db_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'gdrive' in atributos:
            gdrive = 'PySide2.QtCore.Qt.CheckState.Checked'

        else:
            gdrive = 'PySide2.QtCore.Qt.CheckState.Unchecked'

        if 'aws_s3' in atributos:
            aws_s3 = True

        else:
            aws_s3 = False

        if 'ssh' in atributos:
            ssh_enviar = True

        else:
            ssh_enviar = False

        if modulos_modulos_dataleak_common:
            srv_exportar_dados_pbdb = []

            for i in dados_separados:

                if '00SHSTRx00' in i:
                    i = i.replace(':00SHSTRx00', '')
                    i = str(i)

                    if formatos_copia_dadobruto:
                        puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(gdrive))
                        srv_exportar_dados_pbdb.append(puxar_pbdb)

                    else:
                        puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(gdrive))
                        srv_exportar_dados_pbdb.append(puxar_pbdb)

                if '00EMSTRx00' in i:
                    i = i.replace(':00EMSTRx00', '')
                    i = str(i)

                    if formatos_copia_dadobruto:
                        puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(gdrive))
                        srv_exportar_dados_pbdb.append(puxar_pbdb)

                    else:
                        puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(gdrive))
                        srv_exportar_dados_pbdb.append(puxar_pbdb)

                if '00DMSTRx00' in i:
                    i = i.replace(':00DMSTRx00', '')
                    i = str(i)

                    if formatos_copia_dadobruto:
                        puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(gdrive))
                        srv_exportar_dados_pbdb.append(puxar_pbdb)

                    else:
                        puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(gdrive))
                        srv_exportar_dados_pbdb.append(puxar_pbdb)

        if modulos_modulos_dataleak_googledorks:
            srv_exportar_dados_dorks = []
            for i in dados_separados:

                if '00SHSTRx00' in i:
                    i = i.replace(':00SHSTRx00', '')

                    if formatos_copia_dadobruto:
                        dados_dorks_separados = google_scrap(termo=i, dadobruto=True,
                                                             gdr=str(gdrive))
                        srv_exportar_dados_dorks.append(dados_dorks_separados)

                    else:
                        dados_dorks_separados = google_scrap(termo=i, dadobruto=False,
                                                             gdr=str(gdrive))
                        srv_exportar_dados_dorks.append(dados_dorks_separados)

                elif '00EMSTRx00' in i:
                    i = i.replace(':00EMSTRx00', '')

                    if formatos_copia_dadobruto:
                        dados_dorks_separados = google_scrap(termo=i, dadobruto=True,
                                                             gdr=str(gdrive))
                        srv_exportar_dados_dorks.append(dados_dorks_separados)

                    else:
                        dados_dorks_separados = google_scrap(termo=i, dadobruto=False,
                                                             gdr=str(gdrive))
                        srv_exportar_dados_dorks.append(dados_dorks_separados)

                if '00DMSTRx00' in i:
                    i = i.replace(':00DMSTRx00', '')

                    if formatos_copia_dadobruto:
                        dados_dorks_separados = google_scrap(termo=i, dadobruto=True,
                                                             gdr=str(gdrive))
                        srv_exportar_dados_dorks.append(dados_dorks_separados)

                    else:
                        dados_dorks_separados = google_scrap(termo=i, dadobruto=False,
                                                             gdr=str(gdrive))
                        srv_exportar_dados_dorks.append(dados_dorks_separados)

        if modulos_modulos_dataleak_wordlist:
            srv_exportar_dados_wl = []
            for i in dados_separados:

                if '00SHSTRx00' in i:
                    i = i.replace(':00SHSTRx00', '')
                    dados_wl_separados = verificar_dados(i)
                    srv_exportar_dados_wl += dados_wl_separados

        if modulos_modulos_dataleak_api:
            for i in dados_separados:

                if '00EMSTRx00' in i:
                    i = i.replace(':00EMSTRx00', '')

                    # Have I Been Pwned/email
                    if situacaoHaveIPwned == True:
                        listaf_haveipwned = check_breach(i)
                        for ex3 in listaf_haveipwned:
                            if i in ex3:
                                srv_exportar_dados.append(ex3)

                    # Scylla/email
                    if situacaoScylla == True:
                        temp_scyla = []
                        if formatos_copia_dadobruto:
                            listaf_scylla = chamar_limpar_scylla(email=i, dadobruto=True,
                                                                 gdr=str(gdrive))
                            for ex1 in listaf_scylla:

                                if i in ex1:
                                    srv_exportar_dados.append(ex1)
                                    temp_scyla.append(ex1)

                            for item_lista in temp_scyla:
                                list_temporaria = item_lista.split(':')
                                dominio_vazado = list_temporaria[2]
                                scylla_dado_bruto(dominio_vazado, gdr=str(gdrive))

                        else:
                            listaf_scylla = chamar_limpar_scylla(email=i)
                            for ex1 in listaf_scylla:

                                if i in ex1:
                                    srv_exportar_dados.append(ex1)

                    # Intelligencex/email
                    if situacaoIntelx == True:

                        if formatos_copia_dadobruto:
                            listaf_inteligencex = intelligencex_sid_raw(termo=i, conteudobruto=True, gdr=gdix)
                            for ex2 in listaf_inteligencex:

                                if i in ex2:
                                    srv_exportar_dados.append(ex2)

                        else:
                            listaf_inteligencex = intelligencex_sid_raw(termo=i)
                            for ex2 in listaf_inteligencex:

                                if i in ex2:
                                    srv_exportar_dados.append(ex2)

                elif '00SHSTRx00' in i:
                    i = i.replace(':00SHSTRx00', '')

                    # Have I Been Pwned/senha
                    if situacaoHaveIPwned == True:
                        listaf_haveipwned = check_breach(i)
                        for ex3 in listaf_haveipwned:

                            if i in ex3:
                                srv_exportar_dados.append(ex3)

                    # Scylla/senha
                    if situacaoScylla == True:
                        temp_scyla = []

                        if formatos_copia_dadobruto:
                            listaf_scylla = chamar_limpar_scylla(senha=i, dadobruto=True,
                                                                 gdr=str(gdrive))
                            for ex1 in listaf_scylla:

                                if i in ex1:
                                    srv_exportar_dados.append(ex1)
                                    temp_scyla.append(ex1)

                            for item_lista in temp_scyla:
                                list_temporaria = item_lista.split(':')
                                dominio_vazado = list_temporaria[2]
                                scylla_dado_bruto(dominio_vazado, gdr=str(gdrive))

                        else:
                            listaf_scylla = chamar_limpar_scylla(senha=i)
                            for ex1 in listaf_scylla:

                                if i in ex1:
                                    srv_exportar_dados.append(ex1)

                elif '00DMSTRx00' in i:
                    i = i.replace(':00DMSTRx00', '')
                    # Intelligencex/documents

                    if situacaoIntelx == True:

                        if formatos_copia_dadobruto:
                            listaf_inteligencex = intelligencex_sid_raw(termo=i, conteudobruto=True, gdr=gdix)
                            for ex2 in listaf_inteligencex:

                                if i in ex2:
                                    srv_exportar_dados.append(ex2)

                        else:
                            listaf_inteligencex = intelligencex_sid_raw(termo=i)
                            for ex2 in listaf_inteligencex:

                                if i in ex2:
                                    srv_exportar_dados.append(ex2)

        if srv_exportar_dados or srv_exportar_dados_wl or srv_exportar_dados_pbdb or srv_exportar_dados_dorks:

            if srv_exportar_dados:
                gerar_resultados(serverx=True, ssh_enviar=ssh_enviar, aws_s3_gerar=aws_s3, key=key,
                                 nome='API_', conteudo=srv_exportar_dados,
                                 gdrive=str(gdrive),
                                 txt_f=str(txt_f),
                                 txt_ocult=str(txt_ocult),
                                 txt_cript=str(txt_cript),
                                 docx_f=str(docx_f),
                                 docx_ocult=str(docx_ocult),
                                 docx_cript=str(docx_cript),
                                 pdf_f=str(pdf_f),
                                 pdf_ocult=str(pdf_ocult),
                                 pdf_cript=str(pdf_cript),
                                 xlsx_f=str(xlsx_f),
                                 xlsx_ocult=str(xlsx_ocult),
                                 xlsx_cript=str(xlsx_cript),
                                 json_f=str(json_f),
                                 json_ocult=str(json_ocult),
                                 json_cript=str(json_cript),
                                 html_f=str(html_f),
                                 html_ocult=str(html_ocult),
                                 html_cript=str(html_cript),
                                 xsl_f=str(xsl_f),
                                 xsl_ocult=str(xsl_ocult),
                                 xsl_cript=str(xlsx_cript),
                                 db_f=str(db_f),
                                 db_ocult=str(db_ocult),
                                 db_cript=str(db_cript))

            if srv_exportar_dados_wl:
                gerar_resultados(serverx=True, ssh_enviar=ssh_enviar, aws_s3_gerar=aws_s3, key=key,
                                 nome='WORDLIST_', conteudo=srv_exportar_dados_wl, gdrive=str(gdrive),
                                 txt_f=str(txt_f),
                                 txt_ocult=str(txt_ocult),
                                 txt_cript=str(txt_cript),
                                 docx_f=str(docx_f),
                                 docx_ocult=str(docx_ocult),
                                 docx_cript=str(docx_cript),
                                 pdf_f=str(pdf_f),
                                 pdf_ocult=str(pdf_ocult),
                                 pdf_cript=str(pdf_cript),
                                 xlsx_f=str(xlsx_f),
                                 xlsx_ocult=str(xlsx_ocult),
                                 xlsx_cript=str(xlsx_cript),
                                 json_f=str(json_f),
                                 json_ocult=str(json_ocult),
                                 json_cript=str(json_cript),
                                 html_f=str(html_f),
                                 html_ocult=str(html_ocult),
                                 html_cript=str(html_cript),
                                 xsl_f=str(xsl_f),
                                 xsl_ocult=str(xsl_ocult),
                                 xsl_cript=str(xlsx_cript),
                                 db_f=str(db_f),
                                 db_ocult=str(db_ocult),
                                 db_cript=str(db_cript))

            if srv_exportar_dados_pbdb:
                gerar_resultados(serverx=True, ssh_enviar=ssh_enviar, aws_s3_gerar=aws_s3, key=key,
                                 nome='COMMONWEBSITES_', conteudo=srv_exportar_dados_pbdb, gdrive=str(gdrive),
                                 txt_f=str(txt_f),
                                 txt_ocult=str(txt_ocult),
                                 txt_cript=str(txt_cript),
                                 docx_f=str(docx_f),
                                 docx_ocult=str(docx_ocult),
                                 docx_cript=str(docx_cript),
                                 pdf_f=str(pdf_f),
                                 pdf_ocult=str(pdf_ocult),
                                 pdf_cript=str(pdf_cript),
                                 xlsx_f=str(xlsx_f),
                                 xlsx_ocult=str(xlsx_ocult),
                                 xlsx_cript=str(xlsx_cript),
                                 json_f=str(json_f),
                                 json_ocult=str(json_ocult),
                                 json_cript=str(json_cript),
                                 html_f=str(html_f),
                                 html_ocult=str(html_ocult),
                                 html_cript=str(html_cript),
                                 xsl_f=str(xsl_f),
                                 xsl_ocult=str(xsl_ocult),
                                 xsl_cript=str(xlsx_cript),
                                 db_f=str(db_f),
                                 db_ocult=str(db_ocult),
                                 db_cript=str(db_cript))

            if srv_exportar_dados_dorks and srv_exportar_dados_dorks != None and srv_exportar_dados_dorks != 'None':
                gerar_resultados(serverx=True, ssh_enviar=ssh_enviar, aws_s3_gerar=aws_s3, key=key,
                                 nome='DORKS_', conteudo=srv_exportar_dados_dorks, gdrive=str(gdrive),
                                 txt_f=str(txt_f),
                                 txt_ocult=str(txt_ocult),
                                 txt_cript=str(txt_cript),
                                 docx_f=str(docx_f),
                                 docx_ocult=str(docx_ocult),
                                 docx_cript=str(docx_cript),
                                 pdf_f=str(pdf_f),
                                 pdf_ocult=str(pdf_ocult),
                                 pdf_cript=str(pdf_cript),
                                 xlsx_f=str(xlsx_f),
                                 xlsx_ocult=str(xlsx_ocult),
                                 xlsx_cript=str(xlsx_cript),
                                 json_f=str(json_f),
                                 json_ocult=str(json_ocult),
                                 json_cript=str(json_cript),
                                 html_f=str(html_f),
                                 html_ocult=str(html_ocult),
                                 html_cript=str(html_cript),
                                 xsl_f=str(xsl_f),
                                 xsl_ocult=str(xsl_ocult),
                                 xsl_cript=str(xlsx_cript),
                                 db_f=str(db_f),
                                 db_ocult=str(db_ocult),
                                 db_cript=str(db_cript))

            json_rs = {}
            json_rs['APIs'] = srv_exportar_dados
            json_rs['Word lists'] = srv_exportar_dados_wl
            json_rs['Common websites'] = srv_exportar_dados_pbdb
            json_rs['GoogleDorks'] = srv_exportar_dados_dorks

            with open(f'{path_server_w}/etc/parameters.txt') as pegar_conf_e:
                pegar_ce = pegar_conf_e.read()

                if 'email_notification:yes' in pegar_ce:

                    if 'email_body:yes' in pegar_ce:
                        expd = ('\n'.join(map(str, srv_exportar_dados)))
                        expd = expd.replace('\n', '<br>')
                        expw = ('\n'.join(map(str, srv_exportar_dados_wl)))
                        expw = expw.replace('\n', '<br>')
                        expp = ('\n'.join(map(str, srv_exportar_dados_pbdb)))
                        expp = expp.replace('\n', '<br>')
                        expg = ('\n'.join(map(str, srv_exportar_dados_dorks)))
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
                        expd = ('\n'.join(map(str, srv_exportar_dados)))
                        # expd = expd.replace('\n', '<br>')
                        expw = ('\n'.join(map(str, srv_exportar_dados_wl)))
                        # expw = expw.replace('\n', '<br>')
                        expp = ('\n'.join(map(str, srv_exportar_dados_pbdb)))
                        # expp = expp.replace('\n', '<br>')
                        expg = ('\n'.join(map(str, srv_exportar_dados_dorks)))
                        # expg = expg.replace('\n', '<br>')

                        corpo_telegram_dados = f'\n*API results:*\n\n{expd}\n\n*Word Lists results:*\n\n{expw}\n' \
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

            return json_rs
        
            break


        if loop_scan == False:
            break
