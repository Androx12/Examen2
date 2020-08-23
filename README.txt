Andrey Rivera Quesada
Josue Valverde Domínguez


Link en GIT: https://github.com/Androx12/Examen2.git

Este programa se ejecuta desde el modulo main.py y cuenta con un solo directorio
El modulo main realiza la distribución completa de los demas modulos

****** El programa realiza lo siguiente:

Es una mesa de poker en la que existe una baraja de cartas se pueden realizar las siguientes acciones.

1 Crear una baraja ("/deck/new")
2 Revolver la baraja ("/deck/shuffle")
3 Ver las cartas que quedan en la baraja ("/deck/show/remain")
4 Tomar una carta para jugar ("/deck/pickone")
5 Ver las cartas que tengo en la mano ("/user/show/hand")
6 Ver las posibles jugadas que tengo en mano ("/user/play")

FUNCIONALIDADES

1 Se crea una baraja de cartas completa en un archivo json

2 Si la baraja existe la revuelve, si no indica que no hay cartas disponibles

3 Muestras las cartas que hay en la baraja, de no existir indica que no hay cartas disponibles

4 Toma una carta de la baraja la elimina y la guarda en un json llamado 'barajaMano', de no existir indica que no hay cartas disponibles

5 Muestras las cartas que hay en la mano, de no existir indica que no hay cartas en mano

6 Realiza un calculo de las posibles jugadas que pueden haber en la mano, de no existir cartas en mano indica que no hay cartas

****** El programa realiza validaciones como:

Verificar si existen cartas antes de intentar revovler, tomar o mostrar

OTRAS NOTAS:
Solo ejecutar desde el MAIN, el archivo 'logicaCartas.py' se uso exclusivamente para realizar pruebas desde consola, no afecta el comportamiento en ejecución. 