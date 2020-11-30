#!/usr/bin/python

import datetime
import requests
import pathlib
import json
import time
import random
import os
import getpass
from pathlib import Path

import coloredlogs
import urllib3
import logging
import verboselogs
from etc.api.googledrv.gdrive_folder import *


# Global variables/Variáveis globais.
path_central_scylla = str(pathlib.Path(__file__).parent.absolute())
path_scylla_f = path_central_scylla.replace('/etc/api', '')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
definir = os.environ

for valor, item in definir.items():

    if valor == 'APPDATA':
        lista_item = item.split('\\')
        usuario = lista_item[2]

usuario = getpass.getuser()
documentos = f'/home/{usuario}/Documents'

with open(f'{path_scylla_f}/etc/api/googledrv/id_folder.txt', 'r') as id_f:
    id_gdr = id_f.read()


def logando_scylla(tipo, mensagem):
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


def scylla_dado_bruto(nome, gdr=None):
    """
    Saves the raw file of data leak/Salva o dado bruto do vazamento de dados.

    :param nome: Name/Nome
    :param gdr: Uploads to Google Drive/Sobe arquivo para o Google Drive.
    """
    hashscy = random.getrandbits(64)

    with open(f'{path_scylla_f}/etc/api/googledrv/id_folder.txt', 'r') as pegar_id_pasta:
        id_pasta = str(pegar_id_pasta.read())

    Path(f'/home/{usuario}/Documents/Oblivion').mkdir(parents=True, exist_ok=True)

    with open(f'{documentos}/Oblivion/RAW_scylla_{nome}_{hashscy}.txt', 'w+') as arquivo_scylla:
        time.sleep(1.8)
        header = {
            'Accept': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }

        url = 'https://scylla.sh/search?q=domain:Collection1-btc-combo&size=5000&start=5000'
        scy_dadob = requests.get(url, headers=header, verify=False)
        scy_js = scy_dadob.json()
        contador = 0
        transportar = []
        final_tr = []
        for js_r in scy_js:
            for content_r in js_r['fields'].items():

                if contador == 3:
                    contador = 0

                if contador == 0:
                    transportar.clear()

                if 'domain' in content_r:
                    transportar.append(content_r[1])
                    contador += 1
                if 'email' in content_r:
                    transportar.append(content_r[1])
                    contador += 1
                if 'password' in content_r:
                    transportar.append(content_r[1])
                    contador += 1

            try:
                mover_tr = f'{transportar[1]}:{transportar[2]}:{transportar[0]}'
                arquivo_scylla.write(f'{mover_tr}\n')

            except:
                pass

            final_tr += transportar

    if gdr == 'PySide2.QtCore.Qt.CheckState.Checked':
        subir_arquivo_drive_raiz(id_pasta,
                                 f'RAW_scylla_{nome}_{hashscy}.txt',
                                 'text/plain',
                                 f'{documentos}/Oblivion/RAW_scylla_{nome}_{hashscy}.txt')


def limpar_scylla(data, dadobruto_pegar):
    """
    Organizes the data/Organiza os dados.

    :param data: List of data content/Lista contendo os dados.
    :param dadobruto_pegar: To save the raw data/Para salvar o dado bruto.
    """
    scylla_final = []
    scylla_lista = []
    lista_domain = []
    for fields in data:
        for valor, item in fields['fields'].items():

            if valor == 'email':
                scylla_final.insert(0, item)

            if valor == 'password':
                scylla_final.insert(1, item)

            if valor == 'domain':
                scylla_final.insert(2, item)
                lista_domain.append(valor)
                scylla_final.append('None')

        adicionar_pontos = (':'.join(scylla_final))
        scylla_lista.append(adicionar_pontos)
        scylla_final = []

    return scylla_lista


def chamar_limpar_scylla(email=None, senha=None, dadobruto=False, gdr=None):
    """
    Calls the Scylla API/Chama a API da Scylla.

    :param email: E-mail.
    :param senha: Password/Senha.
    :param dadobruto: To save the raw data/Para salvar o dado bruto.
    :param gdr: Uploads to Google Drive/Sobe arquivo para o Google Drive.
    """
    cls_scylla_final = []
    gdrs = gdr
    url_email = "https://scylla.sh/search?q=email%3Ainput"
    url_senha = "https://scylla.sh/search?q=password%3Ainput"

    header = {
        'Accept': 'application/json',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }

    if email != None and senha != None:
        url_email = url_email.replace('input', email)
        url_senha = url_senha.replace('input', senha)
        r_email = requests.get(url_email, headers=header, verify=False)
        time.sleep(1)
        r_senha = requests.get(url_senha, headers=header, verify=False)
        time.sleep(1)
        data_email = r_email.json()
        data_senha = r_senha.json()
        limpar_scylla(data_email)
        limpar_scylla(data_senha)
        lista_scylimp = (limpar_scylla(data_email,dadobruto_pegar=dadobruto))
        return lista_scylimp

    elif email != None and senha == None:
        try:
            url_email = url_email.replace('input', email)
            time.sleep(1.8)
            r_email = requests.get(url_email, headers=header, verify=False)
            data_email = r_email.json()
            #limpar_scylla(data_email)

            lista_scylimp = (limpar_scylla(data_email, dadobruto_pegar=dadobruto))
            return lista_scylimp

        except:
            logando_scylla('error', 'Was not possible to call Scylla API')


    elif senha != None and email == None:
        try:
            url_senha = url_senha.replace('input', senha)
            time.sleep(1.8)
            r_senha = requests.get(url_senha, headers=header, verify=False)
            time.sleep(1)
            data_senha = r_senha.json()
            lista_scylimp = (limpar_scylla(data_senha, dadobruto_pegar=dadobruto))
            return lista_scylimp

        except:
            logando_scylla('error', 'Was not possible to call Scylla API')
