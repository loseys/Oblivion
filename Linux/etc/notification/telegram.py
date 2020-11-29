#!/usr/bin/python

import pathlib
import requests
import smtplib
import logging

import coloredlogs
import verboselogs
from etc.api.keys import *


path_atual_tl = str(pathlib.Path(__file__).parent.absolute())
path_tl_final = path_atual_tl.replace('/etc/notification','')


def logando_notification(tipo, mensagem):
    """
    Generates the log message/Gera a mensagem de log.

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


def notificar_telegram(status_nosafe=False, data_nosafe=None):
    """
    Generates the notification to Telegram account/Gera a notificação para a conta do Telegram.
    """
    usuarios = []

    with open(f'{path_tl_final}/etc/notification/users.txt', 'r') as lista:
        separar = lista.readlines()

    if status_nosafe:
        mensagem = str(data_nosafe)

    else:
        with open(f'{path_tl_final}/etc/notification/message.txt', 'r') as mensagem_corpo:
            mensagem = str(mensagem_corpo.read())

    for i in separar:
        i = i.strip('\r')
        i = i.strip('\n')
        i = i.split(';')
        usuarios += i

    for i in usuarios:

        if i == '' or i == ' ':
            usuarios.remove(i)

    for mandar in usuarios:
        token = telegram_bot
        chat_id = mandar
        texto = mensagem
        #url_req = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
        send_message(chat_id=mandar, text=mensagem, token=telegram_bot)
        #results = requests.get(url_req)


def send_message(chat_id, text=None, parse_mode = 'Markdown', token=None):
    """
    Sends message in bold mode/Enviar mensagem em negrito.

    :param chat_id: ID of Telegram account/ID da conta Telgram.
    :param text: Message/Mensagem.
    :param parse_mode: Ignore.
    :param token: ID Telegram bot/ID do bot Telegram.
    """
    URL = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    answer = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
    r = requests.post(URL, json=answer)

    if (text == '/bold'):
        send_message(chat_id, 'Here comes the'+'*'+'bold'+'*'+'text!')
