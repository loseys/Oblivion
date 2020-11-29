#!/usr/bin/python

import requests
import datetime
import random
import time
import logging

import coloredlogs
import verboselogs
from etc.scrap.db_wordlist import lista_wordlists


def logando_wordlist(tipo, mensagem):
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


def verificar_dados(credencial):
    """
    Checks the list of wordlists in "db_wordlist.py"/Checa a lista de word lists no "db_wordlist.py".

    :param credencial: Password, e-mail or document/Senha, e-mail ou documento.
    """
    lista_wordlists_final = []

    for dados_wl in lista_wordlists:
        definir = random.uniform(0, 5)
        temporizador = definir
        try:
            header = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
                'Accept': 'text/html, application/xhtml + xml, application/xml; q = 0.9, image/webp',
                'Accept-Encoding': 'gzip',
                'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
                'Upgrade-Insecure-Requests': '1',
                'Referer': 'https://www.google.com/'
            }
            time.sleep(temporizador)
            verificar_wl = requests.get(dados_wl, headers=header)
            vazou_wl = verificar_wl.text
            separar_wl = dados_wl.split('/')
            wordlist_atual = separar_wl[-1]

            if credencial in vazou_wl:
                aplicar = f'{None}:{credencial}:{separar_wl[-1]}:None'
                lista_wordlists_final.append(aplicar)

        except:
            logando_wordlist('warning','Was not possible to access the word list database in GitHub repository')

    return lista_wordlists_final
