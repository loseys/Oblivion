import os
import re
import datetime
import pprint
import requests
import pathlib
import random
import getpass
from pathlib import Path

import coloredlogs
import logging
import verboselogs
from etc.api.intelxapi import *
from etc.api.keys import *
from etc.api.googledrv.gdrive_folder import subir_arquivo_drive_raiz


# Global variables/Variáveis globais.
path_atual_i = str(pathlib.Path(__file__).parent.absolute())
path_i_data = path_atual_i.replace('\\etc\\api','')

API_ROOT = 'https://2.intelx.io'
API_KEY  = intelligencex_key
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'

definir = os.environ

for valor, item in definir.items():

    if valor == 'APPDATA':
        lista_item = item.split('\\')
        usuario = lista_item[2]

documentos = f'C:/Users/{usuario}/Documents'

with open(f'{path_i_data}/etc/api/googledrv/id_folder.txt', 'r') as id_f:
    id_gdr = id_f.read()


def logando_intelligencex(tipo, mensagem):
    """
    Generates the log message.

    :param tipo: Set the log type/Seta o tipo de log
    :param mensagem: Set the message of log/Seta a mensagem do log
    :return: Return the complete log's body/Retorna o corpo completo do log
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


def intelligencex_info_leak(termo):
    """
    Searches if the data is included in some data leak/Pesquisa se os dados estão contidos em algum vazamento de dados.

    :param termo: Here come the password, e-mail or document/Aqui vai a senha, e-mail ou documento.
    """
    API_ROOT = 'https://2.intelx.io'
    API_KEY = intelligencex_key
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    sid_raw_final = []
    api_int = intelx(key=API_KEY)
    valor_sid = api_int.search(term=termo)


def intelligencex_download_raw(id, type=0, bucket=""):
    """
    Downloads the raw of data leak/Baixa os dados brutos do data leak.
    """
    h = {'x-key': API_KEY, 'User-Agent': USER_AGENT}
    r = requests.get(f"{API_ROOT}/file/read?type={type}&systemid={id}&bucket={bucket}", headers=h, stream=True)


def intelligencex_pegar_sid():
    """
    Gets the SID of the data leak/Pega o SID do vazamento de dados.

    NOTE: SID is a identify number of the data leak/SID é um número de identificação do vazamento de dados.
    """
    for i in id.values():
        for pegar_sid in i:
            for xfp1, xfp2 in pegar_sid.items():

                if xfp1 == 'systemid':
                #or xfp1 == 'date' or xfp1 == 'name':
                    print(xfp2)


def caracter_win(arquivo_w):
    """
    Clears the bad characters of the data leak file/Limpa alguns caractéres do arquivo do vazamento de dados que poderão
    gerar alguns erros.

    :param arquivo_w: Path file/Local do arquivo
    :return: Returns the "cleaned" file/Retorna o arquivo "limpo".
    """
    arquivo_w = str(arquivo_w)
    arquivo_w = arquivo_w.strip()
    arquivo_w = arquivo_w.rstrip()
    arquivo_w = arquivo_w.replace('\\','')
    arquivo_w = arquivo_w.replace('\r','')
    arquivo_w = arquivo_w.replace('\n','')
    arquivo_w = arquivo_w.replace('/', '')
    arquivo_w = arquivo_w.replace('//', '')
    letras_numeros = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'x', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                      'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                      '9', '0', ' ']
    for i in arquivo_w:

        if i not in letras_numeros:
            arquivo_w = arquivo_w.replace(i, '')

    return arquivo_w


def intelligencex_sid_raw(termo, conteudobruto=False, gdr=None):
    """
    Gets the data leak and save it/Obtem o vazamento de dados e o salva.

    :param termo: Files types/Tipos de arquivos.
    :param conteudobruto: Saves the raw file/Salvar o dado bruto.
    :param gdr: Uploads to Google Drive/Sobe arquivo para o Google Drive.
    """
    lista_intelligencex_trash = []
    lista_intelligencex = []
    sid_raw_final = []
    api_int = intelx(key=API_KEY)
    valor_sid = api_int.search(term=termo)

    for i in valor_sid.values():
        time.sleep(3.2)
        for pegar_sid in i:
            hash = random.getrandbits(64)
            for xfp1, xfp2 in pegar_sid.items():

                if xfp1 == 'date':
                    in_data = xfp2
            for xfp1, xfp2 in pegar_sid.items():

                if xfp1 == 'name':
                    in_name = xfp2
            for xfp1, xfp2 in pegar_sid.items():

                if xfp1 == 'systemid':
                    in_sid = xfp2

            time.sleep(3.2)
            type = 0
            bucket = ""
            h = {'x-key': API_KEY, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
            r = requests.get(f"{API_ROOT}/file/read?type={type}&systemid={in_sid}&bucket={bucket}", headers=h,
                             stream=True)

            situation = str(r)

            if situation == '<Response [200]>':
                st_in_name = caracter_win(in_name)
                st_in_data = str(in_data)
                st_in_data = st_in_data.replace(":", "_")
                st_in_data = st_in_data.replace(" ", "_")
                nomeArquivoFinal = 'Intelligencex'
                nomeArquivoFinal += st_in_data

                if conteudobruto == True:
                    Path(f'C:/Users/{getpass.getuser()}/Documents/Oblivion').mkdir(parents=True, exist_ok=True)
                    with open(f"{documentos}/Oblivion/RAW_intelx_{st_in_name}.txt", "wb") as f:
                        st_in_data = in_data + ' - ' + in_name + '\n'
                        st_in_data_b = str.encode(st_in_data)
                        f.write(st_in_data_b)
                        f.write(r.content)
                        f.close()

                    if gdr == 'PySide2.QtCore.Qt.CheckState.Checked':
                        subir_arquivo_drive_raiz(id_gdr,
                                                 f"RAW_intelx_{st_in_name}.txt",
                                                 'text/plain',
                                                 f"{documentos}/Oblivion/RAW_intelx_{st_in_name}.txt")

                final_raw = r.text
                final_raw = str(final_raw)
                sid_raw_final = final_raw.split('\n')
                for contend_data in sid_raw_final:

                    if termo in contend_data:
                        contend_data = str(contend_data)
                        contend_data = contend_data.replace('\r', ' ')
                        contend_data = contend_data.replace('\r', ' ')
                        contend_data = contend_data.replace('\t', ' ')
                        contend_data = contend_data.replace('\n', ' ')
                        contend_data = contend_data.replace('\\N', ' ')
                        contend_data = contend_data.replace('\\', ' ')
                        contend_data = contend_data.replace('\\\\', ' ')

                        contend_data = contend_data.replace('		', ' ')
                        contend_data = contend_data.replace('	    ', ' ')
                        contend_data = contend_data.replace('	   ', ' ')
                        contend_data = contend_data.replace('	  ', ' ')
                        contend_data = contend_data.replace('	 ', ' ')
                        contend_data = contend_data.replace('   ', ' ')
                        contend_data = contend_data.replace('  ', ' ')
                        contend_data = ("	".join(contend_data.split()))
                        contend_data = contend_data.replace('	', ' ')
                        contend_data = (" ".join(contend_data.split()))
                        contend_data = contend_data.replace(' ', ':')
                        in_name = in_name.replace(':','_')
                        in_data = in_data.replace(':','_')
                        final_data_int = f'{contend_data}:{in_name}:{in_data}'
                        final_data_int = final_data_int.rstrip()
                        final_data_int = final_data_int.strip()
                        final_data_int = final_data_int.replace('\r', '')
                        final_data_int = final_data_int.replace('\r','')
                        final_data_int = final_data_int.replace('\t', '')
                        final_data_int = final_data_int.replace('\n', '')
                        final_data_int = final_data_int.replace('\\N', '')
                        final_data_int = final_data_int.replace('\\', '')
                        final_data_int = final_data_int.replace('\\\\', '')
                        lista_intelligencex_trash.append(final_data_int)

            else:
                logando_intelligencex('warning','Was not possible to call IntelligenceX API')

    return lista_intelligencex_trash
