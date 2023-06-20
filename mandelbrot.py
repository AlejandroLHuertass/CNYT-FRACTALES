import numpy as np
import matplotlib.pyplot as plt



''''Define la función mandelbrot que recibe un arreglo c y el número máximo de iteraciones max_iter. Esta función calcula el conjunto de Mandelbrot y devuelve una máscara booleana indicando qué puntos del plano complejo pertenecen al conjunto.'''
def mandelbrot(c, max_iter):
    '''Crea un arreglo de ceros con la misma forma y tipo de c para almacenar los valores iterativos de la secuencia de Mandelbrot.'''
    z = np.zeros_like(c)
    '''Crea una máscara booleana con la misma forma que c y todos sus elementos inicializados en True. Esta máscara se utiliza para filtrar los puntos que todavía pueden pertenecer al conjunto de Mandelbrot.'''
    mascara = np.ones_like(c, dtype=bool)
    for i in range(max_iter):
        '''Actualiza los valores en z aplicando la fórmula iterativa del conjunto de Mandelbrot solo para los puntos que todavía pueden pertenecer al conjunto, utilizando la máscara.'''
        z[mascara] = z[mascara] * z[mascara] + c[mascara]
        '''Actualiza la máscara booleana filtrando los puntos que aún cumplen con la condición de estar dentro de un límite arbitrario (en este caso, se verifica que la magnitud de z sea menor que 2).'''
        mascara = np.logical_and(mascara, np.abs(z) < 2)
    return mascara


'''Define la función dibujar_mandelbrot que toma los límites del plano complejo, el ancho y alto de la imagen, y el número máximo de iteraciones.'''
def dibujar_mandelbrot():
    
    x_min = float(input("\n¿Que valor minimo al eje x? : "))
    x_max = float(input("\n¿Que valor maximo al eje x? : "))
    y_min = float(input("\n¿Que valor minimo al eje y? : "))
    y_max = float(input("\n¿Que valor maximo al eje y? : "))
    max_iter = int(input("\n¿Que valor de iteraciones desea? : "))
    
    '''
    x_max = -2.0
    x_min = 1.0
    y_min = 1.5
    y_max = -1.5
    max_iter = 25
    '''
       
    '''
    x_min = -0.74877
    x_max = -0.74872
    y_min = 0.06505
    y_max = 0.06510
    max_iter = 500'''
    
    '''Crea un arreglo de puntos espaciados uniformemente en el eje x dentro del rango dado por x_min y x_max.'''
    xs = np.linspace(x_min, x_max, 800)
    '''Crea un arreglo de puntos espaciados uniformemente en el eje y dentro del rango dado por y_min y y_max.'''
    ys = np.linspace(y_min, y_max, 600)
    '''Crea una rejilla bidimensional con los arreglos xs e ys, donde xv representa los valores de x repetidos a lo largo del eje y y yv representa los valores de y repetidos a lo largo del eje x.'''
    xv, yv = np.meshgrid(xs, ys)
    '''Crea un arreglo complejo c a partir de la rejilla xv e yv.'''
    c = xv + yv * 1j
    '''Calcula el conjunto de Mandelbrot llamando a la función mandelbrot con el arreglo complejo c y el número máximo de iteraciones.'''
    fractal = mandelbrot(c, max_iter)

    '''Crea una nueva figura para la visualización con un tamaño específico (8 pulgadas de ancho y 6 pulgadas de alto).'''
    plt.figure(figsize=(8, 6))
    ''''Muestra la imagen del conjunto de Mandelbrot utilizando la función imshow de Matplotlib. fractal.T transpone la matriz del fractal para que se muestre correctamente. Se utiliza el mapa de colores 'hot' para la visualización. El parámetro extent define los límites del plano complejo a mostrar.'''
    plt.imshow(fractal.T, cmap='hot', extent=[y_min, y_max, x_min, x_max])
    plt.ylabel('Real(c)')
    plt.xlabel('Im(i)')
    plt.title('Conjunto de Mandelbrot')
    plt.show()

'''Define la función dibujar_triangulo_sierpinski que toma como argumentos un objeto de ejes (ax), el nivel actual de recursión (nivel), y las coordenadas de los vértices del triángulo (p1, p2, p3). Esta función dibuja el Triángulo de Sierpinski utilizando recursividad.'''

def dibujar_triangulo_sierpinski(ax, nivel, p1, p2, p3):
    '''Si el nivel de recursión es 0, se dibuja el triángulo base utilizando la función fill() de los ejes ax.'''
    if nivel == 0:
        # Dibujar el triángulo base
        ax.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'k')
    else:
        ''' De lo contrario, se calculan los puntos medios de cada lado del triángulo mediante promedios de las coordenadas de los vértices.
        Se llama recursivamente a la función dibujar_triangulo_sierpinski para los tres nuevos triángulos generados, con un nivel de recursión reducido en 1.'''

        # Calcular los puntos medios de cada lado del triángulo
        p12 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        p23 = [(p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2]
        p31 = [(p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2]
        
        # Llamar recursivamente a la función para los tres nuevos triángulos
        dibujar_triangulo_sierpinski(ax, nivel-1, p1, p12, p31)
        dibujar_triangulo_sierpinski(ax, nivel-1, p12, p2, p23)
        dibujar_triangulo_sierpinski(ax, nivel-1, p31, p23, p3)

'''Define la función dibujar_triangulo que toma como argumento el número de niveles de recursión (niveles). Esta función se encarga de crear los ejes y configuraciones para el gráfico del Triángulo de Sierpinski.'''
def dibujar_triangulo(niveles):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    '''Crea una figura y ejes utilizando subplots(), configura el aspecto para que sea igual en todas las dimensiones con set_aspect('equal') y oculta los ejes con axis('off').'''
    
    # Coordenadas del triángulo inicial
    p1 = [0, 0]
    p2 = [0.5, 1]
    p3 = [1, 0]
    '''Define las coordenadas de los vértices del triángulo inicial.'''
    
    dibujar_triangulo_sierpinski(ax, niveles, p1, p2, p3)
    plt.show()

def main():
    print("Bienvenido a la graficadora de fractales\n")
    print("En este programa puedes generar fractales a partir del conjunto de Mandelbrot o de los Triángulo de Sierpinski\n")

    print("Presione 1 si desea generar fractales a partir del conjunto de Mandelbrot\nPresione 2 si desea generar fractales a partir de los Triángulo de Sierpinski\n" )
    bandera=True
    while bandera == True:
        opcion = input()
        
        if opcion == "1":
            dibujar_mandelbrot()
            bandera = False

        elif opcion == "2":
            niveles = int(input("¿Que etapa desea observar? : "))
            dibujar_triangulo(niveles-1)
            bandera = False
        else:
            print("\nPor favor digite una opcion valida\n")
        

main()

    
