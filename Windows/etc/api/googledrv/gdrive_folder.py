import os
import pickle
import pathlib
import logging

import coloredlogs
import verboselogs
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


# Global variables/Variáveis globais.
path_atual_gj2 = str(pathlib.Path(__file__).parent.absolute())
path_gj2_data = path_atual_gj2.replace('\\etc\\api\\googledrv','')

CLIENT_SECRET_FILE = f'{path_gj2_data}\client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']


def logando_gdrive_f(tipo, mensagem):
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


def criar_pasta_drive():
    """
    Creates a new folder in Google Drive/Cria uma nova pasta no Google Drive.
    """
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    national_parks = ['aaa1', 'bbb1', 'ccc1']

    for national_park in national_parks:
        file_metadata = {
            'name': national_park,
            'mimeType': 'application/vnd.google-apps.folder'
            # 'parents': []
        }

        service.files().create(body=file_metadata).execute()


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    """
    Uploads files to Google Drive/Sobe arquivos para o Google Drive.
    """
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    cred = None
    pickle_file = f'{path_gj2_data}/token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        logando_gdrive_f('verbose','Loading files to the Cloud')
        return service
    except Exception as e:
        logando_gdrive_f('warning','Was not possible to load the files to Cloud')
        return None


def subir_arquivo_drive_raiz(id_pasta, nome, mime, local):
    """
    Function that receive the variables to send to Create_Service/Variável que
    recebe variáveis para assim chamar a função Create_Service.

    :param id_pasta: ID of Google Drive folder/ID da pasta do Google Drive.
    :param nome: Name of Google Drive file/Nome do arquivo Google Drive.
    :param mime: Mime of file/Mime do arquivo.
    :param local: Path of file/Local do arquivo.
    """
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    folder_id = id_pasta
    file_names = [nome]
    mime_types = ['application/vnd.openxmlformats-officedoument.spreadsheetml']
    mime_types.append(mime)

    for file_name, mime_type in zip(file_names, mime_types):
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(local.format(file_name), mimetype=mime_type)

        service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()


def autenticar_id(id_pasta, nome, mime, local):
    """
    Sends a test file to authenticate the Google Drive account/Enviar um
    arquivo teste para autenticar a conta Google Drive.

    :param id_pasta: ID of Google Drive folder/ID da pasta do Google Drive.
    :param nome: Name of Google Drive file/Nome do arquivo Google Drive.
    :param mime: Mime of file/Mime do arquivo.
    :param local: Path of file/Local do arquivo.
    """
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    with open(f'{path_gj2_data}/etc/api/googledrv/id_folder.txt', 'w') as novo_id:
        novo_id.write(id_pasta)

    folder_id = id_pasta
    file_names = [nome]
    mime_types = ['application/vnd.openxmlformats-officedoument.spreadsheetml']
    mime_types.append(mime)

    for file_name, mime_type in zip(file_names, mime_types):
        file_metadata = {
            'name': file_name,
            'parents': id_pasta

        }

        media = MediaFileUpload(local.format(file_name), mimetype=mime_type)

        service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
