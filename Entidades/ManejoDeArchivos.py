class ManejadorDeArchivos:
    def __init__(self, nombre_archivo):
        self.__nombre_archivo = nombre_archivo

    def leer_archivo(self):
        try:
            with open(self.__nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            return f"El archivo '{self.__nombre_archivo}' no se encontró."
        except Exception as e:
            return f"Ocurrió un error al leer el archivo: {str(e)}"

    def escribir_archivo(self, contenido):
        try:
            with open(self.__nombre_archivo, 'w') as archivo:
                archivo.write(contenido)
            return ""
        except Exception as e:
            return f"Ocurrió un error al escribir en el archivo: {str(e)}"