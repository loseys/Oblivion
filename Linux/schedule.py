import os
import sys
import time
import pathlib
from sqlalchemy import create_engine
import coloredlogs
import verboselogs

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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


# Global variables/Variáveis globais.
db_name = 'data.db'
path_atual = str(pathlib.Path(__file__).parent.absolute())
db_path = path_atual.replace('\etc','')

exportar_dados = []
exportar_dados_wl =[]
exportar_dados_pbdb = []
exportar_dados_dorks = []
exportar_dados_nltk = []
exportar_dados_cves = []

with open(sys.argv[1], 'r') as s_config:
    script_c = s_config.read()

def db_data2():
    """
    - Connects to database file/Conecta ao arquivo database.

    - Reads the script created and separates all the variables of files/Lê o arquivo de script criado e separa todas as
    variaveis dos arquivos.

    - Executes the modules/Executa os módulos.

    - Saves the results/Salva os resultados

    - Notifies the user/Notifica o usuário.
    """
    db_connect = create_engine(f'sqlite:///{db_path}/{db_name}')
    id_items2 = []
    conn = db_connect.connect()

    try:
        query = conn.execute("select email from data")
        # id1 = ([i[0] for i in query.cursor.fetchall()])

        for i in query.cursor.fetchall():
            ii = str(i[0])
            ii += ':00SHSTRx00'
            id_items2.append(ii)

    except:
        pass

    try:
        query = conn.execute("select senha from data")
        # id1 = ([i[0] for i in query.cursor.fetchall()])

        for i in query.cursor.fetchall():
            ii = str(i[0])
            ii += ':00EMSTRx00'
            id_items2.append(ii)

    except:
        pass

    try:
        query = conn.execute("select documento from data")
        # id1 = ([i[0] for i in query.cursor.fetchall()])

        for i in query.cursor.fetchall():
            ii = str(i[0])
            ii += ':00DMSTRx00'
            id_items2.append(ii)

    except:
        pass

    arrumar_id_items2 = []
    for ef in id_items2:

        if not 'None:' in ef and ef != '' and not ' ' in ef and ':' in ef:
            arrumar_id_items2.append(ef)

    return arrumar_id_items2

dados_separados = db_data2()

if 'agenda_modulos_vulscan=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    modulos_modulos_vulscan= 'PySide2.QtCore.Qt.CheckState.Checked'

else:
    modulos_modulos_vulscan = False

modulos_modulos_naturallanguage = False

modulos_modulos_dataleak_personalizada = False

if 'agenda_modulos_commonwebsites=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    modulos_modulos_dataleak_common = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    modulos_modulos_dataleak_common = False

if 'agenda_modulos_googledorks=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    modulos_modulos_dataleak_googledorks = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    modulos_modulos_dataleak_googledorks = False

if 'agenda_modulos_wordlists=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    modulos_modulos_dataleak_wordlist = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    modulos_modulos_dataleak_wordlist = False

if 'agenda_modulos_leak_api=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    modulos_modulos_dataleak_api = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    modulos_modulos_dataleak_api = False

if 'agenda_gerar_copia_dadobruto=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    formatos_copia_dadobruto = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    formatos_copia_dadobruto = False

if 'agenda_gerar_copia_txt=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    txt_f = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    txt_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_txt_ocult=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    txt_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    txt_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_txt_cript=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    txt_cript = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    txt_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_docx=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    docx_f = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    docx_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_docx_ocult=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    docx_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    docx_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_docx_cript=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    docx_cript = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    docx_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_pdf=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    pdf_f = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    pdf_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_pdf_ocult=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    pdf_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    pdf_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_pdf_cript=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    pdf_cript = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    pdf_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_xlsx=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    xlsx_f = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    xlsx_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_xlsx_ocult=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    xlsx_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    xlsx_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_xlsx_cript=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    xlsx_cript = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    xlsx_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_json=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    json_f = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    json_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_json_ocult=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    json_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    json_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_json_cript=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    json_cript = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    json_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_html=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    html_f = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    html_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_html_ocult=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    html_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    html_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_html_cript=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    html_cript = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    html_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_xsl=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    xsl_f = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    xsl_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_xsl_ocult=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    xsl_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    xsl_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_xsl_cript=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    xsl_cript = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    xsl_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_db=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    db_f = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    db_f = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_db_ocult=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    db_ocult = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    db_ocult = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_copia_db_cript=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    db_cript = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    db_cript = 'PySide2.QtCore.Qt.CheckState.Unchecked'

if 'agenda_gerar_dadobruto=PySide2.QtCore.Qt.CheckState.Checked' in script_c:
    gdrive = 'PySide2.QtCore.Qt.CheckState.Checked'
    gdix = 'PySide2.QtCore.Qt.CheckState.Checked'
else:
    gdrive = 'PySide2.QtCore.Qt.CheckState.Unchecked'
    gdix = 'PySide2.QtCore.Qt.CheckState.Unchecked'

print(path_atual)

with open(f'{path_atual}/etc/config', 'r') as file:
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

if modulos_modulos_dataleak_common:
    exportar_dados_pbdb = []

    for i in dados_separados:
        if '00SHSTRx00' in i:
            i = i.replace(':00SHSTRx00', '')
            i = str(i)

            if formatos_copia_dadobruto:
                puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(gdrive))
                exportar_dados_pbdb.append(puxar_pbdb)

            else:
                puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(gdrive))
                exportar_dados_pbdb.append(puxar_pbdb)

        if '00EMSTRx00' in i:
            i = i.replace(':00EMSTRx00', '')
            i = str(i)
            if formatos_copia_dadobruto:
                puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(gdrive))
                exportar_dados_pbdb.append(puxar_pbdb)

            else:
                puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(gdrive))
                exportar_dados_pbdb.append(puxar_pbdb)

        if '00DMSTRx00' in i:
            i = i.replace(':00DMSTRx00', '')
            i = str(i)
            if formatos_copia_dadobruto:
                puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=True, gdr=str(gdrive))
                exportar_dados_pbdb.append(puxar_pbdb)

            else:
                puxar_pbdb = verificar_ultimos_pb(credencial=i, dadobruto=False, gdr=str(gdrive))
                exportar_dados_pbdb.append(puxar_pbdb)

if modulos_modulos_dataleak_personalizada:
    pass

if modulos_modulos_dataleak_googledorks:
    exportar_dados_dorks = []
    for i in dados_separados:
        if '00SHSTRx00' in i:
            i = i.replace(':00SHSTRx00', '')
            if formatos_copia_dadobruto:
                dados_dorks_separados = google_scrap(termo=i, dadobruto=True,
                                                     gdr=str(gdrive))
                exportar_dados_dorks.append(dados_dorks_separados)
            else:
                dados_dorks_separados = google_scrap(termo=i, dadobruto=False,
                                                     gdr=str(gdrive))
                exportar_dados_dorks.append(dados_dorks_separados)

        elif '00EMSTRx00' in i:
            i = i.replace(':00EMSTRx00', '')
            if formatos_copia_dadobruto:
                dados_dorks_separados = google_scrap(termo=i, dadobruto=True,
                                                     gdr=str(gdrive))
                exportar_dados_dorks.append(dados_dorks_separados)
            else:
                dados_dorks_separados = google_scrap(termo=i, dadobruto=False,
                                                     gdr=str(gdrive))
                exportar_dados_dorks.append(dados_dorks_separados)

        if '00DMSTRx00' in i:
            i = i.replace(':00DMSTRx00', '')
            if formatos_copia_dadobruto:
                dados_dorks_separados = google_scrap(termo=i, dadobruto=True,
                                                     gdr=str(gdrive))
                exportar_dados_dorks.append(dados_dorks_separados)
            else:
                dados_dorks_separados = google_scrap(termo=i, dadobruto=False,
                                                     gdr=str(gdrive))
                exportar_dados_dorks.append(dados_dorks_separados)

if modulos_modulos_dataleak_wordlist:
    exportar_dados_wl = []
    for i in dados_separados:
        if '00SHSTRx00' in i:
            i = i.replace(':00SHSTRx00','')
            dados_wl_separados = verificar_dados(i)
            exportar_dados_wl += dados_wl_separados

if modulos_modulos_dataleak_api:
    for i in dados_separados:
        if '00EMSTRx00' in i:
            i = i.replace(':00EMSTRx00', '')

            # Have I Been Pwned/email
            if situacaoHaveIPwned == True:
                listaf_haveipwned = check_breach(i)
                for ex3 in listaf_haveipwned:
                    if i in ex3:
                        exportar_dados.append(ex3)

            # Scylla/email
            if situacaoScylla == True:
                temp_scyla = []
                if formatos_copia_dadobruto:
                    listaf_scylla = chamar_limpar_scylla(email=i, dadobruto=True,
                                                         gdr=str(gdrive))
                    for ex1 in listaf_scylla:
                        if i in ex1:
                            exportar_dados.append(ex1)
                            temp_scyla.append(ex1)
                    for item_lista in temp_scyla:
                        list_temporaria = item_lista.split(':')
                        dominio_vazado = list_temporaria[2]
                        scylla_dado_bruto(dominio_vazado, gdr=str(gdrive))
                else:
                    listaf_scylla = chamar_limpar_scylla(email=i)
                    for ex1 in listaf_scylla:
                        if i in ex1:
                            exportar_dados.append(ex1)

            # Intelligencex/email
            if situacaoIntelx == True:
                if formatos_copia_dadobruto:
                    listaf_inteligencex = intelligencex_sid_raw(termo=i, conteudobruto=True, gdr=gdix)
                    for ex2 in listaf_inteligencex:
                        if i in ex2:
                            exportar_dados.append(ex2)
                else:
                    listaf_inteligencex = intelligencex_sid_raw(termo=i)
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
                if formatos_copia_dadobruto:
                    listaf_scylla = chamar_limpar_scylla(senha=i, dadobruto=True,
                                                         gdr=str(gdrive))
                    for ex1 in listaf_scylla:
                        if i in ex1:
                            exportar_dados.append(ex1)
                            temp_scyla.append(ex1)
                    for item_lista in temp_scyla:
                        list_temporaria = item_lista.split(':')
                        dominio_vazado = list_temporaria[2]
                        scylla_dado_bruto(dominio_vazado, gdr=str(gdrive))
                else:
                    listaf_scylla = chamar_limpar_scylla(senha=i)
                    for ex1 in listaf_scylla:
                        if i in ex1:
                            exportar_dados.append(ex1)

        elif '00DMSTRx00' in i:
            i = i.replace(':00DMSTRx00', '')

#print(f'API --> {exportar_dados}')
#print(f'WORDLIST --> {exportar_dados_wl}')
#print(f'CW Pastebin --> {exportar_dados_pbdb}')
#print(f'Dorks --> {exportar_dados_dorks}')
#print(f'CVEs --> {exportar_dados_cves}')

if exportar_dados == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == ['None'] or exportar_dados_dorks == [None]:
    exportar_dados = []

if exportar_dados_wl == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == ['None'] or exportar_dados_dorks == [None]:
    exportar_dados_wl = []

if exportar_dados_pbdb == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == ['None'] or exportar_dados_dorks == [None]:
    exportar_dados_pbdb = []

if exportar_dados_dorks == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == ['None'] or exportar_dados_dorks == [None]:
    exportar_dados_dorks = []

if exportar_dados_cves == 'None' or exportar_dados_dorks == 'None ' or exportar_dados_dorks == ['None'] or exportar_dados_dorks == [None]:
    exportar_dados_cves = []

if exportar_dados or exportar_dados_wl or exportar_dados_pbdb or exportar_dados_dorks:
    if exportar_dados:
        gerar_resultados(nome='API_', conteudo=exportar_dados,
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
                         xsl_cript=str(xsl_cript),
                         db_f=str(db_f),
                         db_ocult=str(db_ocult),
                         db_cript=str(db_cript))

    if exportar_dados_wl:
        gerar_resultados(nome='WORDLIST_', conteudo=exportar_dados_wl, gdrive=str(gdrive),
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
                         xsl_cript=str(xsl_cript),
                         db_f=str(db_f),
                         db_ocult=str(db_ocult),
                         db_cript=str(db_cript))

    if exportar_dados_pbdb:
        gerar_resultados(nome='COMMONWEBSITES_', conteudo=exportar_dados_pbdb, gdrive=str(gdrive),
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
                         xsl_cript=str(xsl_cript),
                         db_f=str(db_f),
                         db_ocult=str(db_ocult),
                         db_cript=str(db_cript))

    if exportar_dados_dorks and exportar_dados_dorks != None and exportar_dados_dorks != 'None' and exportar_dados_dorks != ['None'] and exportar_dados_dorks != [None]:
        gerar_resultados(nome='DORKS_', conteudo=exportar_dados_dorks, gdrive=str(gdrive),
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
                         xsl_cript=str(xsl_cript),
                         db_f=str(db_f),
                         db_ocult=str(db_ocult),
                         db_cript=str(db_cript))

    enviar_email_oblivion()
    notificar_telegram()

#input('\nPress enter to exit...')
