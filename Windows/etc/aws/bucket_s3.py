import sys
import time
import os.path
import logging
import datetime
import pathlib

import boto
import boto.s3
import boto.s3.connection


# Global variables/Variáveis globais.
path_atual_s3 = str(pathlib.Path(__file__).parent.absolute())
path_s3_final = path_atual_s3.replace('\\etc\\aws','')


def descobrir_hosts():
    """
    Gets the AWS S3 accounts/Pega as contas da AWS S3.
    """
    with open(f'{path_s3_final}/etc/serverx/config/s3_hosts.txt', 'r') as s3_hosts:
        lista_s3 = s3_hosts.read()
    lista_break_s3 = lista_s3.split('\n')
    return lista_break_s3


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


def subir_bucket_s3(diretorioUpload_v, key=None):
    """
    Upload the files to AWS S3/Sobe os arquivos para AWS S3.

    :param access_key_v: Access key/Chave de acesso.
    :param secret_key_v: Secret key/Chave secreta.
    :param bucket_name_v: Bucket name/Nome do bucket.
        - Need to be in lowercase mode
    :param diretorioUpload_v: File path/Local do arquivo.
    :param destDir_v: Name path of bucket/Nome do path do bucket.
    """
    hosts_s3_send = descobrir_hosts()

    for hosts in hosts_s3_send:
        hosts_temporario = hosts.split(';')

        if key != hosts_temporario[3]:
            break

        try:
            time.sleep(1.5)

            MAX_SIZE = 20 * 1000 * 1000
            PART_SIZE = 6 * 1000 * 1000

            hosts = hosts.split(';')
            access_key = hosts[0]
            secret_key = hosts[1]
            bucket_name = hosts[2]

            diretorioUpload = diretorioUpload_v
            destDir = str(datetime.datetime.now()).split(' ')[0] + '/'

            conn = boto.connect_s3(
                    aws_access_key_id = access_key,
                    aws_secret_access_key = secret_key,
                    host = 's3.us-east-1.amazonaws.com',
                    #is_secure=False,
                    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                    )

            time.sleep(1.5)

            try:
                bucket = conn.create_bucket(bucket_name,
                    location=boto.s3.connection.Location.DEFAULT)
                time.sleep(0.5)

            except:
                pass

            uploadFileNames = []

            for (diretorioUpload, dirname, filename) in os.walk(diretorioUpload):
                uploadFileNames.extend(filename)
                break

            for filename in uploadFileNames:
                sourcepath = os.path.join(diretorioUpload + filename)
                destpath = os.path.join(destDir, '', filename)
                filesize = os.path.getsize(sourcepath)

                if filesize > MAX_SIZE:
                    mp = bucket.initiate_multipart_upload(destpath)
                    fp = open(sourcepath,'rb')
                    fp_num = 0

                    while (fp.tell() < filesize):
                        fp_num += 1
                        mp.upload_part_from_file(fp, fp_num, cb=percent_cb, num_cb=10, size=PART_SIZE)
                    mp.complete_upload()

                else:
                    k = boto.s3.key.Key(bucket)
                    k.key = destpath
                    k.set_contents_from_filename(sourcepath,
                            cb=percent_cb, num_cb=10)

        except:
            pass
