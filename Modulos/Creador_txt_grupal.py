#Librerías
import os
#Función para convertir un conjunto de datas divididas por dias en un archivo .txt.
def crear_txt(arreglo, nombre):
    ##Crear la carpeta si no existe
    if not os.path.exists("Archivos_txt"):
        os.makedirs("Archivos_txt")
    with open(os.path.join("Archivos_txt", "Dias_totales-"+str(nombre)), 'w') as file:
        #Abre (o crea) un archivo en modo de escritura.
        file.write('Hora num, Temperatura exterior\n')
        #Para leer cada data.
        for i in arreglo:
            #Para leer cada fila de cada data.
            for e in i:
                #Se usa para solo tomar lo relevante de cada data.
                continuar = 0
                for o in e:
                    #Para guardar la temperatura.
                    if continuar == len(e)-1:
                        file.write(str(o))
                    #Para guardar el tiempo.
                    elif continuar > 0:
                        file.write(str(o)+',')
                    #Se usa para solo tomar lo relevante de cada data.
                    continuar = continuar+1
                 #Para dejar un espacio, (representa las filas).   
                file.write('\n')
            #Para dejar un espacio demás, (representa la división entre una data y otra).
            file.write('\n')
        #Para avisar que se ha creadi satisfactoriamente el .txt.
        print("Se han guardado todos los datos en 'Dias_totales-"+str(nombre)+".txt'")
                
                
       
