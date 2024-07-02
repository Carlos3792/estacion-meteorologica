#Librerías.
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#Función para graficar.
def graficar_datos(arreglo, nombre):
    ##Crear la carpeta si no existe
    if not os.path.exists("Graficas"):
        os.makedirs("Graficas")
    ##Para guardar en subcarpeta.
    nombre_pdf = os.path.join("Graficas", 'Graficas_matplotlib-'+str(nombre)+'.pdf')
    #Crear un archivo PDF para guardar las gráficas.
    with PdfPages(nombre_pdf) as pdf:
        #Para extraer la temperatura y horas de un día.
        for i in arreglo:
            datos_x = []
            datos_y = []
            for e in i:
                datos_x.append(e[1])
                datos_y.append(e[2])
            etiqueta = e[0]
            #Graficar los puntos de datos.
            plt.scatter(datos_x, datos_y, label=str(etiqueta), s=5)  #10 # Usar plt.scatter para solo puntos y s para el tamaño
            #Para poner las etiquetas al gráfico.
            plt.xlabel('Hora num')
            plt.ylabel('Temperatura exterior (°C)')
            plt.title(f'Temperatura Exterior por Hora - {etiqueta}')
            plt.legend()
            #Guardar la gráfica en el archivo PDF.
            pdf.savefig()
            plt.clf()  #Limpiar la figura para la siguiente gráfica.
    print("Se han guardado todas las gráficas en 'Graficas_matplotlib-"+str(nombre)+".pdf'")

