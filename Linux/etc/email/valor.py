#!/usr/bin/python

import smtplib
import logging
import pathlib
import base64

import coloredlogs
import verboselogs


# Global variables/Variáveis globais.
path_atual_vl= str(pathlib.Path(__file__).parent.absolute())
path_vl = path_atual_vl.replace('/etc/email','')


def logando_valor(tipo, mensagem):
    """
    :param tipo: Sets the log type/Seta o tipo de log.
    :param mensagem: Sets the message of log/Seta a mensagem do log.
    :return: Returns the complete log's body/Retorna o corpo completo do log.
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


with open(f'{path_vl}/etc/email/parameters.txt', 'r') as id_crd:
    valores_id = id_crd.read()
    valores_id = valores_id.split('\n')

    for e in valores_id:

        if 'id_1' in e:
            e = e.split(':')
            id_f1 = str(e[1])

        if 'id_2' in e:
            e = e.split(':')
            id_f2 = str(e[1])


# Decode the e-mail and password of e-mail account/Decodifica o e-mail e a senha da conta de e-mail.
id_f1 = str(id_f1)
id_f2 = str(id_f2)

try:
    id_f1 = (base64.b32decode(bytearray(id_f1, 'ascii')).decode('utf-8'))
    id_f2 = (base64.b32decode(bytearray(id_f2, 'ascii')).decode('utf-8'))

except:
    pass
