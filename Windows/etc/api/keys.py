import pathlib
import coloredlogs
import logging
import verboselogs


path_central_key = str(pathlib.Path(__file__).parent.absolute())
path_central_keyf = path_central_key.replace('\\etc\\api', '')


def logando_keys(tipo, mensagem):
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


with open(f'{path_central_keyf}/etc/api/keys_db.txt', 'r') as pegar_keys:
    conteudo_keys = pegar_keys.read().split('\n')
    for e in conteudo_keys:

        if 'intelligencex_key' in e:
            e = e.split(' ')
            intelligencex_key = str(e[2].replace("'",''))

        if 'haveibeenpwned_key' in e:
            e = e.split(' ')
            haveibeenpwned_key = str(e[2].replace("'",''))

        if 'telegram_bot' in e:
            e = e.split(' ')
            telegram_bot = str(e[2].replace("'",''))
