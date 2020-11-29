import winreg
import time
import requests
from pathlib import Path

import coloredlogs
import logging
import verboselogs


def logando_cves(tipo, mensagem):
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


def foo(hive, flag):
    """
    Creates a list with all softwares of computer/Cria uma lista com todos os programas do computador.
    """
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]
    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]

            except EnvironmentError:
                software['version'] = 'undefined'

            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]

            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)

        except EnvironmentError:
            continue

    return software_list


def verificar_programas (lista_programa, dadobruto=False):
    """
    Calls the Cirlc.lu API and compares with the list of softwares/Chama a API e compara com os programas do computador.

    :param lista_programa: List of softwares of computer/Lista dos programas do computador.
    :param dadobruto: Ignore
    """
    url = 'https://cve.circl.lu/api/last'
    header = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Accept': 'text/html, application/xhtml + xml, application/xml; q = 0.9, image/webp',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com/'
    }
    time.sleep(1.8)
    r = requests.get(url, headers=header)
    situation = str(r)

    if situation == '<Response [200]>':
        final_cve_json = r.json()
        lista_final_cves = []
        lista_tmp_cves = []
        lista_sistemas = ['versoes afetadas:']

        for i in final_cve_json:
            for e, x in i.items():

                if e == 'Published':
                    add = f'{e}: {x}'
                    lista_tmp_cves.append(add)

                elif e == 'id':
                    add = f'{e}: {x}'
                    lista_tmp_cves.append(add)

                elif e == 'vulnerable_configuration':
                    for k in x:
                        lista_sistemas.append(k)

                elif e == 'access':
                    add = f'{e}: {x}'
                    for kl, kk in x.items():
                        if kl == 'complexity':
                            final = f'{kl}: {kk}'
                            lista_tmp_cves.append(final)

                elif e == 'summary':
                    add = f'{e}: {x}'
                    lista_tmp_cves.append(add)
                    lista_final_cves.append(lista_tmp_cves)
                    lista_tmp_cves = []

        lista_unica = []
        for vulneravel in lista_sistemas:

            if not 'versoes afetadas' in vulneravel:
                vulneravel_lista = vulneravel.split(':')
                atual_cve = vulneravel_lista[4]

                if atual_cve not in lista_unica:
                    lista_unica.append(atual_cve)

        exp_cve = []

        for software in lista_programa:
            bloquear = ['(x64)', 'x64']
            verificar_programas = '%s' % (software['name'])
            verificar_programas = verificar_programas.lower()
            lista_tp = []
            for item in lista_unica:

                if item in verificar_programas:
                    p1 = (f'O aplicativo "{verificar_programas}" pode estar vulnerável à novas CVEs!')
                    exp_cve.append(f'{p1}\n\n')
                    for dados in lista_final_cves:
                        dados_tmp = str(dados)
                        dados_tmp = dados_tmp.lower()

                        if item in dados_tmp:
                            for dado_separar in dados:
                                p2 = (dado_separar)
                                exp_cve.append(f'{p2}\n')

                                if 'summary' in dado_separar:
                                    p3 = '\n'
                                    exp_cve.append(f'{p3}\n')

        return exp_cve

    else:
        logando_cves('warning', 'Was not possible to call Cirlc.lu API')
        exp_cve = []
        return exp_cve


def iniciar_analise_total_cves():
    """
    Calls the foo function, the verificar_programas function and return all software of computer that are includeD in
    some CVE/Chama a função foo, a função verificar_programas e retorna todos os software que estão contidos em alguma
    CVE.
    """
    software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)
    cvrt = verificar_programas(lista_programa=software_list)
    return cvrt
