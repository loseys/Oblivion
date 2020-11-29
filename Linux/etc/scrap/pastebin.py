#!/usr/bin/python

import urllib.request
import requests
import random
import pathlib
import time
import datetime
import logging
import getpass
from pathlib import Path

import coloredlogs
import verboselogs
from bs4 import BeautifulSoup
from etc.api.googledrv.gdrive_folder import *


# Global variables/Variáveis globais.
path_f = str(pathlib.Path(__file__).parent.absolute())
path_f = path_f.replace('/etc/scrap','')

data_atual = datetime.date.today()
definir = os.environ

for valor, item in definir.items():

    if valor == 'APPDATA':
        lista_item = item.split('\\')
        usuario = lista_item[2]

usuario = getpass.getuser()
documentos = f'/home/{usuario}/Documents'

with open(f'{path_f}/etc/api/googledrv/id_folder.txt', 'r') as id_f:
    id_gdr = id_f.read()


def logando_pastebin(tipo, mensagem):
    """
    Generates the log message/Gera a mensagem de log.

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


def verificar_ultimos_pb(credencial, dadobruto=False, gdr=None):
    """
    Checks the last public pastes on Pastebin/Checa os últimos pastes no Pastebin.

    :param termo: Password, e-mail or document.
    :param dadobruto: To save the raw data/Para salvar o dado bruto.
    :param gdr: Uploads to Google Drive/Sobe arquivo para o Google Drive.
    """
    header = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Accept': 'text/html, application/xhtml + xml, application/xml; q = 0.9, image/webp',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com/'
    }

    url = 'https://pastebin.com/archive'
    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    links = []

    for a in soup.find_all('a', href=True):

        if a.text:
            links.append(a['href'])

    for i in links:

        if len(i) == 9:
            link_final = f'https://pastebin.com/raw{i}'
            sleep_numero = random.uniform(0, 8)
            time.sleep(sleep_numero)
            leak_pastb = requests.get(link_final, headers=header)
            conteudo_pb = leak_pastb.text
            conteudo_pb = str(conteudo_pb)
            conteudo_lista = conteudo_pb.split('\n')

            if credencial in conteudo_pb:

                if dadobruto == True:
                    ii = i.replace('/','')
                    Path(f'/home/{usuario}/Documents/Oblivion').mkdir(parents=True, exist_ok=True)
                    with open(f'{documentos}/Oblivion/RAW_pastebin_{ii}.txt', 'w', encoding='utf-16') as file_db:
                        conteudo_pb = conteudo_pb #.encode('utf-16')
                        conteudo_pb = str(conteudo_pb)

                        file_db.write(conteudo_pb)

                    if gdr == 'PySide2.QtCore.Qt.CheckState.Checked':
                        subir_arquivo_drive_raiz(id_gdr,
                                                 f'RAW_pastebin_{ii}.txt',
                                                 'text/plain',
                                                 f'{documentos}/Oblivion/RAW_pastebin_{ii}.txt')

                for i in conteudo_lista:

                    if credencial in i:
                        final_pbk = f'{i}:{link_final}'
                        final_pbk = final_pbk.strip('\r')
                        final_pbk = final_pbk.strip('\n')
                        final_pbk = final_pbk.strip('\f')
                        final_pbk = final_pbk.replace('\r', '')
                        final_pbk = final_pbk.replace('\n', '')
                        final_pbk = final_pbk.replace('\f', '')
                        final_pbk = final_pbk.replace('\\r', '')
                        final_pbk = final_pbk.replace('\\n', '')
                        final_pbk = final_pbk.replace('\\f', '')

                        return final_pbk
