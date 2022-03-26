#!/bin/sh
clear
echo "Pasando todos los archivos de prueba con errores a la aplicacion"
echo "-----Linea uno con mas elementos-----"
python3 mainCommandLine.py entradaLinea1Invalida.txt salida.txt
echo "-----Linea dos no coincide con lo marcado en la linea 1-----"
python3 mainCommandLine.py entradaLongitudLinea2Invalida.txt salida.txt
echo "-----Linea tres no coincide con lo marcado en la linea 1-----"
python3 mainCommandLine.py entradaLongitudLinea3Invalida.txt salida.txt
echo "-----Linea cuatro no coincide con lo marcado en la linea 1-----"
python3 mainCommandLine.py entradaLongitudLinea4Invalida.txt salida.txt
echo "-----M1 menor a 2-----"
python3 mainCommandLine.py entradaM1MEnorA2.txt salida.txt
echo "-----M1 mayor a 50-----"
python3 mainCommandLine.py entradaM1MayorA50.txt salida.txt
echo "-----M2 menor a 2-----"
python3 mainCommandLine.py entradaM2MenorA2.txt salida.txt
echo "-----M2 mayor a 50-----"
python3 mainCommandLine.py entradaM2MayorA50.txt salida.txt
echo "-----Caracteres invalidos en el mensaje-----"
python3 mainCommandLine.py entradaCaracteresInvalidosMensaje.txt salida.txt
echo "-----Caracteres repetidos en instruccion 1-----"
python3 mainCommandLine.py entradaCaracteresRepetidosInstruccion1.txt salida.txt
echo "-----Caracteres repetidos en instruccion 2-----"
python3 mainCommandLine.py entradaCaracteresRepetidosInstruccion2.txt salida.txt
echo "-----Dos instrucciones en el mismo mensaje-----"
python3 mainCommandLine.py entradaDosInstruccionesEnMensaje1.txt salida.txt

