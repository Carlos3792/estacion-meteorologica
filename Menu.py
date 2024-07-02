#Librerias externas:
import os
##Librerias propias:
from Modulos import Lector_archivo_csv
from Modulos import Graficador_matplotlib
from Modulos import Creador_txt_individual
from Modulos import Creador_txt_grupal
from Modulos import Generador_descenso_gradiente
from Modulos import Generador_regresion_lineal
from Modulos import Graficador_con_linea_matplotlib
from Modulos import Graficador_gnuplot
from Modulos import Graficador_con_linea_gnuplot
from Modulos import Generador_regresion_polinomial
from Modulos import Graficador_con_polinomio_matplotlib
#Logica del menu.
def menu():
    ##Variables a usar.
    etiqueta1 = ""  #Para la data escogida.
    etiqueta2 = ""  #Para el tipo de generador de linea escogido para los datos.
    etiqueta3 = ""  #Para el tipo de generador de linea escogido para m y b.
    etiqueta4 = ""  #Para el polinomio arbitrario.
    dia = 0
    x = []
    m_b = []
    m_b_linea = []
    ass = []       #Para guardar los polinomios de orden arbitrario.
    ass_linea = [] #Para guardar los polinomios de orden arbitrario de los m y b.
    #si x tiene datos será igual a 1 --- si m y b tienen datos serán iguale a 1 --- si m y b tienen m y b será 1. --- si no a generado el polinomio arbitrario para los dias. -- si no a generado un polinomio arbitrario para m y b.
    activado = [0,0,0,0,0]
    ##Ejecución del menu visual.
    mostrar_menu(1, x, dia)
    #Aplicación de la lógica del menú.
    while True:
        #Respuesta del primer menú - El principal.
        respuesta = input("===>")
        ###Para extraer y normalizar datos.
        if respuesta == "1":
            ##Muestra del menú de archivos csv para normalizar.
            limpiar_consola()
            mostrar_menu(2, x, dia)
            respuesta = input("===>")
            ##Opciones de archivos csv a escoger.
            seguir = True
            while seguir:
                seguir = False
                if respuesta == "1":
                    x = Lector_archivo_csv.leer_normalizar("Data_sets/datos1.csv")
                    etiqueta1 = "datos1"
                    limpiar_consola()
                    mostrar_menu(1, x, dia)
                    mostrar_menu(3, x, dia)
                elif respuesta == "2":
                    x = Lector_archivo_csv.leer_normalizar("Data_sets/datos2.csv")
                    etiqueta1 = "datos2"
                    limpiar_consola()
                    mostrar_menu(1, x, dia)
                    mostrar_menu(3, x, dia)
                elif respuesta == "3":
                    x = Lector_archivo_csv.leer_normalizar("Data_sets/datos3.csv")
                    etiqueta1 = "datos3"
                    limpiar_consola()
                    mostrar_menu(1, x, dia)
                    mostrar_menu(3, x, dia)
                elif respuesta == "4":
                    x = Lector_archivo_csv.leer_normalizar("Data_sets/datos4.csv")
                    etiqueta1 = "datos4"
                    limpiar_consola()
                    mostrar_menu(1, x, dia)
                    mostrar_menu(3, x, dia)
                ##Excepciones.
                else:
                    #Para opción invalida.
                    limpiar_consola()
                    mostrar_menu(2, x, dia)
                    mostrar_menu(11, x, dia)
                    respuesta = input("===>")
                    seguir = True
            ##Para concluir.
            activado[0] = 1
            respuesta = "0"
        ###Para visualizar datos del archivo csv seleccionado.
        elif respuesta == "2":
            #Para si no ha escogido un archivo csv.
            if activado[0] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(4, x, dia)
            #Para si ya escogió un archivo csv.
            else:
                ##Menú de opciones de visualización de datos.
                limpiar_consola()
                mostrar_menu(5, x, dia)
                respuesta = input("===>")
                #Opciones de visualización a escoger.
                seguir = True
                while seguir:
                    seguir = False
                    #Para mostrar el total de datos - len(x).
                    if respuesta == "1":
                        limpiar_consola()
                        mostrar_menu(1, x, dia)
                        mostrar_menu(8, x, len(x))
                    #Para mostrar todos los datos (x).
                    elif respuesta == "2":
                        limpiar_consola()
                        print("Respuesta:")
                        print(x)
                        mostrar_menu(1, x, dia)
                    #Para mostrar todos los datos de un dia.
                    elif respuesta == "3":
                        limpiar_consola()
                        mostrar_menu(6, x, dia)
                        #Aquí se digita la posición del dia a mirar.
                        seguir = True
                        while seguir:
                            try:
                                seguir = False
                                respuesta = int(input("===>"))-1
                                print("Respuesta:")
                                print(x[respuesta])            
                                mostrar_menu(1, x, dia)
                            #Excepciones.
                            except ValueError:
                                seguir = True
                                limpiar_consola()
                                mostrar_menu(6, x, dia)
                                mostrar_menu(12, x, dia)
                            except IndexError:
                                seguir = True
                                limpiar_consola()
                                mostrar_menu(6, x, dia)
                                mostrar_menu(11, x, dia)                                
                    #Para mostrar la columna de un dia.
                    elif respuesta == "4":
                        limpiar_consola()
                        #Menú de selección de dia.
                        mostrar_menu(6, x, dia)
                        #Para iniciar con la selección del dia.
                        seguir = True
                        while seguir:
                            try:
                                seguir = False
                                dia = int(input("===>"))-1
                                limpiar_consola()
                                #Menú de selección de fila.
                                mostrar_menu(7, x, dia)        
                                seguir = True
                                while seguir:
                                    try:
                                        #Selección de fila.
                                        respuesta = int(input("===>"))-1
                                        limpiar_consola()
                                        print("Respuesta:")
                                        print(x[dia][respuesta])            
                                        mostrar_menu(1, x, dia)
                                    #Excepciones
                                    except ValueError:
                                        seguir = True
                                        limpiar_consola()
                                        mostrar_menu(7, x, dia)
                                        mostrar_menu(12, x, dia)
                                    except IndexError:
                                        seguir = True
                                        limpiar_consola()
                                        mostrar_menu(7, x, dia)
                                        mostrar_menu(11, x, dia)        
                            #Excepciones    
                            except ValueError:
                                seguir = True
                                limpiar_consola()
                                mostrar_menu(6, x, dia)
                                mostrar_menu(12, x, dia)
                            except IndexError:
                                seguir = True
                                limpiar_consola()
                                mostrar_menu(6, x, dia)
                                mostrar_menu(11, x, dia)                     
                    #Para si se equivocó al seleccionar una opción de visualización.
                    else:
                        #Falta mensaje de no se pudo
                        limpiar_consola()
                        mostrar_menu(5, x, dia)
                        mostrar_menu(11, x, dia)
                        respuesta = input("===>")
                        seguir = True    
            ##Para concluir.
            respuesta = "0"   
        ###Opción para graficar con matplotlib
        elif respuesta == "3":
            #Para si no ha escogido un archivo csv.
            if activado[0] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(4, x, dia)
            else:
                limpiar_consola()
                print("Respuesta:")
                Graficador_matplotlib.graficar_datos(x, etiqueta1)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
                #Para concluir
            respuesta = "0"   
        ###Opción para crear un txt individual.
        elif respuesta == "4":
            #Para si no ha escogido un archivo csv.
            if activado[0] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(4, x, dia)
            else:
                limpiar_consola()
                print("Respuesta:")
                Creador_txt_individual.crear_txt(x, etiqueta1)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0" 
        ###Opción para crear un txt grupal.
        elif respuesta == "5":
            #Para si no ha escogido un archivo csv.
            if activado[0] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(4, x, dia)
            else:
                limpiar_consola()
                print("Respuesta:")
                Creador_txt_grupal.crear_txt(x, etiqueta1)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0" 
        ###Opción para generar una linea de regresión lineal para los datos.
        elif respuesta == "6":
            #Para si no ha escogido un archivo csv.
            if activado[0] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(4, x, dia)
            else:
                limpiar_consola()
                m_b = Generador_regresion_lineal.generar_lineas_regresion_lineal(x)
                activado[1] = 1
                etiqueta2 = "regresion_lineal"
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Opción para generar una linea con descenso del gradiente para los datos.
        elif respuesta == "7":
            #Para si no ha generado un data set
            if activado[0] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(4, x, dia)
            else:
                limpiar_consola()
                m_b = Generador_descenso_gradiente.generar_lineas_regresion_lineal(x)
                activado[1] = 1
                etiqueta2 = "descenso_gradiente"
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Para visualizar los datos de m y b.
        elif respuesta == "8":
            #Para si no ha escogido un archivo csv, ni generado puntos m y b.
            if activado[0] == 0 or activado[1] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                if activado[0] == 0:
                    mostrar_menu(4, x, dia)
                if activado[1] == 0:
                    mostrar_menu(10, x, dia)
            #Para si si lo hizo.
            else:
                #Menú para visualizar los m y b.
                limpiar_consola()
                mostrar_menu(9, x, dia)
                #Opción para escoger como quiere visualizar los m y b.
                respuesta = input("===>")            
                seguir = True
                while seguir:
                    seguir = False
                    #Para ver el total de m y b.
                    if respuesta == "1":
                        limpiar_consola()
                        mostrar_menu(1, x, dia)
                        mostrar_menu(8, x, len(m_b))
                    #Para ver los m y b
                    elif respuesta == "2":
                        limpiar_consola()
                        print("Respuesta:")
                        print(m_b)
                        mostrar_menu(1, x, dia)
                    #Para ver los m y b de un dia en especifico.
                    elif respuesta == "3":
                        #Menú para escoger un dia.
                        limpiar_consola()
                        mostrar_menu(6, x, dia)
                        seguir = True
                        while seguir:
                            seguir = False
                            try:
                                respuesta = int(input("===>"))-1
                                print("Respuesta:")
                                print(m_b[respuesta])            
                                mostrar_menu(1, x, dia)
                            #Excepciones
                            except ValueError:
                                seguir = True
                                limpiar_consola()
                                mostrar_menu(6, x, dia)
                                mostrar_menu(12, x, dia)
                            except IndexError:
                                seguir = True
                                limpiar_consola()
                                mostrar_menu(6, x, dia)
                                mostrar_menu(11, x, dia)                              
                    #Para si en el menú de visualización de m y b escogió una opción incorrecta.
                    else:
                        #Falta mensaje de no se pudo
                        limpiar_consola()
                        mostrar_menu(9, x, dia)
                        mostrar_menu(11, x, dia)
                        respuesta = input("===>")
                        seguir = True                         
            ##Para concluir
            respuesta = "0"
        ###Para graficar en matplotlib con la linea que mejor se ajuste.    
        elif respuesta == "9":
            #Para si no a escogido un archivo csv, ni a generado los m y b.
            if activado[0] == 0 or activado[1] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                if activado[0] == 0:
                    mostrar_menu(4, x, dia)
                if activado[1] == 0:
                    mostrar_menu(10, x, dia)
            #Para si sí lo hizo.
            else:
                limpiar_consola()
                Graficador_con_linea_matplotlib.graficar_datos(x, m_b, etiqueta1, etiqueta2)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Para generar una linea de regresion lineal para todos los m y b
        elif respuesta == "10":
            #Para si no ha generado un conjunto de m y b.
            if activado[1] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(10, x, dia)
            else:
                limpiar_consola()
                m_b_linea = Generador_regresion_lineal.generar_lineas_regresion_lineal([m_b])
                activado[2] = 1
                etiqueta3 = "regresion_lineal"
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"        
        ###Para graficar los m y b con sus puntos.
        elif respuesta == "12":
            #Para si no a generado los m y b, ni sus m y b.
            if activado[1] == 0 or activado[2] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                if activado[0] == 0:
                    mostrar_menu(10, x, dia)
                if activado[1] == 0:
                    mostrar_menu(14, x, dia)
            #Para si sí lo hizo.
            else:
                limpiar_consola()
                Graficador_con_linea_matplotlib.graficar_datos([m_b], m_b_linea, "m_b", etiqueta3)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ##########################################################################
        ###Para salir del programa.
        elif respuesta == "13":
            #Para si no ha escogido un archivo csv.
            if activado[0] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(4, x, dia)
            else:
                limpiar_consola()
                print("Respuesta:")
                Graficador_gnuplot.graficar_datos(x, etiqueta1)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
                #Para concluir
            respuesta = "0"   
        ###Para salir del programa.
        elif respuesta == "14":
            #Para si no a escogido un archivo csv, ni a generado los m y b.
            if activado[0] == 0 or activado[1] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                if activado[0] == 0:
                    mostrar_menu(4, x, dia)
                if activado[1] == 0:
                    mostrar_menu(10, x, dia)
            #Para si sí lo hizo.
            else:
                limpiar_consola()
                Graficador_con_linea_gnuplot.graficar_datos(x, m_b, etiqueta1, etiqueta2)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Para salir del programa.
        elif respuesta == "15":
            #Para si no a generado los m y b, ni sus m y b.
            if activado[1] == 0 or activado[2] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                if activado[0] == 0:
                    mostrar_menu(10, x, dia)
                if activado[2] == 0:
                    mostrar_menu(14, x, dia)
            #Para si sí lo hizo.
            else:
                limpiar_consola()
                Graficador_con_linea_gnuplot.graficar_datos([m_b], m_b_linea, "m_b", etiqueta3)            
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Para mostrar los m y b de los m y b.
        elif respuesta == "16":
            if activado[2] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(14, x, dia)
            else:
                limpiar_consola()
                print("Respuesta:")
                print(m_b_linea)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
        ###Para generar una regresion polinomial para los dias
        elif respuesta == "17":
            #Para si no ha escogido un archivo csv.
            if activado[0] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(4, x, dia)
            else:
                #Menú para escoger un grado del polinomio.
                        limpiar_consola()
                        mostrar_menu(15, x, dia)
                        seguir = True
                        while seguir:
                            seguir = False
                            try:
                                respuesta = int(input("===>"))
                                limpiar_consola()
                                ass = Generador_regresion_polinomial.generar_regresion_polinomial(x, respuesta)
                                activado[3] = 1
                                etiqueta4 = "regresion_polinomial"
                                mostrar_menu(1, x, dia)
                                mostrar_menu(3, x, dia)
                            #Excepciones
                            except ValueError:
                                seguir = True
                                limpiar_consola()
                                mostrar_menu(15, x, dia)
                                mostrar_menu(12, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Para salir del programa.
        elif respuesta == "18":
            #Para si no ha escogido un archivo csv.
            if activado[1] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(10, x, dia)
            else:
                #Menú para escoger un grado del polinomio.
                        limpiar_consola()
                        mostrar_menu(15, x, dia)
                        seguir = True
                        while seguir:
                            seguir = False
                            try:
                                respuesta = int(input("===>"))
                                limpiar_consola()
                                ass_linea = Generador_regresion_polinomial.generar_regresion_polinomial([m_b], respuesta)
                                activado[4] = 1
                                etiqueta4 = "regresion_polinomial"
                                mostrar_menu(1, x, dia)
                                mostrar_menu(3, x, dia)
                            #Excepciones
                            except ValueError:
                                seguir = True
                                limpiar_consola()
                                mostrar_menu(15, x, dia)
                                mostrar_menu(12, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Para salir del programa.
        elif respuesta == "19":
            #Para si no a escogido un archivo csv, ni a generado el polinomio.
            if activado[0] == 0 or activado[3] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                if activado[0] == 0:
                    mostrar_menu(4, x, dia)
                if activado[3] == 0:
                    mostrar_menu(16, x, dia)
            #Para si sí lo hizo.
            else:
                limpiar_consola()
                Graficador_con_polinomio_matplotlib.graficar_datos(x, ass, etiqueta1, etiqueta4)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Para salir del programa.
        elif respuesta == "20":
            #Para si no a generado un m y b, ni a generado los polinomio.
            if activado[1] == 0 or activado[4] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                if activado[1] == 0:
                    mostrar_menu(10, x, dia)
                if activado[4] == 0:
                    mostrar_menu(17, x, dia)
            #Para si sí lo hizo.
            else:
                limpiar_consola()
                Graficador_con_polinomio_matplotlib.graficar_datos([m_b], ass_linea, "m_b", etiqueta4)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ###
        #elif respuesta == "21":
        #    break
        ###
        #elif respuesta == "22":
        #    break
        ###Para mostrar los coeficientes de los dias.
        elif respuesta == "23":
            #Para si no ha generado unos coeficientes.
            if activado[3] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(16, x, dia)
            else:
                #Menú para escoger un grado del polinomio.
                limpiar_consola()
                print("Respuesta:")
                print(ass)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
            
        ###Para mostrar los coeficientes de los -m- y -b-
        elif respuesta == "24":
            #Para si no ha generado unos coeficientes.
            if activado[4] == 0:
                limpiar_consola()
                mostrar_menu(1, x, dia)
                mostrar_menu(17, x, dia)
            else:
                #Menú para escoger un grado del polinomio.
                limpiar_consola()
                print("Respuesta:")
                print(ass)
                mostrar_menu(1, x, dia)
                mostrar_menu(3, x, dia)
            ##Para concluir
            respuesta = "0"
        ###Para salir del programa.
        elif respuesta == "25":
            break
        else:
            limpiar_consola()
            mostrar_menu(1, x, dia)
            mostrar_menu(11, x, dia)
           
#Función para limpiar consola.            
def limpiar_consola():
    # Comando para limpiar la consola
    if os.name == 'posix':  # Para sistemas Unix/Linux (incluyendo macOS)
        _ = os.system('clear')  # Comando para limpiar en Unix/Linux
    else:  # Para sistemas Windows
        _ = os.system('cls')  # Comando para limpiar en Windows
###Menus:
def mostrar_menu(tipo, x, dia):
    #Menú principal
    if tipo == 1:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃   ┃                  ===== Menú Principal ====                       ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
        print("┃1. ┃ Leer archivo csv, extraer y normalizar datos.                    ┃")
        print("┃2. ┃ Visualizar datos extraidos y normalizados.                       ┃")
        print("┃3. ┃ Graficar los datos como puntos en matplotlib.                    ┃")
        print("┃4. ┃ Crear un archivo txt individual por cada día de los datos.       ┃")
        print("┃5. ┃ Crear un archivo txt grupal por para todos los dias de los datos.┃")
        print("┃6. ┃ Generar una línea de regresión lineal para todos los días.       ┃")
        print("┃7. ┃ Generar una línea con descenso del gradiente para los días.      ┃")
        print("┃8. ┃ Visualizar los -m- y -b- generados de todos los días.            ┃")
        print("┃9. ┃ Graficar los datos como puntos en matplotlib con sus -m- y -b-.  ┃")
        print("┃10.┃ Generar una línea de regresión lineal para los -m- y -b-         ┃")
        print("┃11.┃ Generar una línea con descenso del gradiente para los -m- y -b-  ┃")
        print("┃12.┃ Graficar los -m- y -b- con sus propios -m- y -b- con matplotlib. ┃")
        
        print("┃13.┃ Graficar los datos como puntos en gnuplot.                       ┃")
        print("┃14.┃ Graficar los datos como puntos en gnuplot con sus -m- y -b-.     ┃")
        print("┃15.┃ Graficar los -m- y -b- con sus propios -m- y -b- con gnuplot.    ┃")
        print("┃16.┃ Visualizar los -m- y -b- generados de todos los -m- y -b-        ┃")

        print("┃17.┃ Generar una regresión polinomial para todos los días.            ┃")
        print("┃18.┃ Generar una regresión polinomial para los -m- y -b-              ┃")
        print("┃19.┃ Graficar los datos como puntos en matplotlib con su polinomio    ┃")
        print("┃20.┃ Graficar los -m- y -b- con su polinomio con matplotlib.          ┃")
        print("┃21.┃ ----------------------------------------------------             ┃")
        print("┃22.┃ ----------------------------------------------------             ┃")
        print("┃23.┃ Para pintar en pantalla los coeficientes del set de dato         ┃")
        print("┃24.┃ Para pintar en pantalla los coeficientes de los -m- y -b-        ┃")
        print("┃25.┃ Finalizar aplicación.                                            ┃")
        print("└───┴──────────────────────────────────────────────────────────────────┘")
    #Para extraer datos.
    if tipo == 2:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃   ┃             ===== Normalizar y extraer datos ====                ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
        print("┃1. ┃ Para el primer conjuto de datos: datos1.csv                      ┃")
        print("┃2. ┃ Para el segundo conjuto de datos: datos2.csv                     ┃")
        print("┃3. ┃ Para el tercer conjuto de datos: datos3.csv                      ┃")
        print("┃4. ┃ Para el cuarto conjuto de datos: datos4.csv                      ┃")
        print("└───┴──────────────────────────────────────────────────────────────────┘")
    #Si escogio los datos de un dia.
    elif tipo == 3:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃ == Se ha realizado satisfactoriamente la operación. ==           ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio los datos de un dia.
    elif tipo == 4:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃ == No ha generado un set de datos, tiene que hacerlo primero. == ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogió visualizar datos extraidos y normalizados.
    elif tipo == 5:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃   ┃                  ===== Visualizar datos ====                     ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
        print("┃1. ┃ Mostrar Cantidad total de datos.                                 ┃")
        print("┃2. ┃ Mostrar todos los datos. (No recomendable por ser demaciados)    ┃")
        print("┃3. ┃ Mostrar la datos de un dia.                                      ┃")
        print("┃4. ┃ Mostrar una fila de datos de un dia.                             ┃") 
        print("└───┴──────────────────────────────────────────────────────────────────┘")
    #Si escogio los datos de un dia.
    elif tipo == 6:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃ == Digite el dia - Dias posibles: "+str(len(x))+" ==                        ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio una fila de un dia. 
    elif tipo == 7:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃ == Digite la fila - filas posibles:"+str(len(x[dia]))+" ==                       ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Resultado. 
    elif tipo == 8:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃ == Resultado:"+str(len(x))+" ==                                             ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogió visualizar datos extraidos y normalizados.
    elif tipo == 9:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃   ┃              ===== Visualizar -m- y -b- ====                     ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
        print("┃1. ┃ Mostrar Cantidad total de -m- y -b-.                             ┃")
        print("┃2. ┃ Mostrar todos los -m- y -b-. (No recomendable por ser demaciados)┃")
        print("┃3. ┃ Mostrar los -m- y -b- de un dia.                                 ┃")
        print("└───┴──────────────────────────────────────────────────────────────────┘")
    #Si escogio los datos de un dia.
    elif tipo == 10:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃   == No ha generado un conjunto de -m- y -b-, necesitas unos ==  ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio los datos de un dia.
    elif tipo == 11:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃   == La respuesta está fuera del rango de opciones válidas. ==   ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio los datos de un dia.
    elif tipo == 12:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃   == El dato ingresado no es numérico. Inténtelo nuevamente. ==  ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio los datos de un dia.
    elif tipo == 13:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃                == ¡Aplicación finalizada! ==                   ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio los datos de un dia.
    elif tipo == 14:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃     == Necesita otros -m- y -b- para graficar la línea. ==       ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio los datos de un dia.
    elif tipo == 15:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃             == Digite el grado del polinomio ==                  ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio los datos de un dia.
    elif tipo == 16:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃     == No ha generado un polinomio para el set de datos ==       ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    #Si escogio los datos de un dia.
    elif tipo == 17:
        print("┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ℹ. ┃      == No ha generado un polinomio para los -m- y -b- ==        ┃")
        print("┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
menu()
