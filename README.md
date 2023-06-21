#  Fractales

Un fractal es una figura o patrón que se repite a diferentes escalas y detalles infinitos. Es como una estructura matemática que exhibe autosimilitud, lo que significa que partes más pequeñas de la figura se asemejan a la figura completa.

Un ejemplo comúnmente conocido de fractal es el conjunto de Mandelbrot, que tiene una forma geométrica. Otros ejemplos incluyen el triángulo de Sierpinski, el helecho de Barnsley y el copo de nieve de Koch las cuales generan similitudes a escalas diferentes y esta propiedad se refleja en la naturaleza repetitiva, dejo algunos ejemplos.


<img src="https://github.com/AlejandroLHuertass/CNYT-FRACTALES/assets/88836525/4b4ddbc3-b502-4f9c-bce4-cb907ddbd68d](https://www.aepjp.es/wp-content/uploads/2020/08/bird-wing-colorful-fauna-material-peacock-1159930-pxhere-com-1024x768.jpg" width="200" height="200" />
<img src="https://pijamasurf.com/wp-content/uploads/10.208.149.45/uploads/2013/02/snowflake.jpeg" width="200" height="200" />
Los fractales tienen aplicaciones en matemáticas, física, informática, arte y muchas otras áreas.
Relación con los números complejos

Un fractal se puede generar iterativamente aplicando una función matemática a un número complejo inicial y repitiendo el proceso varias veces. Esta función toma como entrada un número complejo y produce un nuevo número complejo como resultado. La función puede ser no lineal y puede implicar operaciones como la multiplicación, la suma o la exponenciación de números complejos.

## El conjunto de MandelBrot

El conjunto de Mandelbrot es un ejemplo destacado de fractal relacionado con los números complejos, y su visualización revela patrones intrigantes y detalles infinitos.
Esto nos planea que los números complejos están compuestos por una parte real y una parte imaginaria y se pueden representar como puntos en el plano complejo. Si vemos el eje x representara la parte real y el eje y representa la parte imaginaria. La combinación de estos dos componentes crea un espacio matemático que se genera a partir de las ecuaciones desarrolladas por MandelBrot.
Cabe destacas que una de las características es que fractales exhiben autosimilitud, lo que significa que presentan patrones similares a diferentes escalas. Cada parte de un fractal se asemeja al conjunto completo, lo que da lugar a una estructura recursiva. 

El conjunto de Mandelbrot es uno de los fractales más conocidos y se basa en la iteración de una función específica donde cada uno de sus resultados se pueden colocar en un plano complejo y a través de colores mostrar fractales. 

### ¿Como funciona la formula para generar un fractal a partir conjunto de Mandelbrot?

Para generar el conjunto de Mandelbrot, se usa una fórmula muy sencilla que se repite muchas veces. La fórmula es z = z^2 + c, donde z y c son números complejos. Comenzamos con un valor inicial de z y luego aplicamos la fórmula una y otra vez hasta alcanzar un numero de repeticiones que ya vienen definidas.

El valor absoluto de "z" nos permite medir qué tan lejos está "z" del origen, que es el punto (0, 0) en el plano complejo. Si el valor absoluto de "z" se mantiene por debajo del umbral establecido, que por lo general es 2, durante todas las iteraciones y este tiende a 0, podemos concluir que la secuencia es acotada y el punto pertenece al conjunto de Mandelbrot.

Por otro lado, si en algún momento el valor absoluto de "z" supera el umbral de 2 durante las iteraciones, significa que la secuencia está creciendo rápidamente y divergiendo o con tendencia al infinito. En este caso, concluimos que el punto está fuera del conjunto de Mandelbrot.

El conjunto de Mandelbrot está formado por todos los puntos en un plano complejo para los cuales la secuencia correspondiente es acotada. Estos puntos se pintan de negro en una imagen del conjunto de Mandelbrot. Los puntos que están fuera del conjunto se pintan con diferentes colores según qué tan rápido divergen.

La parte interesante del conjunto de Mandelbrot es que, cuando te acercas y haces zoom en diferentes partes de la imagen, aparecen patrones muy detallados y complicados. Estos patrones se repiten a diferentes escalas y crean estructuras fractales, que son como figuras que se repiten una y otra vez.


## El Triangulo de Sepienski

El triángulo de Sierpinski es un ejemplo clásico de cómo una figura simple puede generar una estructura compleja mediante la repetición de un patrón básico. 
### ¿Como funciona?

La idea se basa en la de división del triángulo en triángulos más pequeños mediante puntos medios. Por ejemplo, si tenemos un triángulo donde sus 3 puntas se llaman A, B y C, si queremos generar el siguiente nivel de triángulos más pequeños podemos empezar encontrando el punto medio para cada lado del triángulo, estos puntos medios los llamaremos D, E y F, Luego, construimos los tres triángulos más pequeños utilizando los vértices del triángulo original y los puntos medios:
Triángulo superior: vértices (A, D, E)
Triángulo inferior izquierdo: vértices (D, B, F)
Triángulo inferior derecho: vértices (E, F, C)
Este proceso se repite para cada uno de los triángulos más pequeños generados, dividiendo cada lado en segmentos y construyendo triángulos nuevos con los puntos medios.
La clave de esta fórmula es que se basa en la división en tercios de cada lado del triángulo original. Al repetir este proceso de división y construcción de triángulos más pequeños, se obtiene la estructura fractal del Triángulo de Sierpinski.

## En conclusión

los fractales son patrones geométricos complejos que se repiten infinitamente. Pueden generarse utilizando números complejos, como en el conjunto de MandelBrot, o mediante procesos de división y repetición, como en el Triángulo de Sierpinski.
El estudio de los Fractales ha generado diversas aplicaciones como en las telecomunicaciones y compresión de datos donde fractales se han utilizado para la compresión de datos en aplicaciones como la transmisión de imágenes y videos. 

También en Modelado de fenómenos naturales donde los fractales se utilizan para modelar y comprender fenómenos naturales complejos. Por ejemplo, se han aplicado fractales en la meteorología para analizar y predecir patrones climáticos

## Bibliografía 

1. BBC Mundo, Qué son los fractales y cómo pueden ayudarnos a entender el universo | (https://www.youtube.com/watch?v=4u7TwSwo0rU&t=120s&ab_channel=BBCNewsMundo)
2. Aceff Sánchez, F. de. (2000). Fractales. Pro Mathematica, 14(27-28), 121-133. Recuperado a partir de (https://revistas.pucp.edu.pe/index.php/promathematica/article/view/8162)


