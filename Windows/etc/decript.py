import os
import pathlib

from cryptography.fernet import Fernet


# Global variables/Variáveis globais.
path_atual_dc = str(pathlib.Path(__file__).parent.absolute())
path_dc_final = path_atual_dc.replace('\\etc','')


def decript_file(arquivo, chave=None):
    """
    Decrypt a file/Desencriptografa uma arquivo.

    :param arquivo: Path file/Local do arquivo.
    :param chave: Key/Chave
    """
    if chave == None:
        with open(f'{path_dc_final}/etc/key_crypt.txt', 'r') as pegar_key:
            key = pegar_key.read()

        input_file = arquivo #+ '.encrypted'
        output_file = arquivo

        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)

        arquivo_f = str(arquivo)
        arquivo_f = arquivo_f.replace('.encrypted', '')
        os.rename(arquivo, arquivo_f)

    else:
        try:
            key = str(chave)
            input_file = arquivo
            output_file = arquivo

            with open(input_file, 'rb') as f:
                data = f.read()
            fernet = Fernet(key)

            try:
                decrypted = fernet.decrypt(data)

                with open(output_file, 'wb') as f:
                    f.write(decrypted)
                arquivo_f = str(arquivo)
                arquivo_f = arquivo_f.replace('.encrypted', '')
                os.rename(arquivo, arquivo_f)

            except:
                pass

        except:
            pass