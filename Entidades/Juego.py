import random

class Juego:
    LIMITE_INTENTOS = 14

    def __init__(self):
        self.__numero_secreto = self.generar_numero_secreto()
        self.intentos = 0
        self.suposiciones = []
        
    
    @classmethod
    def generar_numero_secreto(cls):
        cifras_aleatorias = random.sample(range(10), 4)
        numero_secreto = ''.join(map(str, cifras_aleatorias))
        return numero_secreto
    
    @property
    def get_numero_secreto(self):
        return self.__numero_secreto
    
    #La funcion que se llama por cada intento(Devuelve un error o el resultado)
    def validar_entrada(self, numero):
        errores = []
        numero = numero.strip()

        if self.suposiciones.__contains__(numero):
            errores.append(f"No se puede repetir la misma entrada")

        if not numero.isnumeric():
            errores.append(f"La entrada debe contener solo caracteres numéricos.")
        else:
            if len(set(numero)) != len(numero):
                errores.append(f"No se permiten cifras repetidas en la entrada.")

        if len(numero) != 4:
            errores.append(f"La entrada no tiene longitud 4.")

        # Uso de tupla para diferenciar los errores de los resultados
        if errores:
            return "\n".join(errores) , "err"
        else:
            self.suposiciones.append(numero)
            return self.__calcular_muertos_heridos(numero)

    def __calcular_muertos_heridos(self, entrada):
        muertos = 0
        heridos = 0

        for i in range(4):
            if entrada[i] == self.__numero_secreto[i]:
                muertos += 1
            elif entrada[i] in self.__numero_secreto:
                heridos += 1

        if muertos == 4:
            return f"¡Has adivinado el número!", "success"
        else:
            # Verificar si es el último intento
            if self.intentos == self.LIMITE_INTENTOS-1 and muertos != 4:
                return "!HAS PERDIDO¡ PULSA ENTER PARA REINICIAR", "end"
            else:
                self.intentos += 1
                return (muertos, heridos), "again"



