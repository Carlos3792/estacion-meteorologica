#Librerias.
import subprocess
import os
#Para graficar las datas.
def graficar_datos(arreglo, m_b, nombre, tipo_linea):
    ##Crear la subcarpeta si no existe.
    subcarpeta = "Graficas"
    if not os.path.exists(subcarpeta):
        os.makedirs(subcarpeta)
    #Variable para definir etiquetas.
    otra = False
    if len(arreglo[0][0]) == 3:
        #Crear un archivo para guardar las instrucciones de Gnuplot.
        gnuplot_script = f"""
        set terminal pdfcairo enhanced
        set output '{subcarpeta}/Graficas_gnuplot-{tipo_linea}-{nombre}.pdf'
        set xlabel 'Hora num'
        set ylabel 'Temperatura exterior (°C)'
        set grid
        set pointsize 0.5
        """
    else:
        #Crear un archivo para guardar las instrucciones de Gnuplot.
        gnuplot_script = f"""
        set terminal pdfcairo enhanced
        set output '{subcarpeta}/Graficas_gnuplot-{tipo_linea}-{nombre}.pdf'
        set xlabel 'm'
        set ylabel 'b'
        set grid
        set pointsize 0.5
        """
    linea = 0
    #Para extraer la temperatura y horas de un dia.
    for idx, i in enumerate(arreglo):
        datos_x = []
        datos_y = []
        etiqueta = ""
        for e in i:
            datos_x.append(e[len(e)-2])     #[1]
            datos_y.append(e[len(e)-1])     #[2]
            if len(e)-3 >= 0:
                etiqueta = e[0]         #[0]
            else:
                etiqueta = nombre
                otra = True
        m = m_b[linea][0]  
        b = m_b[linea][1]
        #Instrucciones de Gnuplot para graficar.
        if otra:
            gnuplot_script += f"""
            set title 'b por m - {etiqueta}'
            f(x) = {m}*x + {b} 
            plot '-' using 1:2 with points pointtype 7 title '{etiqueta}', \
                f(x) with lines title "Funcion lineal y = mx + b"  
            """
        else:
            gnuplot_script += f"""
            set title 'Temperatura Exterior por Hora - {etiqueta}'
            f(x) = {m}*x + {b}
            plot '-' using 1:2 with points pointtype 7 title '{etiqueta}', \
                f(x) with lines title "Funcion lineal y = mx + b"  
            """
        linea = linea+1
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

    print(f"Se han guardado todas las gráficas en 'Graficas_gnuplot-{tipo_linea}-{nombre}.pdf'")

