import sys

sys.path.append("./app/")
from Processor import Processor

if __name__ == '__main__' :
    try :
        print("Neubox - Challenge 1 - ahora en python")
        if len(sys.argv) != 3:
            raise Exception("Los parametros para la ejecución de la aplicación no son los correctos, debe agregar el nombre del archivo de entrada y el nombre del archivo de salida")
            
        archivoEntrada = sys.argv[1]
        archivoSalida = sys.argv[2]

        Procesador = Processor()
        response = Procesador.procesar_archivo(archivoEntrada, archivoSalida)

        if response["status"]:
            print('Información: ' + response["message"])
        else:
            print('Error: ' + response["message"])

    except Exception as e:
        if hasattr(e, 'message'):
            print('Error : ' + e.message)
        else:
            #print(type(e))    # the exception instance
            #print(e.args)     # arguments stored in .args
            #print(e)


            print('Error : '+ e.args[0])
