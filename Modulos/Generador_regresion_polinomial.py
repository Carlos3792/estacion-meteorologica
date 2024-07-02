def generar_regresion_polinomial(arreglo, grado):
    coeficientes = []
    for datos in arreglo:
        coeficientes.append(regresion_polinomial(datos, grado))
    return coeficientes

def regresion_polinomial(arreglo, grado):
    #Extracción de los x y y
    x = [punto[-2] for punto in arreglo]
    y = [punto[-1] for punto in arreglo]  
    # Calcular las sumas necesarias:
    #TOtal de datos
    n = len(x)
    #Sumatorias de x y x*y elevando x 
    sum_x = [sum(xi**k for xi in x) for k in range(2 * grado + 1)]
    sum_yx = [sum(yi * (xi**k) for xi, yi in zip(x, y)) for k in range(grado + 1)]
    
    #Formar el sistema de ecuaciones normal - las a y el b
    A = [[sum_x[i + j] for j in range(grado + 1)] for i in range(grado + 1)]
    b = sum_yx
    
    #Resolver el sistema de ecuaciones
    A_inv = invM(A)
    coeficientes = multmatporvector(A_inv, [b])
    
    return coeficientes

# Funciones de álgebra lineal de Danny
def Mmenor(M, i, j):
    m = []
    for ii in range(len(M)):
        if ii != i:
            fila = []
            for jj in range(len(M[ii])):
                if jj != j:
                    fila.append(M[ii][jj])
            m.append(fila)
    return m

def det(M):
    if len(M) == 1:
        return M[0][0]
    suma = 0
    for i in range(len(M)):
        Mm = Mmenor(M, 0, i)
        suma = suma + ((-1) ** i) * M[0][i] * det(Mm)
    return suma

def tras(A):
    mat=[]
    for j in range(len(A[0])):
        fila=[]
        for i in range(len(A)):
            fila.append(A[i][j])
        mat.append(fila)
    return mat

#def tras(A):
#    return list(map(list, zip(*A)))

def adj(M):
    m = []
    for i in range(len(M)):
        fila = []
        for j in range(len(M)):
            fila.append(((-1) ** (i + j)) * det(Mmenor(M, i, j)))
        m.append(fila)
    return m

def proporesc(alfa,A):
    arre=[]
    for i in range(len(A)):
        arre.append(alfa*A[i])
    return arre

#def proporesc(alfa, A):
#    return [[alfa * elem for elem in fila] for fila in A]

def promatporesc(alfa,W):
    mat=[]
    for i in range(len(W)):
        mat.append(proporesc(alfa,W[i]))
    return mat

#def promatporesc(alfa, W):
#    return proporesc(alfa, W)

def invM(M):
    return promatporesc(1 / det(M), tras(adj(M)))

def multmat(A, B):
    mult = []
    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(A[0])):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        mult.append(fila)
    return mult

def multmatporvector(A,B): #version modificada para mult. matriz por vector. vector debe pasarse como matriz de 1 columna.
    mult=[]
    for i in range(len(A)):
          suma=0
          for k in range(len(A[i])):
              suma=suma+A[i][k]*B[0][k]
          mult.append(suma)
    return mult

#def multmatporvector(A, B): 
#    return [sum(A[i][k] * B[0][k] for k in range(len(A[i]))) for i in range(len(A))]



