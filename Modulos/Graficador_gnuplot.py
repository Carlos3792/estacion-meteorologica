#Librerias.
import subprocess
import os
#Para graficar las datas
def graficar_datos(arreglo, nombre):
    ##Crear la subcarpeta si no existe
    subcarpeta = "Graficas"
    if not os.path.exists(subcarpeta):
        os.makedirs(subcarpeta)
    #Crear un archivo para guardar las instrucciones de Gnuplot.
    gnuplot_script = f"""
    set terminal pdfcairo enhanced
    set output '{subcarpeta}/Graficas_gnuplot-{nombre}.pdf'
    set xlabel 'Hora num'
    set ylabel 'Temperatura exterior (°C)'

    set grid
    set pointsize 0.5
    
    """    
    # Para extraer la temperatura y horas de un dia.
    for idx, i in enumerate(arreglo):
        datos_x = []
        datos_y = []
        etiqueta = ""
        for e in i:
            datos_x.append(e[1])
            datos_y.append(e[2])
            etiqueta = e[0]
        #Instrucciones de Gnuplot para graficar.
        gnuplot_script += f"""
        set title 'Temperatura Exterior por Hora - {etiqueta}'
        plot '-' using 1:2 with points pointtype 7 title '{etiqueta}'  
        """
        #gnuplot_script += f"""
        #set title 'Temperatura Exterior por Hora - {etiqueta}'
        #plot '-' with points pointtype 7 title '{etiqueta}'
        #"""
        for x, y in zip(datos_x, datos_y):
            gnuplot_script += f"\n{x} {y}"

        gnuplot_script += "\ne\n"    
    #Ejecutar Gnuplot con el script usando subprocess.
    process = subprocess.Popen(['gnuplot'], stdin=subprocess.PIPE, text=True)
    process.communicate(gnuplot_script)

    print(f"Se han guardado todas las gráficas en 'Graficas_gnuplot-{nombre}.pdf'")


