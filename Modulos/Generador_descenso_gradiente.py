#Función para generar las líneas de regresión lineal utilizando el descenso del gradiente
def generar_lineas_regresion_lineal(arreglo):
    # Parámetros del descenso del gradiente
    alpha = 0.01  # Tasa de aprendizaje
    iteraciones = 1000
    b_m = []
    for i in arreglo:
        x = []
        y = []
        for e in i:
            x.append(e[1])
            y.append(e[2])

        # Ajustar los coeficientes utilizando el descenso del gradiente
        theta = ajustar_coeficientes(x, y, alpha, iteraciones)
        b_m.append([theta[1], theta[0]])

    return b_m


#Función para calcular la hipótesis (predicción).
def hipotesis(theta, x):
    return theta[0] + theta[1] * x

#Función para calcular la función de costo (MSE). #se usa para observar cómo el costo disminuye a lo largo del tiempo y asegurarse de que el algoritmo está convergiendo.
def costo(theta, x, y):
    m = len(y)
    J = 0
    for i in range(m):
        J += (hipotesis(theta, x[i]) - y[i]) ** 2
    return J / (2 * m)

#Función para calcular el gradiente del costo.
def gradiente(theta, x, y):
    m = len(y)
    grad = [0, 0]
    for i in range(m):
        grad[0] += (hipotesis(theta, x[i]) - y[i])
        grad[1] += (hipotesis(theta, x[i]) - y[i]) * x[i]
    grad[0] /= m
    grad[1] /= m
    return grad

# Función para el descenso del gradiente
def descenso_gradiente(x, y, alpha, iteraciones):
    theta = [0, 0]  # Inicializar theta
    for _ in range(iteraciones):
        grad = gradiente(theta, x, y)
        theta[0] -= alpha * grad[0]
        theta[1] -= alpha * grad[1]
    return theta

#Función para ajustar los coeficientes usando el descenso del gradiente
def ajustar_coeficientes(x, y, alpha, iteraciones):
    return descenso_gradiente(x, y, alpha, iteraciones)
