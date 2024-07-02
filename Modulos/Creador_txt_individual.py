#Librerías
import os
#Función para convertir un conjunto de datas divididas por dias en varios archivos .txt, uno por cada dia.
def crear_txt(arreglo, nombre):
    ##Nombre de los directorios.
    carpeta = "Archivos_txt"
    subcarpeta = nombre
    ##Para crear la carpeta principal si no existe.
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    ##Crear la subcarpeta dentro de la carpeta principal
    carpeta_sub = os.path.join(carpeta, subcarpeta)
    if not os.path.exists(carpeta_sub):
        os.makedirs(carpeta_sub)
    #Para enumerar cada archivo .txt desde el primero al ultimo.
    conteo = 0
    #Para leer cada data.
    for i in arreglo:
        #Para irle subiendo a la enumeración.
        conteo = conteo+1
        #Abre (o crea) un archivo en modo de escritura
        with open(os.path.join(carpeta_sub,"Dia_"+str(conteo)+"-"+str(nombre)+".txt"),'w') as file:
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
    print("Se han guardado todos los datos en archivos de texto en /Archivos_txt/"+str(nombre))
                
                
       

