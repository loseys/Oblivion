def separar_atributos(texto):
    """
    Separates the attributes/Separa os atributos.
    """
    atributos = []

    if '&%loop' in texto:
        atributos.append('loop')

    if '&common_web' in texto:
        atributos.append('common_web')

    if '&google_dorks' in texto:
        atributos.append('google_dorks')

    if '&wordlists' in texto:
        atributos.append('wordlists')

    if '&api' in texto:
        atributos.append('api')

    if '&dado_bruto' in texto:
        atributos.append('dado_bruto')

    if '&txt_f' in texto:
        atributos.append('txt_f')

    if '&txt_ocult' in texto:
        atributos.append('txt_ocult')

    if '&txt_cript' in texto:
        atributos.append('txt_cript')

    if '&docx_f' in texto:
        atributos.append('docx_f')

    if '&docx_ocult' in texto:
        atributos.append('docx_ocult')

    if '&docx_cript' in texto:
        atributos.append('docx_criopt')

    if '&pdf_f' in texto:
        atributos.append('pdf_f')

    if '&pdf_ocult' in texto:
        atributos.append('pdf_ocult')

    if '&pdf_cript' in texto:
        atributos.append('pdf_cript')

    if '&xlsx_f' in texto:
        atributos.append('xlsx_f')

    if '&xlsx_ocult' in texto:
        atributos.append('xlsx_ocult')

    if '&xlsx_cript' in texto:
        atributos.append('xlsx_cript')

    if '&json_f' in texto:
        atributos.append('json_f')

    if '&json_ocult' in texto:
        atributos.append('json_ocult')

    if '&json_cript' in texto:
        atributos.append('json_cript')

    if '&html_f' in texto:
        atributos.append('html_f')

    if '&html_ocult' in texto:
        atributos.append('html_ocult')

    if '&html_cript' in texto:
        atributos.append('html_cript')

    if '&xsl_f' in texto:
        atributos.append('xsl_f')

    if '&xsl_ocult' in texto:
        atributos.append('xsl_ocult')

    if '&xsl_cript' in texto:
        atributos.append('xsl_cript')

    if '&db_f' in texto:
        atributos.append('db_f')

    if '&db_ocult' in texto:
        atributos.append('db_ocult')

    if '&db_cript' in texto:
        atributos.append('db_cript')

    if '&gdrive' in texto:
        atributos.append('gdrive')

    if '&aws_s3' in texto:
        atributos.append('aws_s3')

    if '&ssh' in texto:
        atributos.append('ssh')

    return atributos

def separar_atributos_headers(texto):
    """
    Separates the attributes of Headers/Separa os atributos do Headers.
    """
    atributos = []

    try:
        if texto['loop'] == 'True':
            atributos.append('loop')
    except:
        pass

    try:
        if texto['common_web'] == 'True':
            atributos.append('common_web')
    except:
        pass

    try:
        if texto['google_dorks'] == 'True':
            atributos.append('google_dorks')
    except:
        pass

    try:
        if texto['wordlists'] == 'True':
            atributos.append('wordlists')
    except:
        pass

    try:
        if texto['api'] == 'True':
            atributos.append('api')
    except:
        pass

    try:
        if texto['dado_bruto'] == 'True':
            atributos.append('dado_bruto')
    except:
        pass

    try:
        if texto['txt_f'] == 'True':
            atributos.append('txt_f')
    except:
        pass

    try:
        if texto['txt_ocult'] == 'True':
            atributos.append('txt_ocult')
    except:
        pass

    try:
        if texto['txt_cript'] == 'True':
            atributos.append('txt_cript')
    except:
        pass

    try:
        if texto['docx_f'] == 'True':
            atributos.append('docx_f')
    except:
        pass

    try:
        if texto['docx_ocult'] == 'True':
            atributos.append('docx_ocult')
    except:
        pass

    try:
        if texto['docx_cript'] == 'True':
            atributos.append('docx_criopt')
    except:
        pass

    try:
        if texto['pdf_f'] == 'True':
            atributos.append('pdf_f')
    except:
        pass

    try:
        if texto['pdf_ocult'] == 'True':
            atributos.append('pdf_ocult')
    except:
        pass

    try:
        if texto['pdf_cript'] == 'True':
            atributos.append('pdf_cript')
    except:
        pass

    try:
        if texto['xlsx_f'] == 'True':
            atributos.append('xlsx_f')
    except:
        pass

    try:
        if texto['xlsx_ocult'] == 'True':
            atributos.append('xlsx_ocult')
    except:
        pass

    try:
        if texto['xlsx_cript'] == 'True':
            atributos.append('xlsx_cript')
    except:
        pass

    try:
        if texto['json_f'] == 'True':
            atributos.append('json_f')
    except:
        pass

    try:
        if texto['json_ocult'] == 'True':
            atributos.append('json_ocult')
    except:
        pass

    try:
        if texto['json_cript'] == 'True':
            atributos.append('json_cript')
    except:
        pass

    try:
        if texto['html_f'] == 'True':
            atributos.append('html_f')
    except:
        pass

    try:
        if texto['html_ocult'] == 'True':
            atributos.append('html_ocult')
    except:
        pass

    try:
        if texto['html_cript'] == 'True':
            atributos.append('html_cript')
    except:
        pass

    try:
        if texto['xsl_f'] == 'True':
            atributos.append('xsl_f')
    except:
        pass

    try:
        if texto['xsl_ocult'] == 'True':
            atributos.append('xsl_ocult')
    except:
        pass

    try:
        if texto['xsl_cript'] == 'True':
            atributos.append('xsl_cript')
    except:
        pass

    try:
        if texto['db_f'] == 'True':
            atributos.append('db_f')
    except:
        pass

    try:
        if texto['db_ocult'] == 'True':
            atributos.append('db_ocult')
    except:
        pass

    try:
        if texto['db_cript'] == 'True':
            atributos.append('db_cript')
    except:
        pass

    try:
        if texto['gdrive'] == 'True':
            atributos.append('gdrive')
    except:
        pass

    try:
        if texto['aws_s3'] == 'True':
            atributos.append('aws_s3')
    except:
        pass

    try:
        if texto['ssh'] == 'True':
            atributos.append('ssh')
    except:
        pass

    return atributos