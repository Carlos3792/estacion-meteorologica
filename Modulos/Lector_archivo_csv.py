#Función para extrar el tiempo y la temperatura del archivo csv y dividirlo en datas por dia.
def leer_normalizar(archivo):
    #Para abrir el archivo csv.
    with open(str(archivo), "r") as archivo:
        #Lee todas las líneas excepto la primera (encabezado) #readlines() lee cada linea del archivo. #[1:] para que inicie por el primer archivo. 
        lineas = archivo.readlines()[1:]
        #Para guardar todos los datos en un arreglo.
        data = []
        #Recorrido por cada linea guardada en "lineas".
        for linea in lineas:
            #Divide la línea por comas.
            campos = linea.strip().split(",")
            #Guardamos cada fila.
            data.append(campos)
        #Para dividir la data por dias #dia_act = dia act.
        dia_act = ""
        #Para solo tomar los dias de la segunda columna/Fecha y hora.  21</>12/2012 12:10
        for i in data[0][1]:
            if i == "/":
                break
            dia_act = dia_act+i    
        #Esta es la data final, la data con los datos normalizados. #data_f = data_final.
        data_f = []
        #Para guardar temporalmente la data de un dia, que corresponde a todos los datos de un dia. #data_d = data de un dia.
        data_d = []
        #Recorrido para normalizar los datos
        for i in data:
            #Arreglo para guardar temporalmente una fila de una data de un dia.
            fila = []
            #Variables para guardar los datos de tiempo:
            fecha = ""
            hora = ""
            minuto = ""
            #Recorrido para dividir la segunda tabla en fecha, hora y minuto.
            for e in range(len(i[1])):
                #Para tomar fecha.
                if e < len(i[1])-5:
                    fecha = fecha+i[1][e]
                #Para tomar hora.
                elif e < len(i[1])-3:
                    hora = hora+i[1][e]
                #Para tomar minuto.
                elif e > len(i[1])-3:
                    minuto = minuto+i[1][e]
            #Sacamos las horas totales, al sumar las horas por los minutos divididos por 60. 
            hora = float(hora)+(float(minuto)/60)
            #Guardamos en la primer fila todos los datos necesarios.
            fila.append(fecha.replace(" ", ""))
            fila.append(hora)
            try:
                fila.append(float(i[5])) #Para coger la temperatura.
            except ValueError:
                continue
            #Para tomar el dia de cada iteración y verificar si es igual o no al actual #Esto se hace para dividir la data por dias.
            dia_sig = ""
            #Sacando el dia de esta iteración.
            for e in i[1]:
                if e == "/":
                    break
                dia_sig = dia_sig+e
            #Validamos si la fila obtenida corresponde el mismo dia o a otro.
            if dia_sig != dia_act:
                #Guardamos la data del dia en la data final.
                data_f.append(data_d)
                #Limpiamos para seguir con la siguiente data del siguiente dia.
                data_d = []
                #Primer elemento de la siguiente data.
                data_d.append(fila)######
                #Cambiamos el dia actual, para validar con este dia y no el anterior.
                dia_act = dia_sig
            #Si no corresponde al mismo dia, entonces seguimos guardando las filas(datos) en la misma data del mismo dia.
            else:
                data_d.append(fila)
        #Para guardar la data del ultimo dia. 
        data_f.append(data_d)
        #Mensaje
        print("Todos los datos han sido extraídos y normalizados en una variable temporal.")
        #Para retornar la data
        return data_f

##Vista de como seria una fila antes y despues de la normalización.  
#Estructura de una fila original:
#print(['1192', '21/09/2018 08:57', '5', '24.6', '64', '24.6', '63', '29.89', '26.34', '0', '0', '---', '17.1', '24.6', '0', '0', '0', '0', '0'])
#Estructura obtenida:
#print(['21/09/2018 ', 8.95, '24.6'])

