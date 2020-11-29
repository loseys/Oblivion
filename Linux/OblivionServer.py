#!/usr/bin/python

import coloredlogs
import verboselogs
import datetime
import logging
import pathlib
import os.path
import logging
import pathlib
import re

from flask import Flask, request, redirect, url_for
from flask_restful import Resource, Api
from flask import render_template
from sqlalchemy import create_engine
from pathlib import Path
from etc.email.send_email import *
from etc.api.scylla import *
from etc.api.intelxapi import *
from etc.api.intelligencex import *
from etc.api.hibpwned import *
from etc.scrap.wordlists_search import *
from etc.scrap.pastebin import *
from etc.scrap.google_dorks import *
from etc.create import *
from etc.notification.telegram import *
from etc.serverx.config.attributes import *
from etc.serverx.config.config_server import *
from etc.serverx.system.windows.applicate import *


# Global variables/Variáveis globais.
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app = Flask(__name__)
api = Api(app)

path_atual_server = str(pathlib.Path(__file__).parent.absolute())
path_server = path_atual_server.replace('\\etc\\serverx','')


def logando_server(tipo, mensagem):
    """
    :param tipo: Set the log type/Irá setar o tipo de log.
    :param mensagem: Set the message of log/Irá setar a mensagem do log.
    :return: Return the complete log's body/Irá retornar o corpo completo do log.
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


print("Oblivion [version 1.0.0]", "Copyright (c) 2020, Loseys - BSD License.", sep='\n');
print(r'''
   ___ _     _ _       _             
  /___\ |__ | (_)_   _(_) ___  _ __  
 //  // '_ \| | \ \ / / |/ _ \| '_ \ 
/ \_//| |_) | | |\ V /| | (_) | | | |
\___/ |_.__/|_|_| \_/ |_|\___/|_| |_|                                    
''')





logando_server('verbose', 'Starting server')

# Gets the security keys/Pega as chaves de segurança.
with open(f'{path_server}/etc/serverx/config/keys.txt', 'r') as ler_keys:
    cont_keys = ler_keys.read()
    cont_keys = cont_keys.split('\n')
    sec_keys = []
    for e in cont_keys:
        if e != '' and e != ' ':
            sec_keys.append(e)


def gerar_log():
    """
    Writes the log files/Escreve os arquivos de log.
    """
    arquivo = Path(f'{path_server}/etc/serverx/logs/{datetime.date.today().strftime("%d-%m-%Y")}.txt')
    if os.path.exists(arquivo):
        with open(f'{path_server}/etc/serverx/logs/{datetime.date.today().strftime("%d-%m-%Y")}.txt', 'a') as acessos:
            acessos.write(f'{datetime.datetime.now()} - {request.headers["Host"]} {request.headers["User-Agent"]}\n')
    else:
        with open(f'{path_server}/etc/serverx/logs/{datetime.date.today().strftime("%d-%m-%Y")}.txt', 'w') as acessos:
            acessos.write(f'{datetime.datetime.now()} - {request.headers["Host"]} {request.headers["User-Agent"]}\n')


@app.route("/oblivion")
def index():
    """
    Shows the initial interface on x:x/oblivion
    """
    gerar_log()
    return render_template('index.html')


class validar(Resource):
    def get(self, key, parametros):
        gerar_log()
        sessao = False
        sessao_api = False
        header_c = str(request.headers)

        # validando requisição por url
        for e in sec_keys:
            if str(e) in str(key):
                sessao = True

        # validando requisição por request
        if 'Key' in header_c:
            key = request.headers['Key']
            for e in sec_keys:
                if e == request.headers['Key']:
                    sessao_api = True

        if sessao or sessao_api:
            if sessao:
                atributos = separar_atributos(parametros)
                #return atributos

                if atributos == []:
                    mensagem_error = "{'error':'invalid arguments'}"
                    return mensagem_error

            else:
                atributos = separar_atributos_headers(request.headers)
                #return atributos

                if atributos == []:
                    mensagem_error = "{'error':'invalid arguments'}"
                    return mensagem_error

            data_usuario = self.db_data_user();os_system = 'windows'

            #### scan aqui ####

            if os_system == 'windows':
                if '&EM' in parametros or '&PW' in parametros or '&DM' in parametros:
                    result = re.search('"(.*)"', parametros)
                    parametro_cred = result.group(1)
                    if '&EM' in parametros:
                        parametro_cred_list = []
                        parametro_cred_list.append(f'{parametro_cred}:00EMSTRx00')

                    if '&PW' in parametros:
                        parametro_cred_list = []
                        parametro_cred_list.append(f'{parametro_cred}:00SHSTRx00')

                    if '&DM' in parametros:
                        parametro_cred_list = []
                        parametro_cred_list.append(f'{parametro_cred}:00DMSTRx00')

                    if 'loop' in parametros:
                        #print('em loop')
                        iniciar_scan = srv_aplicar_separar(parametro_cred_list, atributos, loop_scan=True, key=key)

                        if api_return:
                            return iniciar_scan

                    else:
                        #print('nao em loop')
                        iniciar_scan = srv_aplicar_separar(parametro_cred_list, atributos, key=key)

                        if api_return:
                            return iniciar_scan

                elif '&Em' in str(request.headers) or '&Pw' in str(request.headers) or '&Dm' in str(request.headers):
                    #print(request.headers)
                    result = re.search('{(.*)}', str(request.headers))
                    parametro_cred = result.group(1)
                    if '&Em' in str(request.headers):
                        parametro_cred_list = []
                        parametro_cred_list.append(f'{parametro_cred}:00EMSTRx00')
                    if '&Pw' in str(request.headers):
                        parametro_cred_list = []
                        parametro_cred_list.append(f'{parametro_cred}:00SHSTRx00')
                    if '&Dm' in str(request.headers):
                        parametro_cred_list = []
                        parametro_cred_list.append(f'{parametro_cred}:00DMSTRx00')

                    if 'loop' in atributos:
                        #print('em loop')
                        iniciar_scan = srv_aplicar_separar(parametro_cred_list, atributos, loop_scan=True, key=key)

                        if api_return:
                            return iniciar_scan

                    else:
                        #print('nao em loop')
                        iniciar_scan = srv_aplicar_separar(parametro_cred_list, atributos, key=key)

                        if api_return:
                            return iniciar_scan

                else:
                    if 'loop' in atributos:
                        #print('loop com else')
                        iniciar_scan = srv_aplicar_separar(data_usuario, atributos, loop_scan=True, key=key)

                        if api_return:
                            return iniciar_scan

                    else:
                        #print('sem loop else')
                        iniciar_scan = srv_aplicar_separar(data_usuario, atributos, key=key)

                        if api_return:
                            return iniciar_scan

            elif os_system == 'linux':
                pass

            else:
                mensagem_error = "{'error':'bad server config'}"
                return mensagem_error

        # mensagem de erro para url sem key ou header sem parametro key
        else:
            mensagem_error = "{'error':'invalid key'}"
            return mensagem_error

    def db_data_user(self):
        db_connect = create_engine(f'sqlite:///{path_server}/{db_name_f}')
        id_items2 = []
        conn = db_connect.connect()

        try:
            query = conn.execute("select email from data")
            # id1 = ([i[0] for i in query.cursor.fetchall()])

            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00SHSTRx00'
                id_items2.append(ii)
        except:
            pass

        try:
            query = conn.execute("select senha from data")
            # id1 = ([i[0] for i in query.cursor.fetchall()])

            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00EMSTRx00'
                id_items2.append(ii)
        except:
            pass

        try:
            query = conn.execute("select documento from data")
            # id1 = ([i[0] for i in query.cursor.fetchall()])

            for i in query.cursor.fetchall():
                ii = str(i[0])
                ii += ':00DMSTRx00'
                id_items2.append(ii)
        except:
            pass

        arrumar_id_items2 = []
        for ef in id_items2:
            if not 'None:' in ef and ef != '' and not ' ' in ef and ':' in ef:
                arrumar_id_items2.append(ef)

        return arrumar_id_items2


api.add_resource(validar, f'/oblivion/<key>/<parametros>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5001")
