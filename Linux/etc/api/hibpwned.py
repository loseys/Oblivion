#!/usr/bin/python

import requests
import time
import logging

import coloredlogs
import verboselogs
from etc.api.keys import *


# Global variables/Variáveis globais.
headers = {}
headers['content-type'] = 'application/json'
headers['api-version'] = '3'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
headers['hibp-api-key'] = haveibeenpwned_key


def logando_hibpwned(tipo, mensagem):
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


def check_breach(eml):
    """
    Calls the Have I Been Pwned API.
    :param eml: Heres come the password or e-email.
    """
    time.sleep(1.2)
    url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+eml+'?truncateResponse=false'
    r = requests.get(url, headers=headers)
    situation = str(r)
    pwd_lista = []

    if situation == '<Response [200]>':
        data = r.json()
        for list_pwd in data:
            for item_pwd, value_pwd in list_pwd.items():

                if item_pwd == 'Title':
                    t1d = value_pwd

                if item_pwd == 'BreachDate':
                    d1d = value_pwd

            atual_pwd = f'{eml}:None:{t1d}:{d1d}'
            pwd_lista.append(atual_pwd)

    else:
        logando_hibpwned('warning','Was not possible to call Have I Been Pwned API')

    return pwd_lista
