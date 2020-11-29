import mimetypes
import smtplib
import pathlib
import time

import coloredlogs
import verboselogs
from email.message import EmailMessage
from email.utils import make_msgid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from etc.email.valor import *
from etc.serverx.config.config_server import *


path_atual_em = str(pathlib.Path(__file__).parent.absolute())
path_em = path_atual_em.replace('\\etc\\email', '')


def logando_email_image(tipo, mensagem):
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


def enviar_email_oblivion(server=False, status_nosafe=False, data_nosafe=None):
    """
    Sends the e-mail message/Envia o e-mail.

    :param server: Sets if is the Client user or the Server user/Define se é o servidor ou o cliente.
    :param status_nosafe: Sets if Oblivion will send the results in body of e-mail/Seta se o Oblivion vai envar os
    resultados no corpo do e-mail.
    :param data_nosafe: Data to send in e-mail body/Dados para enviar no corpo do e-mail.
    """
    with open(f'{path_em}/etc/email/emails.txt', 'r') as pegar_lista_emails:
        conteudo_lista_emails = pegar_lista_emails.read()
        conteudo_lista_emails = conteudo_lista_emails.replace(' ', '')
        conteudo_lista_emails = conteudo_lista_emails.split(';')

    for e in conteudo_lista_emails:
        time.sleep(1.4)

        if e != ';' and e != ' ' and e != '':
            msg = EmailMessage()
            msg['Subject'] = 'Oblivion - suas credenciais podem estar em risco!'
            msg['From'] = id_f1
            msg['To'] = e

            msg.set_content('This is a plain text body.')
            image_cid = make_msgid(domain='xyz.com')

            if status_nosafe == True:
                estrutura = data_nosafe

            else:
                with open(f'{path_em}/etc/email/body.html', 'r') as pegar_corpo:
                    estrutura = str(pegar_corpo.read())

            msg.add_alternative(f"""\
            {estrutura}
            """.format(image_cid=image_cid[1:-1]), subtype='html')

            with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                try:
                    smtp.ehlo()
                    smtp.starttls()

                    if server:
                        smtp.login(id_f1, id_f2)

                    else:
                        smtp.login(id_f3, id_f4)

                    smtp.send_message(msg)

                except Exception as e:
                    pass
