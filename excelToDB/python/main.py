# coding=<utf-8>
# -*- coding: utf-8 -*-
import os
import sys
import math
import pandas
import codecs
import base64
import pathlib
import pymysql
import pymysql.cursors

from datetime import datetime



# Coleccion de funciones generales de un programa
class FuncGlobales():

    def Encrypt(O0OO00OOOOOOOO00O):
        if O0OO00OOOOOOOO00O.strip() == '' or O0OO00OOOOOOOO00O.strip() == None:
            return 'Error'
        O0OO00OOOOOOOO00O = str(O0OO00OOOOOOOO00O.strip())
        try:
            O0OO00OOOOOOOO00O = ''.join(hex(ord(O0O00O0O000OO000O))[2:] for O0O00O0O000OO000O in O0OO00OOOOOOOO00O)
        except:
            return 'Error'
        O0OO00OOOOOOOO00O = O0OO00OOOOOOOO00O.upper()
        try:
            O0OO00OOOOOOOO00O = base64.b64encode(O0OO00OOOOOOOO00O.encode(
                str(''.join([chr(int(''.join(c), 16)) for c in zip('7574662D38'[0::2], '7574662D38'[1::2])]))))
            O0OO00OOOOOOOO00O = str(O0OO00OOOOOOOO00O, str(
                ''.join([chr(int(''.join(c), 16)) for c in zip('7574662D38'[0::2], '7574662D38'[1::2])])))
            O0OO00OOOOOOOO00O = codecs.encode(O0OO00OOOOOOOO00O, str(
                ''.join([chr(int(''.join(c), 16)) for c in zip('726F745F3133'[0::2], '726F745F3133'[1::2])])))
        except:
            return 'Error'
        try:
            O0OO00OOOOOOOO00O = ''.join(
                hex(ord(OOO00000OOOO00OO0))[2:] for OOO00000OOOO00OO0 in O0OO00OOOOOOOO00O)  # line:21
        except:
            return 'Error'
        O0OO00OOOOOOOO00O = O0OO00OOOOOOOO00O.upper()
        O0OO00OOOOOOOO00O = str(O0OO00OOOOOOOO00O.strip())
        return O0OO00OOOOOOOO00O

    def DeCrypt(OOOOOOOO000000OO0):
        if OOOOOOOO000000OO0.strip() == '' or OOOOOOOO000000OO0.strip() == None:
            return 'Error'
        OOOOOOOO000000OO0 = str(OOOOOOOO000000OO0.strip())
        try:
            OOOOOOOO000000OO0 = ''.join([chr(int(''.join(O0O000000O0O00O00), 16)) for O0O000000O0O00O00 in zip(OOOOOOOO000000OO0[0::2], OOOOOOOO000000OO0[1::2])])
        except:
            return 'Error'
        try:
            OOOOOOOO000000OO0 = codecs.decode(OOOOOOOO000000OO0, str(
                ''.join([chr(int(''.join(c), 16)) for c in zip('726F745F3133'[0::2], '726F745F3133'[1::2])])))
        except:
            return 'Error'
        try:
            OOOOOOOO000000OO0 = OOOOOOOO000000OO0.encode(
                str(''.join([chr(int(''.join(c), 16)) for c in zip('6173636969'[0::2], '6173636969'[1::2])])))
            OOOOOOOO000000OO0 = base64.b64decode(OOOOOOOO000000OO0)
            OOOOOOOO000000OO0 = OOOOOOOO000000OO0.decode(
                str(''.join([chr(int(''.join(c), 16)) for c in zip('6173636969'[0::2], '6173636969'[1::2])])))
        except:
            return 'Error'
        try:
            OOOOOOOO000000OO0 = ''.join([chr(int(''.join(OO0O0O0OOOO0O0000), 16)) for OO0O0O0OOOO0O0000 in zip(OOOOOOOO000000OO0[0::2], OOOOOOOO000000OO0[1::2])])
        except:
            return 'Error'
        OOOOOOOO000000OO0 = str(OOOOOOOO000000OO0.strip())
        return OOOOOOOO000000OO0


# Variables de configuracion
# IPServidor = '417A5A324D774C6D417752324C6D4C34417A4C335A6D7030'
# UsuarioServidor = '417A4C335A514C31414A4C335A51706C416D483241474C6C417752335A6A3D3D'
# ContrasenaServidor = '416D4E335A777031417748325A774C6B416D5A3041514C31416D5A325A47706C416D56324D774D77417A5A324D775A6C5A6D4E6D5A775A6C'
# BaseDatosServidor = '416D563241474C6D417A5A325A474D78417A4C335A6D706A417A4C33416D4C31416D566D5A775A6A5A6D566D5A443D3D'
# Estado1 = 'Activo'
# Estado2 = 'Inactivo'
IPServidor = 'localhost'
UsuarioServidor = 'root'
ContrasenaServidor = 'root'
BaseDatosServidor = 'db_links'
Estado1 = 'Active'
Estado2 = 'Inactive'



# connectionMySQL = pymysql.connect(
#     # host = FuncGlobales.DeCrypt(IPServidor),
#     # user = FuncGlobales.DeCrypt(UsuarioServidor),
#     # password = FuncGlobales.DeCrypt(ContrasenaServidor),
#     # db = FuncGlobales.DeCrypt(BaseDatosServidor),
#     # charset = 'utf8',
#     # cursorclass = pymysql.cursors.DictCursor
#     host = FuncGlobales.DeCrypt(IPServidor),
#     user = UsuarioServidor,
#     password = ContrasenaServidor,
#     db = BaseDatosServidor,
#     charset = 'utf8',
#     cursorclass = pymysql.cursors.DictCursor
# )


EST_CDETALLE = sys.argv[1]

# # Consulta datos del ususario
# with connectionMySQL.cursor() as cursor:
#     # sql = "SELECT PKSAP_NCODIGO FROM " + str(FuncGlobales.DeCrypt(BaseDatosServidor)).strip() + ".tbl_rcaso_sap WHERE SAP_CESTADO = '" + str(Estado1).strip() + "';"
#     sql = "SELECT PKPER_NCODIGO, PER_CNIVEL, PER_CCAMPANA FROM " + str(FuncGlobales.DeCrypt(BaseDatosServidor)).strip() + ".tbl_rpermiso WHERE PKPER_NCODIGO = " + AGENTE + " PER_CESTADO = '" + str(Estado1).strip() + "';"
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#     if len(rows) > 0:
#         # pass
#         for row in rows:
#             PKPER_NCODIGO = row['PKPER_NCODIGO']
#             PER_CNIVEL = row['PER_CNIVEL']
#             PER_CCAMPANA = row['PER_CCAMPANA']


# Manejo del fichero
rutaArchivo = os.path.join(pathlib.Path(__file__).parent.parent.absolute(), 'xls', 'test.xls')
abreArchivo = pandas.read_excel(rutaArchivo, engine="openpyxl", sheet_name="Hoja1")
datos = abreArchivo.values

for i in datos:

    # pass
    Codificacion = i[0]
    CodifTxt = i[1]
    CentroPtoTbjo = i[2]
    Poblacion = i[3]
    Centroplanif = i[4]
    DenomEjecut = i[5]
    NoPedido = i[6]
    FechaAviso = i[7]
    Aviso = i[8]
    FechaCierre = i[9]
    Descripcion = i[10]
    ReemplazoEquipo = i[11]
    CuentaContrato = i[12]
    Instalacion = i[13]
    CeEmplazam = i[14]
    StatusUsuario = i[15]
    Sociedad = i[16]
    AutorAviso = i[17]
    ModificadoPor = i[18]
    ClaseTarifa = i[19]
    TipoRespuesta = i[20]
    Reiteracion = i[21]
    ClaseAviso = i[22]
    FaltaInformacion = i[23]
    FCR = i[24]
    MalClasificado = i[25]
    InicioDeseado = i[26]
    FinDeseado = i[27]
    HoraCierre = i[28]
    ModificadoEl = i[29]
    ModificadoALas = i[30]


    # print(type(ModificadoEl), ModificadoEl)
    if type(ModificadoEl) is datetime:
        pass
        # print(type(ModificadoEl), ModificadoEl, ModificadoEl)
    else:
        # ModificadoEl = str(ModificadoEl)
        # datetime.strptime(date_string, "%d %B, %Y")
        try:
            ModificadoEl = datetime.strptime(ModificadoEl, "%d/%m/%Y")
        except:
            try:
                ModificadoEl = datetime.strptime(ModificadoEl, "%Y/%m/%d")
            except:
                try:
                    ModificadoEl = datetime.strptime(ModificadoEl, "%Y-%m-%d")
                except:
                    ModificadoEl = datetime.strptime(ModificadoEl, "%d-%m-%Y")

    print(type(ModificadoEl), ModificadoEl)