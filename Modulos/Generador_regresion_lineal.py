#Función para sacar los m y b de los puntos del arreglo.
def generar_lineas_regresion_lineal(arreglo):
    m_b = []
    for i in arreglo:
        m_b.append(regresion_lineal(i))
    return m_b
#Función donde ocurre la regresión lineal.
def regresion_lineal(arreglo):
    ##Extración de los x y y.
    x = [punto[-2] for punto in arreglo]
    y = [punto[-1] for punto in arreglo]
    #Sumatoria de x elevados a la 2.
    x_e2 = 0
    for i in x:
        x_e2 = x_e2+i**2
    #Sumatoria de x.
    x_sum = sum(x)
    #Total de datos.
    n = len(x)
    #Construccion de m.
    m = [[x_e2, x_sum],[x_sum, n]]
    #Producto punto entre x y y.
    pt = 0
    for i in range(len(x)):
        pt = pt+(x[i]*y[i])
    #Sacar sumatoria de los y.
    y_sum = sum(y)
    #Construccion de d
    d = [pt, y_sum]
    #Sacar inversa de m
    m_inv = invM(m)
    #multiplicar matrices
    d = [d]
    c = multmatporvector(m_inv, d) 
    return c

###Funciones de danny:
def Mmenor(M,i,j):
    m=[]
    for ii in range(len(M)):
        if ii !=i:
            fila=[]
            for jj in range(len(M[ii])):
                if jj!=j:
                    fila.append(M[ii][jj])
            m.append(fila)
    return m

def det(M):
    if len(M)==1:
        return M[0][0]
    suma=0
    for i in range(len(M)):
        Mm=Mmenor(M,0,i)
        suma=suma+((-1)**i)*M[0][i]*det(Mm)
    return suma

def tras(A):
    mat=[]
    for j in range(len(A[0])):
        fila=[]
        for i in range(len(A)):
            fila.append(A[i][j])
        mat.append(fila)
    return mat

def adj(M):
    m=[]
    for i in range(len(M)):
        fila=[]
        for j in range(len(M)):
            fila.append(((-1)**(i+j))*det(Mmenor(M,i,j)))
        m.append(fila)
    return m

def proporesc(alfa,A):
    arre=[]
    for i in range(len(A)):
        arre.append(alfa*A[i])
    return arre

def promatporesc(alfa,W):
    mat=[]
    for i in range(len(W)):
        mat.append(proporesc(alfa,W[i]))
    return mat

def invM(M):
    return promatporesc(1/det(M),tras(adj(M)))

def multmat(A,B):
    mult=[]
    for i in range(len(A)):
        fila=[]
        for j in range(len(B[1])):
            suma=0
            for k in range(len(A[i])):
                suma=suma+A[i][k]*B[k][j]
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

        
        
        
    

