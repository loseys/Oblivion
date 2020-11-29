import requests
import time
import random
import pathlib
import datetime
import logging
import getpass
from pathlib import Path

import coloredlogs
import verboselogs
from urlextract import URLExtract
from bs4 import BeautifulSoup
from etc.api.googledrv.gdrive_folder import *


# Global variables/Variáveis globais.
path_gd = str(pathlib.Path(__file__).parent.absolute())
path_gdf = path_gd.replace('\etc\scrap','')

data_atual = datetime.date.today()
definir = os.environ


with open(f'{path_gdf}/etc/api/googledrv/id_folder.txt', 'r') as id_f:
    id_gdr = id_f.read()


for valor, item in definir.items():

    if valor == 'APPDATA':
        lista_item = item.split('\\')
        usuario = lista_item[2]

documentos = f'C:/Users/{usuario}/Documents'


def logando_google_dorks(tipo, mensagem):
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


def google_scrap(termo, dadobruto=False, gdr=None):
    """
    Performs Scrap in the Google search website/Realiza Scrap no Google Search.


    :param credencial: Password, e-mail or document/Senha, e-mail ou documento.
    :param dadobruto: To save the raw data/Para salvar o dado bruto.
    :param gdr: Uploads to Google Drive/Sobe arquivo para o Google Drive.
    """
    block = ['https://pastebin.com']
    final_urls = []
    urls = []
    clean = []
    vazou = []
    vazio = []

    google_urls = [
        'https://www.google.com/search?q=site:pastebin.com+intext:leak&sxsrf=ALeKk03cedAQ3Y7jlzXHY8LImOO_gJGxMQ:1606136317667&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwjcobOF3JjtAhWbF7kGHbo3BO4QpwV6BAgFECY&biw=1366&bih=629',
        'https://www.google.com/search?biw=1366&bih=629&tbs=qdr%3Ad&sxsrf=ALeKk02AVQ6YXyUuLeavYsIZjr__SUBBKQ%3A1606136641749&ei=QbO7X5eGLaLD5OUP7dCoqAU&q=site%3Apastebin.com+intext%3A*%3A*&oq=site%3Apastebin.com+intext%3A*%3A*&gs_lcp=CgZwc3ktYWIQA1C3kgJY9KMCYN6nAmgAcAB4AIABVogBhwWSAQE4mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwjXqvef3ZjtAhWiIbkGHW0oClUQ4dUDCA0&uact=5',
        'https://www.google.com/search?biw=1366&bih=629&tbs=qdr%3Ad&sxsrf=ALeKk008FbvhwTD4Qyhal8ibZGTuwj5DwQ%3A1606136886229&ei=NrS7X7-_DYHX5OUPpMaYqAg&q=site%3Apastebin.com+intext%3A%22Target%3A%22&oq=site%3Apastebin.com+intext%3A%22Target%3A%22&gs_lcp=CgZwc3ktYWIQA1DEG1iMMWCSNGgAcAB4AIABWYgBnQOSAQE1mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwi_ssGU3pjtAhWBK7kGHSQjBoUQ4dUDCA0&uact=5',
        'https://www.google.com/search?biw=1366&bih=629&tbs=qdr%3Ad&sxsrf=ALeKk01een-cvWz4vY0qsb4w_IbGk4Ym0w%3A1606136893453&ei=PbS7X9f6GoDC5OUP7amBiA0&q=site%3Apastebin.com+intext%3Apassword&oq=site%3Apastebin.com+intext%3Apassword&gs_lcp=CgZwc3ktYWIQA1DlF1ivIGCNIWgAcAB4AIABZ4gB9gWSAQM4LjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwiXjfqX3pjtAhUAIbkGHe1UANEQ4dUDCA0&uact=5',
        'https://www.google.com/search?biw=1366&bih=629&tbs=qdr%3Ad&sxsrf=ALeKk01EHsZ3TIvfjuSTMJN4z9lThqH_AA%3A1606136962270&ei=grS7X5P8D4Cg5OUPlP6QyAU&q=site%3Apastebin.com+intext%3Aemail&oq=site%3Apastebin.com+intext%3Aemail&gs_lcp=CgZwc3ktYWIQA1DD3ANY3_wDYMr-A2gBcAB4AIABX4gB2QmSAQIxNZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwiTxeK43pjtAhUAELkGHRQ_BFkQ4dUDCA0&uact=5'
    ]

    header = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Accept': 'text/html, application/xhtml + xml, application/xml; q = 0.9, image/webp',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com/'
    }

    for open_urls in google_urls:
        sleep_tempo = random.uniform(0, 6)
        r = requests.get(open_urls, headers=header)
        sites = r.text
        extractor = URLExtract()
        urls = extractor.find_urls(sites)

        for content in urls:

            if "google" not in content:

                if "http" in content:

                    if content not in block:
                        final_urls.append(content)

        sleep_numero = random.uniform(0, 8)
        time.sleep(sleep_numero)

    for rep in final_urls:

        if '&amp' in rep:
            rep = rep.replace('&amp', '')
            clean.append(rep)

    for search in clean:
        url = search
        sleep_tempo = random.uniform(0, 6)

        if 'pastebin' in search:
            alterar_string = search[-8:]
            reponse_gk = requests.get(search, headers=header)
            vazamento_gd = reponse_gk.text
            html = BeautifulSoup(reponse_gk.text, 'html.parser')

            if termo in vazamento_gd:

                if dadobruto == True:
                    alt_string = alterar_string.replace('/','')

                    Path(f'C:/Users/{getpass.getuser()}/Documents/Oblivion').mkdir(parents=True, exist_ok=True)
                    with open (f'{documentos}/Oblivion/RAW_pastebin_{alt_string}.txt','w', encoding='utf-16') as file_gd:
                        for content in html.select('.li1'):
                            leak = content.select_one('.de1')
                            lk = leak.text
                            file_gd.write(lk)

                    if gdr == 'PySide2.QtCore.Qt.CheckState.Checked':
                        subir_arquivo_drive_raiz(id_gdr,
                                                 f'RAW_pastebin_{alt_string}.txt',
                                                 'text/plain',
                                                 f'{documentos}/Oblivion/RAW_pastebin_{alt_string}.txt')

                lista_temp_gd = vazamento_gd.split('\n')
                for i in lista_temp_gd:

                    if termo in i:
                        alt_string = alterar_string.replace('/', '')
                        termo_novo = f'{termo}:pastebin.com/{alt_string}'
                        return termo_novo
