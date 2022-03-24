import re
from File import File


class Processor(File):
    data = ""

    def procesar_archivo(self, rutaArchivo):
        error = ""
        try:
            data = self.read_txt(rutaArchivo)

            if len(data) == 4:
                self.validar_datos(data)

                resultado = self.generar_mensaje(data)
                self.crear_txt(resultado)

            else:
                raise ValueError("La estructura del archivo no coincide con la definición de cuatro líneas")

        except ValueError as e:
            error = e

        return self.generate_response(error)


    def validar_datos(self, data):
        self.validar_instrucciones(data)

        if self.data[0][0] != len(self.data[1]):
            raise ValueError(
                "Error en linea 1 y linea 2, la longitud no coincide con M1"
            )

        if self.data[0][1] != len(self.data[2]):
            raise ValueError(
                "Error en linea 1 y linea 3, la longitud no coincide con M2"
            )

        if self.data[0][2] != len(self.data[3]):
            raise ValueError(
                "Error en linea 1 y linea 4, la longitud no coincide con N"
            )


    def validar_instrucciones(self, data):
        error = ""
        insList = data[0].split(" ")
        nuevaLista = []

        if len(insList) != 3:
            error = "La cantidad de parámetros no es la correcta, deben de ser 3"

        else:
            for num in insList:
                if num.isnumeric():
                    nuevaLista.append(int(num))

                else:
                    error = "Los datos de los tamaños de los mensajes no son numericos"

            if error == "":
                M1 = nuevaLista[0]
                M2 = nuevaLista[1]
                N = nuevaLista[2]

                instruccion1 = data[1]
                instruccion2 = data[2]
                mensaje = data[3]

                if M1 < 2:
                    error = "Error en datos: linea 1, la longitud de la instrucción 1 debe ser mayor a 2"

                elif M1 > 50:
                    error = "Error en datos: linea 1, la longitud de la instrucción 1 debe ser menor a 50"

                elif M2 < 2:
                    error = "Error en datos: linea 1, la longitud de la instrucción 2 debe ser mayor a 2"

                elif M2 > 50:
                    error = "Error en datos: linea 1, la longitud de la instrucción 2 debe ser menor a 50"

                elif N < 3:
                    error = "Error en datos: linea 1, la longitud del mensaje debe ser mayor a 3"

                elif N > 5000:
                    error = "Error en datos: linea 1, la longitud de la instrucción 2 debe ser menor a 5000"

                else:
                    error = (
                        ""
                        if re.match("^[a-zA-Z0-9]+$", mensaje) is not None
                        else "Error en datos: linea 4, formato de mensaje, solo debe contener letras y números"
                    )
            instruccion1 =  self.limpiar_mensaje(instruccion1)
            instruccion2 =  self.limpiar_mensaje(instruccion1)
            self.data = data
            self.data[0] = nuevaLista

        if error != "":
            raise ValueError(error)

    def generar_mensaje(self, data):

        nuevoM1 = data[1]
        nuevoM2 = data[2]
        nuevoMensaje = self.limpiar_mensaje(data[3])
        resultado = ""

        M1 = "Si" if nuevoM1 in nuevoMensaje else "No"
        M2 = "Si" if nuevoM2 in nuevoMensaje else "No"

        if M1 == "Si" and M2 == "Si":
            raise ValueError(
                "Se encontraron las dos instrucciones en el mensaje por lo que no se puede definir cual es el mensaje oculto."
            )
        else:
            resultado = M1 + "\n" + M2

        return resultado

    def limpiar_mensaje(self, mensaje):
        nuevoMensaje = ""

        letraAnterior = ""

        for letra in mensaje:
            letraMinus = letra

            if letraAnterior != letraMinus:
                nuevoMensaje += letra

            letraAnterior = letraMinus

        return nuevoMensaje

    """ Genera una respuesta tipo arreglo con un status y un mensaje"""

    def generate_response(self, error):
        return {
            "status": (error == ""),
            "message": error
            if (error != "")
            else "Archivo procesado correctamente, se genero un archivo (salida.txt) con los resultados",
        }
