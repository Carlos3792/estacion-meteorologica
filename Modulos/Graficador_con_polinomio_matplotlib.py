#Librerias.
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#Función para graficar.
def graficar_datos(arreglo, coeficientes_polinomiales, nombre, tipo_linea):
    #Variable para definir etiquetas
    otra = False
    ##Crear la carpeta si no existe
    if not os.path.exists("Graficas"):
        os.makedirs("Graficas")
    ##Para guardar en subcarpeta.
    nombre_pdf = os.path.join("Graficas", 'Graficas_matplotlib-'+str(tipo_linea)+'-'+str(nombre)+'.pdf')   
    #Crear un archivo PDF para guardar las gráficas.
    with PdfPages(nombre_pdf) as pdf:
        #Para extraer los puntos b y m de cada data de cada dia.
        linea = 0
        #Para extraer la temperatura y horas de un dia.
        for i in arreglo:
            datos_x = []
            datos_y = []
            for e in i:
                datos_x.append(e[len(e)-2])     #[1]
                datos_y.append(e[len(e)-1])     #[2]
            if len(e)-3 >= 0:
                etiqueta = e[0]               #[0]
            else:
                etiqueta = nombre
                otra = True
            #Graficar los puntos de datos.
            #plt.plot(datos_x, datos_y, label=str(etiqueta))
            #Para simplificar los puntos. 'o',
            plt.scatter(datos_x, datos_y, label=str(etiqueta), s=5) #10 # Usar plt.scatter para solo puntos y s para el tamaño   
            #
            # Generar puntos para la curva del polinomio
            x_range = list(range(int(min(datos_x)), int(max(datos_x)) + 1))
            y_range = [sum(coef * (x**exp) for exp, coef in enumerate(coeficientes_polinomiales[linea])) for x in x_range]
            # Graficar la línea de regresión.
            #x_range = [min(datos_x), max(datos_x)]
            #y_range = [m_b[linea][1] + m_b[linea][0] * x for x in x_range] #[m_b[linea][0] + m_b[linea][1]
            plt.plot(x_range, y_range, 'r', label=f'Regresión polinomial ({etiqueta})')
            #------------------------------------------
            #Para poner las etiquetas al grafico.
            if otra:
                plt.xlabel('m')
                plt.ylabel('b')
                plt.title(f'b por m - {etiqueta}')
                plt.legend()
            else:              
                plt.xlabel('Hora num')
                plt.ylabel('Temperatura exterior (°C)')
                plt.title(f'Temperatura Exterior por Hora - {etiqueta}')
                plt.legend()
            #Guardar la gráfica en el archivo PDF.
            pdf.savefig()
            plt.clf()  #Limpiar la figura para la siguiente gráfica.
            #Para ir cambiando de linea de regresión lineal para graficarla junto con los puntos.
            linea = linea+1
    print("Se han guardado todas las gráficas en 'Graficas_matplotlib-"+str(tipo_linea)+"-"+str(nombre)+".pdf'")

