import json

# Función para convertir un caracter a su token
def caracter_a_token(caracter):
    codigo_unicode = hex(ord(caracter))[2:].upper()
    if codigo_unicode in TOKENS:
        return TOKENS[codigo_unicode]
    else:
        return f"0000" # Caracter Nulo

# Diccionario con los tokens
TOKENS = {
    "00": "0000", # Carácter Nulo
    "01": "0001", # Inicio de Encabezado
    "02": "0002", # Inicio de Texto
    "03": "0003", # Fin de Texto
    "04": "0004", # Fin de Transmisión
    "05": "0005", # Consulta
    "06": "0006", # Acuse de recibo
    "07": "0007", # Timbre
    "08": "0008", # Retroceso
    "09": "0009", # Tabulación horizontal
    "0A": "000A", # Salto de línea
    "0B": "000B", # Tabulación Vertical
    "0C": "000C", # De avance
    "0D": "000D", # Retorno de carro
    "0E": "000E", # Desplazamiento hacia fuera
    "0F": "000F", # Desplazamiento hacia dentro
    "10": "0010", # Enlace de datos
    "11": "0011", # Dispositivo de control 1
    "12": "0012", # Dispositivo de control 2
    "13": "0013", # Dispositivo de control 3
    "14": "0014", # Dispositivo de control 4
    "15": "0015", # Confirmación negativa
    "16": "0016", # Síncrono en espera
    "17": "0017", # Fin de Transmisión del Bloque
    "18": "0018", # Cancelar
    "19": "0019", # Finalización del Medio
    "1A": "001A", # Substituto
    "1B": "001B", # Escape
    "1C": "001C", # Separador de fichero
    "1D": "001D", # Separador de grupo
    "1E": "001E", # Separador de registro
    "1F": "001F", # Separador de unidad
    "20": "0020", # Espacio
    "21": "0021", # !
    "22": "0022", # "
    "23": "0023", # #
    "24": "0024", # $
    "25": "0025", # %
    "26": "0026", # &
    "27": "0027", # '
    "28": "0028", # (
    "29": "0029", # )
    "2A": "002A", # *
    "2B": "002B", # +
    "2C": "002C", # ,
    "2D": "002D", # -
    "2E": "002E", # .
    "2F": "002F", # /
    "30": "0030", # 0
    "31": "0031", # 1
    "32": "0032", # 2
    "33": "0033", # 3
    "34": "0034", # 4
    "35": "0035", # 5
    "36": "0036", # 6
    "37": "0037", # 7
    "38": "0038", # 8
    "39": "0039", # 9
    "3A": "003A", # :
    "3B": "003B", # ;
    "3C": "003C", # <
    "3D": "003D", # =
    "3E": "003E", # >
    "3F": "003F", # ?
    "40": "0040", # @
    "41": "0041", # A
    "42": "0042", # B
    "43": "0043", # C
    "44": "0044", # D
    "45": "0045", # E
    "46": "0046", # F
    "47": "0047", # G
    "48": "0048", # H
    "49": "0049", # I
    "4A": "004A", # J
    "4B": "004B", # K
    "4C": "004C", # L
    "4D": "004D", # M
    "4E": "004E", # N
    "4F": "004F", # O
    "50": "0050", # P
    "51": "0051", # Q
    "52": "0052", # R
    "53": "0053", # S
    "54": "0054", # T
    "55": "0055", # U
    "56": "0056", # V
    "57": "0057", # W
    "58": "0058", # X
    "59": "0059", # Y
    "5A": "005A", # Z
    "5B": "005B", # [
    "5C": "005C", # \
    "5D": "005D", # ]
    "5E": "005E", # ^
    "5F": "005F", # _
    "60": "0060", # `
    "61": "0061", # a
    "62": "0062", # b
    "63": "0063", # c
    "64": "0064", # d
    "65": "0065", # e
    "66": "0066", # f
    "67": "0067", # g
    "68": "0068", # h
    "69": "0069", # i
    "6A": "006A", # j
    "6B": "006B", # k
    "6C": "006C", # l
    "6D": "006D", # m
    "6E": "006E", # n
    "6F": "006F", # o
    "70": "0070", # p
    "71": "0071", # q
    "72": "0072", # r
    "73": "0073", # s
    "74": "0074", # t
    "75": "0075", # u
    "76": "0076", # v
    "77": "0077", # w
    "78": "0078", # x
    "79": "0079", # y
    "7A": "007A", # z
    "7B": "007B", # {
    "7C": "007C", # |
    "7D": "007D", # }
    "7E": "007E", # ~
    "7F": "007F", # Delete
    "8D": "2386", # Enter
}

# Abrir archivo JSON
with open("ejemplo.json", "r") as archivo:
    datos = json.load(archivo)

# Recorrer cada caracter del archivo JSON
for caracter in str(datos):
    # Imprimir caracter y token
    print(f" {caracter_a_token(caracter)} := {caracter} ")
